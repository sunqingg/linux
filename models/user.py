# from models import db
from sqlalchemy import Column,Integer,String,ForeignKey

from flask_sqlalchemy import SQLAlchemy
from apps import app
import hashlib

db = SQLAlchemy(app)

user_role = db.Table('user_role',
                     Column('user_id', Integer, ForeignKey('user.id', name='user_role_fk')),
                     Column('role_id', Integer, ForeignKey('role.id', name='user_role_pk')))


class BaseModel(db.Model):
    __abstract__ = True  # 作用： 不会创建模型的对应的表
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), unique=True, nullable=False)


class Role(BaseModel):
    __tablename__ = 'role'


class QX(BaseModel):
    __tablename__ = 'qx'


class User(db.Model):
    id = Column(Integer,
                primary_key=True,
                autoincrement=True)
    phone = Column(String(20),
                   unique=True,
                   nullable=False)
    auth_key = Column(String(100), nullable=False)
    nick_name = Column(String(20))
    photo = Column(String(100))

    # role_id = Column(ForeignKey('role.id'))
    # Many-to-Many 多对多的关系，指定secondary设置关联的表，Table()
    roles = db.relationship(Role, secondary=user_role)

def crypt(text):
    md5 = hashlib.md5()
    md5.update(text.encode('utf8'))
    return md5.hexdigest()

def add_user():
    u1 = User()
    u1.phone = '18161685383'
    u1.auth_key = crypt('123456')
    u1.nick_name = 'sunqingniubi@888'

    u2 = User()
    u2.phone = '17791692096'
    u2.auth_key = crypt('123456')
    u2.nick_name = 'Disen@888'

    db.session.add_all((u1, u2))
    db.session.commit()
    print('提交之后的User-Id:', u1.id, u2.id)


def add_role():
    r1 = Role(name='系统管理员')
    r2 = Role(name='普通用户')

    db.session.add_all((r1, r2))
    db.session.commit()
    print('提交之后的User-Id:', r1.id, r2.id)


def add_user_role():

    # db.Table()不能作为模型类使用
    # db.session.add_all((
    #     user_role(user_id=1, role_id=1),
    #     user_role(user_id=2, role_id=1),
    #     user_role(user_id=2, role_id=2)
    # ))

    # 为用户ID为1的用户增加"系统管理员" 角色
    u = User.query.get(1)

    admin_role = Role.query.filter(Role.name.__eq__('系统管理员')).one()
    print(u.nick_name, admin_role.name)

    # 将角色对象添加给用户
    u.roles.append(admin_role)
    # db.session.add_all(u)
    #如果是更新
    db.session.commit()
    print('ok')

def query_user_role(user_id=1):
    u = User.query.get(user_id)
    print('------拥有的角色-------')
    for role in u.roles:
        print(role.name)


if __name__ == '__main__':
    # app.app_context().push()
    # db.init_app(app)

    add_user()
    add_role()
    add_user_role()
    query_user_role(1)








#---------------------------------------------
# class Role(db.Model):
#     # 定义表名
#     __tablename__ = 'roles'
#     # 定义字段
#     # db.Column 表示是一个字段
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(16), unique=True)
#
#
# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(16), unique=True)
#     role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
#---------------------------------------------

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









