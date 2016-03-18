FROM python:3.5.1

# install popular modules
# (do this first so Docker can reuse cached containers on rebuild)
RUN pip3 install requests werkzeug

# add our library
ADD hookscript.py /usr/local/lib/python3.5/

# add build scripts
ADD compile /bin/
ADD run /bin/
