FROM python:3.4.3-wheezy

# install popular modules
# (do this first so Docker can reuse cached containers on rebuild)
RUN pip3 install requests werkzeug

# add our library
ADD hookscript.py /usr/local/lib/python3.4/

# add build scripts
ADD compile /bin/
ADD run /bin/
