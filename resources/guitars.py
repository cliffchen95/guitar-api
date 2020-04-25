import models

from flask import Blueprint

guitars = Blueprint('guitars', 'guitars')

@guitars.route('/', methods=['GET'])
def hello_guitar():
  return "Hello guitar!"

