import hookscript

state = hookscript.state

if state == None:
    state = 0
state += 1
print(state, end='')

hookscript.state = state
