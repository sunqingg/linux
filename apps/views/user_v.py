from flask import request,render_template
from apps import app
from flask import Blueprint, make_response, redirect, jsonify


blue = Blueprint('userBlue', __name__)

@blue.route('/login',methods=['GET','POST'])
def login():
    data = {
        'cookies': request.cookies,
        'base_url': request.base_url
    }
    return render_template('user/login.html',**data)
    print(cookies.get('token'))





