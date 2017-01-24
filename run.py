#! /usr/bin/env python3
# encoding:utf-8

from flask import *
from models.user import User,loginRegister

app = Flask(__name__)


@app.route('/')
def index():

    # if 'username' in session:
    #     return render_template('home.html',username=escape(session['username']))

    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':

        log_username=request.form['username']
        log_password=request.form['password']

        if loginRegister().query(log_username,log_password): 
            session['username']=request.form['username']
            return redirect(url_for('user'))
    return  render_template('login.html')


@app.route('/register',methods=['GET','POST'])
def register():

    if request.method == 'POST':

            reg_username=request.form['reg_username']
            reg_password=request.form['reg_password']
            loginRegister().register(reg_username,reg_password)

            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))


@app.route('/user')
def user():

    user=User(1,escape(session['username']))
    return render_template('home.html',user=user)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


@app.route('/article')
def article():
    pass


if __name__ == '__main__':
        app.debug=True
        app.run(host='0.0.0.0')


