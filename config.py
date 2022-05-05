import os

base_dir = os.path.dirname(os.path.abspath(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    TEST_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Зачем эта настройка: https://flask-sqlalchemy-russian.readthedocs.io/ru/latest/config.html#id2
    DEBUG = True
    PORT = 5000
    SECRET_KEY = "My secret key =)"
    RESTFUL_JSON = {
        'ensure_ascii': False,
    }
    UPLOAD_FOLDER_NAME = 'upload'
    UPLOAD_FOLDER = os.path.join(base_dir, UPLOAD_FOLDER_NAME)

    LANGUAGES = ['en', 'ru']

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'arsymasterov'
    MAIL_PASSWORD = 'ripper111'

    # administrator list
    ADMINS = ['arsymasterov@gmail.com']