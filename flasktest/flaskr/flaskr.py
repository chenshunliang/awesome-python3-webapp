import sqlhelper
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from contextlib import closing

# configuration
HOST = '127.0.0.1'
DATABASE = 'flasktest'
DEBUG = True
SECRET_KEY = ''
USERNAME = 'sa'
PASSWORD = '1qazxsw@'

app = Flask(__name__)
app.config.from_object(__name__)


# 连接sqllite数据库
def connect_db():
    # app.logger.info(app.config['DATABASE'])
    return sqlhelper.SqlServer(host=app.config['HOST'], user=app.config['USERNAME'], pwd=app.config['PASSWORD'],
                               db=app.config['DATABASE'])


# 初始化数据库
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('/static/schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


if __name__ == '__main__':
    app.run(debug=True)
