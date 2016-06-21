import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or "18205680850@163.com"
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or "159357caonima"
    FLASKY_MAIL_SUBJECT_PREFIX = '[Splunk-auto-data-onboarding]'
    FLASKY_MAIL_SENDER = 'Spider Admin <18205680850@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN') or "jiwu@qti.qualcomm.com"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'mysql://root:159357@localhost/spider' 


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
        'mysql://www-data:www-data@localhost/spider'


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql://www-data:www-data@localhost/spider'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
