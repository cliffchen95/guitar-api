from flask import Flask

from resources.guitars import guitars
from flask_cors import CORS

import models

DEBUG=True
PORT=8000

app = Flask(__name__)
CORS(guitars, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(guitars, url_prefix='/api/v1/guitars')


@app.route('/')
def hello():
  return 'server running'


if __name__ == '__main__':
  
  models.initialize()

  app.run(debug=DEBUG, port=PORT);