from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)

class Config(object):
    DEBUG = True
    # 数据库配置信息
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #redis配置
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    """工程配置信息"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    # flask_session配置信息
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True  # 让cookie中的session——id被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400  # 设置session的有效期




app.config.from_object(Config)
db = SQLAlchemy(app)
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
Session(app)
# csrf防护
CSRFProtect(app)
# 数据库迁移扩展
manager = Manager(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)




@app.route('/index')
def index():
    return 'index'


if __name__ == '__main__':
    manager.run()
