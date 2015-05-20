from hookscript import request

resource = request.values['resource']
if resource == 'cpu':
    while True:
        pass
elif resource == 'mem':
    x = 'xxxxxxxxxxxxxxxxxx'
    while True:
        x += x
elif resource == 'disk':
    f = open('junk','w')
    while True:
        print('junk', file=f)
elif resource == 'output':
    i = 1000000
    while i > 0:
        print('junk')
        i -= 1
