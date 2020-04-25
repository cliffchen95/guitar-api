from flask import Flask

from resources.guitars import guitars

import models

DEBUG=True
PORT=8000

app = Flask(__name__)

app.register_blueprint(guitars, url_prefix='/api/v1/guitars')

@app.route('/')
def hello():
  return 'server running'


if __name__ == '__main__':
  
  models.initialize()

  app.run(debug=DEBUG, port=PORT);