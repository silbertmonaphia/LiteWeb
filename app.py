#! /usr/bin/env python3
# encoding:utf-8

import datetime
from flask import Flask, redirect, url_for, Response, request, render_template, session, escape
from models.user import User, loginRegister
from flask_mongoengine import MongoEngine
from flaskext.markdown import Markdown

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'article',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine(app)
md = Markdown(app, extensions=['footnotes'], entension_configs={
              'footnotes': ('PLACE_MARKER', '```')}, safe_mode=True, output_format='html4')

app.secret_key = 'Z1Jr22~j/3lRX MM!XjbN]LwX/,BT?'


class Post(db.Document):
    author = db.StringField(max_length=50)
    title = db.StringField(max_length=120, required=True)
    tags = db.ListField(db.StringField(max_length=30))
    time = db.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    content = db.StringField()


@app.errorhandler(404)
def not_found(exc):
    return Response('<h3>页面丢失，或不具有访问权限</h3>'), 404


@app.route('/')
def index():

    if 'username' in session:
        return redirect(url_for('article'))

    return redirect(url_for('login'))


# userinfo pages
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        log_username = request.form['username']
        log_password = request.form['password']

        if loginRegister().query(log_username, log_password):
            session['username'] = request.form['username']
            return redirect(url_for('user'))
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        reg_username = request.form['reg_username']
        reg_password = request.form['reg_password']
        invitation_code = request.form['invitation_code']
        print(type(reg_password))
        print(type(reg_password))
        print(type(invitation_code))
        if invitation_code == 'DoNotWearRedHat':
            loginRegister().register(reg_username, reg_password)
            return redirect(url_for('login'))
        else:
            return Response('<h3>邀请码错误</h3>')

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))


@app.route('/user')
def user():

    return redirect(url_for('article'))

# show articles


@app.route('/article')
def article():
    if 'username' in session:
        posts = Post.objects.all()
        user = User(user_id=1, user_name=escape(session['username']))
        return render_template('articles.html', title='articles', posts=posts, user=user)
    else:
        return redirect(url_for('login'))

# show detail of blog


@app.route('/post/<string:title>')
def detail(title):

    if 'username' in session:

        user = User(user_id=1, user_name=escape(session['username']))
        post = Post.objects.get_or_404(author=session["username"], title=title)

        return render_template('detail.html', title="details", post=post, user=user)

    else:

        return redirect(url_for('login'))

# create and edit articles


@app.route('/create/', methods=['GET', 'POST'])
def create():
    if 'username' in session:

        if request.method == 'POST':
            author = session['username']
            title = request.form['title']
            tags_str = request.form['tags']
            tags = tags_str.split('#')
            content = request.form['content']
            post = Post(author=author, title=title, tags=tags, content=content)
            post.save()
            return redirect(url_for('article'))

        user = User(user_id=1, user_name=escape(session['username']))
        return render_template('create.html', user=user)

    else:
        return redirect(url_for('login'))


@app.route('/<string:title>/edit/', methods=['GET', 'POST'])
def edit(title):
    if 'username' in session:
        if request.method == 'POST':
            author = session['username']
            title = request.form['title']
            tags_str = request.form['tags']
            tags = tags_str.split('#')
            content = request.form['content']
            post_new = Post(author=author, title=title,
                            tags=tags, content=content)
            Post.objects(author=author, title=title).delete()
            post_new.save()

        user = User(user_id=1, user_name=escape(session['username']))
        post = Post.objects.get_or_404(author=session["username"], title=title)
        tag_bag = ''
        for tag in post.tags:
            if tag != '':
                tag_bag += ('#' + tag)
        post.tags = tag_bag
        user = User(user_id=1, user_name=escape(session['username']))
        return render_template('edit.html', title="edit", post=post, user=user)
    else:
        return redirect(url_for('login'))


@app.route('/<string:title>/delete/', methods=['GET', 'POST'])
def delete(title):
    if 'username' in session:
        Post.objects(author=session['username'], title=title).delete()
        return redirect(url_for('article'))
    else:
        return redirect(url_for('login'))


def main():
    app.debug = True
    #context = ('/etc/ssl/certs/1_smona.info_bundle.crt', '/etc/ssl/private/2_smona.info.key')
    app.run(host='0.0.0.0', port=5001)

if __name__ == '__main__':
    main()
