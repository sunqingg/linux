# from models import db
# from sqlalchemy import Column,Integer,String

from flask_sqlalchemy import SQLAlchemy
from apps import app

db = SQLAlchemy(app)


class Role(db.Model):
    # 定义表名
    __tablename__ = 'roles'
    # 定义字段
    # db.Column 表示是一个字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


# class User(db.Model):
#     __tablename__ = 'students'
#     id = Column(Integer,
#                 primary_key=True,
#                 autoincrement=True)
#     phone = Column(
#         String(20),
#         unique=True,
#         nullable=False
#     )
#     auht_key = Column(String(100),
#                       nullable=False,)
#     nick_name = Column(
#         String(20),
#         nullable=False
#     )
#     photo = Column(
#         String(100)
#     )









