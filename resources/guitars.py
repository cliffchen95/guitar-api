import models

from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

guitars = Blueprint('guitars', 'guitars')

@guitars.route('/', methods=['GET'])
def hello_guitar():
  return "Hello guitar!"

@guitars.route('/', methods=['POST'])
def create_guitar():
  payload = request.get_json()
  new_guitar = models.Guitar.create(name=payload['name'], is_electric=payload['is_electric'], price=payload['price'])
  print(new_guitar)
  guitar_dict = model_to_dict(new_guitar)
  return jsonify(
      data=guitar_dict,
      message="Successfully created dog!",
      status=201
    ), 201