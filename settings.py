import os

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.join(PROJECT_DIR, 'apps')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
USER_DIR = os.path.join(STATIC_DIR, 'user')

class Dev():
    ENV = 'development'
    DEBUG = True

    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@160.6.68.3:3306/edu?charset=utf8'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@160.6.68.3:3306/edu?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # SQLALCHEMY_ECHO = True


# if __name__ == '__main__':
#     print(PROJECT_DIR)
#     print(BASE_DIR)