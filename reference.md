# Python Reference

See also Hookscript's [general documentation](http://docs.hookscript.com/)

## Hookscript module

Each Python script should begin with `import hookscript` or `from hookscript import ...`.  The module has the following variables available:

  * `request` represents the incoming HTTP request
  * `response` represents the outgoing HTTP response
  * `state` whose value is persisted across script invocations

## HTTP Request

An incoming HTTP request is represented by a [Werkzeug request](http://werkzeug.pocoo.org/docs/0.10/quickstart/#enter-request) value. This value is available as `hookscript.request`.

## HTTP Response

A script doesn't need an explicit response value. Anything sent to `sys.stdout` stream becomes the HTTP response body. However, if you want to modify HTTP response headers, you can call methods on `hookscript.response`. This is a [Werkzeug response](http://werkzeug.pocoo.org/docs/0.10/quickstart/#responses) value.
