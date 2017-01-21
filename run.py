#! /usr/bin/env python3
#encoding:utf-8

from flask import *
from models import User
from 

app = Flask(__name__)


@app.route('/')
def index():
    '''
    主页登陆后显示最新的10篇文章
    '''

    if 'username' in session:
        return render_template('home.html',username=escape(session['username']))

    return redirect(url_for('login'))


@app.route('/login', methods=['GET','POST'])
def login():


        if request.method == 'POST':
            session['username']=request.form['username']
            return redirect(url_for('user'))

        return  render_template('login.html')


@app.route('/register')
def register():
    '''
    把用户的注册信息写入数据库
    '''

    return  render_template('register.html')




@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('login'))


@app.route('/user')
def user():

    user=User(1,escape(session['username']))
    return render_template('home.html',user=user)

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
        app.debug=True
        app.run(host='0.0.0.0')

