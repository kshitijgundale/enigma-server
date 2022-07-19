import json
from urllib import response
from app import app
from flask import request, jsonify
from app.forms import SignUpForm, LoginForm
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, \
    jwt_required, set_access_cookies, set_refresh_cookies, unset_access_cookies, unset_refresh_cookies
from werkzeug.security import generate_password_hash, check_password_hash
from app.mongo import create_user, get_user_by_email

@app.route('/users', methods=['POST'])
def users():

    form = SignUpForm(request.get_json())

    if form.validate():
        user_data = {
            'email': form.data['email'],
            'password_hash': generate_password_hash(form.data['password']),
            'username': form.data['username']
        }
        user = get_user_by_email(form.data['email'])
        if user:
            return "Email already exists", 409
        else:
            user_id = create_user(user=user_data)
            access_token = create_access_token(identity=form.data['email'])
            refresh_token = create_refresh_token(identity=form.data['email'])
            response = jsonify(email=form.data['email'], username=form.data['username'])
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
            return response, 201

    else:
        return jsonify(form.errors), 400

@app.route('/login', methods=['POST'])
def login():

    form = LoginForm(request.get_json())

    if form.validate():
        user = get_user_by_email(form.data['email'])
        if user and check_password_hash(user['password_hash'], form.data['password']):
            access_token = create_access_token(identity=form.data['email'])
            refresh_token = create_refresh_token(identity=form.data['email'])
            response = jsonify(email=user['email'], username=user['username'])
            set_access_cookies(response, access_token)
            set_refresh_cookies(response, refresh_token)
            return response, 201
        else:
            return "Invalid email or password", 401
    else:
        return jsonify(form.errors), 400

@app.route('/auth')
@jwt_required()
def auth():
    email = get_jwt_identity()
    user = get_user_by_email(email)
    return {
        'email': email,
        'username': user['username']
    }, 200

@app.route('/logout')
def logout():
    response = jsonify(message="logged out")
    unset_access_cookies(response)
    unset_refresh_cookies(response)

    return response, 200
