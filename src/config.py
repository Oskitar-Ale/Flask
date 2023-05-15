class Config:
    SECRET_KEY = 'secreto'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '123'
    MYSQL_DB = 'flask_login'

config = {
    'development': DevelopmentConfig
}
