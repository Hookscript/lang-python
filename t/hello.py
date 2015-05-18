from hookscript import request

whom = request.values.get('whom','world')
print('Hello, %s!' % whom)
