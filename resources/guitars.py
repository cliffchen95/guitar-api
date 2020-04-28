import models
Guitar = models.Guitar
from flask import Blueprint, request, jsonify
from playhouse.shortcuts import model_to_dict

guitars = Blueprint('guitars', 'guitars')

@guitars.route('/', methods=['GET'])
def index_guitar():
  result = Guitar.select()
  data = []
  count = 0
  for guitar in result:
    count += 1
    data.append(model_to_dict(guitar))
  return jsonify(
    data=data,
    message=f"Successfully found {count} results",
    status=200
    ), 200

@guitars.route('/<id>', methods=['GET'])
def find_guitar(id):
  result = Guitar.select().where(Guitar.id==id)
  return jsonify(
    data=model_to_dict(result[0]),
    message=f"Successfully found 1 results",
    status=200
    ), 200

@guitars.route('/', methods=['POST'])
def create_guitar():
  payload = request.get_json()
  new_guitar = Guitar.create(
    name=payload['name'], 
    is_electric=payload['is_electric'], 
    price=payload['price']
  )
  
  guitar_dict = model_to_dict(new_guitar)
  return jsonify(
      data=guitar_dict,
      message="Successfully created 1 guitar!",
      status=201
    ), 201
# edit guitar
@guitars.route('/<id>', methods=['PUT'])
def edit_guitar(id):
  payload = request.get_json()

  query = Guitar.update(
    name=payload['name'], 
    is_electric=payload['is_electric'], 
    price=payload['price']
  ).where(Guitar.id == id)
  n = query.execute()

  updated_guitar = Guitar.get_by_id(id)
  return jsonify(
    data=model_to_dict(updated_guitar),
    message=f"Successfully edited guitar with id {id}",
    status=200
  ), 200

@guitars.route('/<id>', methods=['DELETE'])
def delete_guitar(id):
  query = Guitar.delete().where(Guitar.id == id)
  n = query.execute()
  return jsonify(
    data={},
    message=f"Successfully deleted {n} guitar with id {id}",
    status=200
  ), 200