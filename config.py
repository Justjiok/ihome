import logging
import redis


class Config(object):
    DEBUG = True
    # 数据库配置信息
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/information'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #redis配置
    REDIS_HOST = '192.168.140.130'
    REDIS_PORT = 6379

    """工程配置信息"""
    SECRET_KEY = "EjpNVSNQTyGi1VvWECj9TvC/+kq3oujee2kTfQUs8yCM6xX9Yjq52v54g+HVoknA"
    # flask_session配置信息
    SESSION_TYPE = 'redis'
    SESSION_USE_SIGNER = True  # 让cookie中的session——id被加密签名处理
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    PERMANENT_SESSION_LIFETIME = 86400  # 设置session的有效期


class DevelopementConfig(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG


class ProductionConfig(Config):
    DEBUG = False
    LOG_LEVEL = logging.ERROR


# 定义配置字典
config = {
    "development": DevelopementConfig,
    "production": ProductionConfig
}