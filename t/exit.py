from hookscript import request
import sys

x = request.values.get('try')
if x == '1':
    raise Exception('Try %s' % x)
elif x == '2':
    print('Try %s' % x, file=sys.stderr)
    sys.exit(1)
