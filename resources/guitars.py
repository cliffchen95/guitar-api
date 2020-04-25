import models

from flask import Blueprint, request

guitars = Blueprint('guitars', 'guitars')

@guitars.route('/', methods=['GET'])
def hello_guitar():
  return "Hello guitar!"

@guitars.route('/', methods=['POST'])
def create_dog():
  payload = request.get_json()
  print(payload)
  
  return "you hit post"