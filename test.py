from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据库的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@160.6.68.3:3306/edu'
# 跟踪数据库的修改，不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

'''
两张表（管理员/普通用户)
用户（角色ID）
'''


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

@app.route('/drop_db')
def drop_db():
    db.drop_all()
    return '2'

@app.route('/create_db')
def create_db():
    db.create_all()
    return '1'

# db.drop_all()
# db.create_all()

@app.route('/')
def index():
    return "hahah"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
