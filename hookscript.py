#!/usr/bin/env python3

import atexit
import io
import sys

from http.server import BaseHTTPRequestHandler
from pprint import pprint
from werkzeug.wrappers import Request, Response

# exception thrown when parsing an invalid HTTP request
class MalformedHTTPRequest(Exception):
    def __init__(self,code,message):
        self.code = code
        self.message = message
    def __str__(self):
        return "Error parsing HTTP request (%d): %s" % (self.code, self.message)


# low-level parsing of an HTTP request file
class HTTPRequest(BaseHTTPRequestHandler):
    def __init__(self, request_file):
        self.rfile = open(request_file,'rb')
        self.raw_requestline = self.rfile.readline()
        self.parse_request()

    def send_error(self, code, message):
        raise MalformedHTTPRequest(code,message)

    def wsgi_environ(self):
        env = {
            'REQUEST_METHOD': self.command,
            'SERVER_NAME': 'www.runhook.com',
            'SERVER_PORT': '', # TODO depends on http vs https
            'SERVER_PROTOCOL': self.request_version,
        }

        # extract the query string
        try:
            qn = self.path.index('?')
            env['QUERY_STRING'] = self.path[qn+1:]
            path = self.path[0:qn]
        except ValueError:
            path = self.path

        # break apart the original path
        path_parts = path.split('/')
        env['SCRIPT_NAME'] = '/'.join(path_parts[0:2])
        env['PATH_INFO'] = '/'.join(path_parts[2:])

        # create HTTP_* entry for each header
        for k, v in self.headers.items():
            cgi_name = "HTTP_%s" % k.upper().replace('-','_')
            env[cgi_name] = v

        # handle headers with special CGI treatment
        if 'HTTP_CONTENT_TYPE' in env:
            env['CONTENT_TYPE'] = env['HTTP_CONTENT_TYPE']
        if 'HTTP_CONTENT_LENGTH' in env:
            env['CONTENT_LENGTH'] = env['HTTP_CONTENT_LENGTH']

        # WSGI environ keys
        env['wsgi.version'] = (1,0)
        env['wsgi.url_scheme'] = 'http' # TODO depends on http vs https
        env['wsgi.input'] = self.rfile
        env['wsgi.errors'] = open('log','a')
        env['wsgi.multithread'] = False
        env['wsgi.multiprocess'] = True
        env['wsgi.run_once'] = True

        return env


# build request and response object
wsgi_env = HTTPRequest('request').wsgi_environ()
request = Request(wsgi_env)
response = Response( content_type = 'text/plain' )

# capture anything printed to stdout
printed_content = io.StringIO()
sys.stdout = printed_content

# redirect stderr to the log file
sys.stderr = open('log', 'at')

# final clean up before interpreter exits
def onexit():

    # generate HTTP response
    response.data = printed_content.getvalue()
    with open('response', 'wt') as out:
        print('HTTP/1.1 %s' % response.status, file=out)
        for k,v in response.headers:
            print('%s: %s' % (k,v), file=out)
        print('', file=out)
        print(response.data.decode(), file=out, end='')
atexit.register(onexit)
