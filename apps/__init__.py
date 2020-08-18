from flask import Flask
# import settings
app = Flask(__name__)
# app.config.from_object(settings.Dev)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@160.6.68.3/edu?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
