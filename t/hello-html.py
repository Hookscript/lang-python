from hookscript import request, response
from string import Template

whom = request.values.get('whom','world')
response.headers['content-type'] = 'text/html'

t = Template('''
<html>
    <body>
        <h1>Hello, $whom!</h1>

        <form method=GET>
            <input type=submit value="Say Hello to" />
            <input type=text name=whom placeholder="world" />
        </form>
    </body>
</html>
''')
print(t.substitute(whom=whom))
