import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_login import login_user

from playhouse.shortcuts import model_to_dict

User = models.User


users = Blueprint('user', 'users')

@users.route('/', methods=['GET', 'POST', 'DELETE'])
def test():
  if request.method == 'GET':
    return 'connect'

  if request.method == 'POST':
    payload = request.get_json()
    payload['username'] = payload['username'].lower()
    try:
      User.get(User.username == payload['username'])
      return jsonify(
        data={},
        message=f"the username {payload['username']} is taken",
        status=401
      ), 401

    except models.DoesNotExist:
      pw_hash = generate_password_hash(payload['password'])
      user = User.create(
        username=payload['username'],
        password=pw_hash
      )
      user_dict = model_to_dict(user)
      user_dict.pop('password')

      return jsonify(
        data=user_dict,
        message=f"Successfully register user {user_dict['username']}",
        status=201
      ), 201


  if request.method == 'DELETE':
    return 'delete route'

@users.route('/login', methods=['POST'])
def login():
  payload = request.get_json()
  payload['username'] = payload['username'].lower()
  try:
    user = User.get(User.username == payload['username'])
    user_dict = model_to_dict(user)
    if check_password_hash(user_dict['password'], payload['password']):
      login_user(user)
      user_dict.pop('password')

      return jsonify(
        data=user_dict,
        message=f"{user_dict['username']} logged in!",
        status=200
      ), 200

  except models.DoesNotExist:
    return jsonify(
      data={},
      message='Username or password is incorrect',
      status=401
    ), 401
