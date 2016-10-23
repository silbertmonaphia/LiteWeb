#! /usr/bin/env python3
#encoding:utf-8

from flask import *
from models import User

app = Flask(__name__)


@app.route('/user')
def user():

    user=User(1,escape(session['username']))
    return render_template('index.html',user=user)

@app.route('/')
def index():

    if 'username' in session:
        print ('hello')
        return render_template('index.html',username=escape(session['username']))

    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():

        if request.method == 'POST':
            session['username']=request.form['username']
            return redirect(url_for('user'))

        return  render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
        app.debug=True
        app.run(host='0.0.0.0')

