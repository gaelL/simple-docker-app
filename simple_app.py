#!/usr/bin/env python

from flask import Flask, request, make_response
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    resp = make_response()
    resp.set_cookie('cookie_custom', value='values %s' % datetime.now())
    print dir(resp.response)
    # resp.headers['X-Parachutes'] = 'parachutes are cool'
    output = """######## Request headers :
%s

######## Request Cookies :
%s

######## Response Header :
%s
""" % (request.headers, request.cookies, resp.headers)
    resp.data = output
    print output
    return resp

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')

