#!/usr/bin/env python3

import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, send_from_directory, url_for

app = Flask(__name__)


def login_attempt(ip,user,password,user_agent):
    if os.path.exists("auth.log"):
        file_mode = 'a'
    else:
        file_mode = 'w'
    
    with open("/opt/jenkinspot/logs/auth.log", file_mode) as log:
        log_time = datetime.now()
        log.write(f'[{str(log_time.isoformat())}] - {ip} - user: {user} pass: {password} - {user_agent}\n')


@app.route('/jenkins/loginError')
def jenkins_login_error():
    return render_template('loginError'), 401


@app.route('/jenkins/j_acegi_security_check', methods=['GET', 'POST'])
def jenkins_sec_check():
    if request.method == 'POST':
        username = request.form['j_username']
        password = request.form['j_password']

        login_attempt(request.remote_addr,username,password,request.headers.get('User-Agent'))


    return redirect('/jenkins/loginError', code=302) 


@app.route('/jenkins/login', methods=['GET', 'POST'])
def jenkins_login():
    return render_template('login'), 200


@app.route('/')
def index():
    return redirect("/jenkins/login", code=302)


@app.route('/favicon.ico')
def favicon(response):
    response.headers['Content-Type'] = 'image/x-icon'
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/robots.txt')
def robots():
    return '''# we don't want robots to click "build" links
User-agent: *
Disallow: /
''', 200, {'Content-Type': 'plain'}


@app.after_request
def set_headers(response):
    response.headers["X-Jenkins"] = "2.263.4"
    response.headers["X-Hudson"] = "1.395"
    response.headers["X-Jenkins-Session"] = "84134e82"
    response.headers["Server"] = " Jetty(9.4.33.v20201020)"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Instance-Identity"] =  "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsOf3hLUyFD2ozsTrH/vc7+/2NK3Wk6HWnNuNaZTlOjcoC++UIxu8LwPt+XynuQli/VdQB/N7YlQo3xUHvvOwti9JH94xPflqIP4c6SgosKOnh+h6as0KJbz9ftWtj1fS9RHLe5FeBaxmIlZE03LkCaxux7gYRivfMz3xGcs+dkVX6douPmj+QduO0qgn2n/KRgZqVJ+XBqqe5iZbHc28ko7kXDdSZ9Nl47k+vKHpw6JhKcC8hCjHenqR04Vy7G62GTbhG0RReNIO4zCIGEH5P3N36ZPwhBbCUBwdRh3AexMtUwIMzr/G9ohuV3ujuHidw482YjteUjeisNM23l+AzQIDAQAB"
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)