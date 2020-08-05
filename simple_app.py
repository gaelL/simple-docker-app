#!/usr/bin/env python

from flask import Flask, request, make_response
from datetime import datetime
import socket

app = Flask(__name__)

@app.errorhandler(404)
@app.route("/", methods=['GET', 'POST'])
def hello(error_404=None):

    resp = make_response()

    # Set random cookie
    resp.set_cookie('cookie_custom', value='values %s' % datetime.now())

    # print dir(resp.response)
    # resp.headers['X-Parachutes'] = 'parachutes are cool'
    output = """######## Request headers :
%s

######## Request Cookies :
%s

######## Request POST :
%s
%s

######## Server infos :
%s  -  %s

######## Response Header :
%s
""" % (request.headers,
       request.cookies,
       request.form.lists(),
       request.data,
       socket.gethostname(),
       socket.gethostbyname(socket.gethostname()),
       resp.headers)
    resp.data = output

    print output
    return resp

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')

