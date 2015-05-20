import hookscript
from hookscript import request

state = hookscript.state or {}

register = request.values.get('register', '')
if request.method == 'POST':
    value = request.values.get('value','default value')
    if register == 'death':
        raise Exception('I am dead')
    state[register] = value
else:
    value = state.get(register,'unknown register: %s' % register)

print(value, end='')
hookscript.state = state
