FROM python:3.4.3-wheezy

# add our library
ADD hookscript.py /usr/local/lib/python3.4/

# add build scripts
ADD compile /bin/
ADD run /bin/
