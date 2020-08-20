from flask import request, render_template
from apps import app
from flask import Blueprint, make_response, redirect, jsonify

from models.user import User, db, crypt
import uuid
from datetime import datetime, timedelta
from models.token_redis import save_token

blue = Blueprint('userBlue', __name__)


# @blue.route('/login',methods=['GET','POST'])
# def login():
#     data = {
#         'cookies': request.cookies,
#         'base_url': request.base_url
#     }
#     return render_template('user/login.html',**data)
#     print(cookies.get('token'))



@blue.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        phone = request.form.get('phone')
        passwd = request.form.get('passwd')
        print(crypt(passwd))
        login_user = User.query.filter(User.phone == phone,
                                       User.auth_key == crypt(passwd)).one()
        print(login_user)
        if login_user:
            token = uuid.uuid4().hex
            resp = redirect('/')
            resp.set_cookie('token', token, expires=(datetime.now() + timedelta(days=3)))

            save_token(token, login_user.id)
            return resp
        else:
            message = '没有这个人'
    return render_template('user/login.html', msg=message)

