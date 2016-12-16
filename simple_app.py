#!/usr/bin/env python

from flask import Flask, request, make_response
from datetime import datetime
import socket

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def hello():

    resp = make_response()

    # Set random cookie
    resp.set_cookie('cookie_custom', value='values %s' % datetime.now())

    # print dir(resp.response)
    # resp.headers['X-Parachutes'] = 'parachutes are cool'
    output = """"VERSION : %s

######## Request headers :
%s

######## Request Cookies :
%s

######## Request POST :
%s

######## Server infos :
%s  -  %s

######## Response Header :
%s
""" % ("@VERSION@",
       request.headers,
       request.cookies,
       request.form.lists(),
       socket.gethostname(),
       socket.gethostbyname(socket.gethostname()),
       resp.headers)
    resp.data = output
    print output
    return resp

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')

