import sqlhelper
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# configuration
HOST = '127.0.0.1'
DATABASE = 'flasktest'
DEBUG = True
SECRET_KEY = '1234567890zxcvbnm'
USERNAME = 'sa'
PASSWORD = '1qazxsw@'

app = Flask(__name__)
app.config.from_object(__name__)


# 连接sqllite数据库
def connect_db():
    # app.logger.info(app.config['DATABASE'])
    return sqlhelper.SqlServer(host=app.config['HOST'], user=app.config['USERNAME'], pwd=app.config['PASSWORD'],
                               db=app.config['DATABASE'])


# 初始化数据库 todo
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('/static/schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


# 列表页
@app.route('/')
def show_entries():
    db = connect_db()
    resList = db.ExecQuery('select id,title,text from entries')
    app.logger.debug(resList)
    entries = []
    for (id, title, text) in resList:
        entries.append({'id': id, 'title': title, 'text': text})
    app.logger.debug(entries)
    return render_template('show_entries.html', entries=entries)


# 添加数据
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('login_in'):
        abort(401)
    db = connect_db()
    db.ExecNonQuery('insert into entries values ({0},{1})'.format(request.form['title'], request.form['text']))
    flash('new entry was successful posted')
    return redirect(url_for('show_entries'))


# 登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'invalid username'
        if request.form['password'] != app.config['PASSWORD']:
            error = 'invalid password'
        else:
            session['login_in'] = True
            flash('you were login in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


# 退出
@app.route('/logout')
def logout():
    session.pop('login_in', None)
    flash('you were logout')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run(debug=True)
