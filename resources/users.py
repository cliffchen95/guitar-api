import models

from flask import Blueprint

users = Blueprint('user', 'users')

@users.route('/', methods=['GET'])
def test():
  return 'connect'