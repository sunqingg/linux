from apps import app
from apps.views import user_v
from flask_script import Manager
from flask import render_template,request
from models.user import db
# from models import db
# from flask_sqlalchemy import SQLAlchemy
# from apps import app
#
# db = SQLAlchemy(app)

# @app.route('/',host='0.0.0.0')
# def index():
#     return render_template('index.html')

@app.route('/create_db')
def create_database():
    db.create_all()
    return '创建数据库中的所有模型表成功'

@app.route('/drop_db')
def drop_database():
    db.drop_all()
    return '删除数据库中的所有模型表'
@app.route('/')
def origin():
    return render_template('index.html')

# db.create_all()
if __name__ == '__main__':
    # 将蓝图注册到app中,url_prefix  蓝图需要经过这个URL的过滤
    app.register_blueprint(user_v.blue, url_prefix='/user')
    #
    # # 初始化数据库
    # # db.init_app(app)
    #
    manager = Manager(app)
    manager.run()
    # app.run(debug=True,host='0.0.0.0')








