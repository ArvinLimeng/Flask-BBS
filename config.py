import os

DEBUG = True

SECRET_KEY = os.urandom(24)

DIALECT = 'mysql'  # 要用的什么数据库
DRIVER = 'pymysql'  # 连接数据库驱动
USERNAME = 'root'  # 用户名
PASSWORD = 'root'  # 密码
HOST = 'localhost'  # 服务器
PORT = '3306'  # 端口
DATABASE = 'bbs'  # 数据库名

SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False