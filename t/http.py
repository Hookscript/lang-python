from hookscript import request, response
import requests

http = request.values['protocol']
file = request.values['file']
url = '%s://storage.googleapis.com/hookscript/%s' % (http,file)

r = requests.get(url)
if r.status_code == 200:
    print(r.text, end='')
else:
    response.status_code = r.status_code
    print('Request to %s failed' % url, end='')
