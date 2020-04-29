from flask import Flask

from resources.guitars import guitars
from resources.users import users
from flask_cors import CORS
from flask_login import LoginManager

import models

DEBUG=True
PORT=8000

app = Flask(__name__)

app.secret_key = "jfk231?fd31fjs==fa"

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
  try:
    user = models.User.get_by_id(user_id)
    return user
  except models.DoesNotExist:
    return None
    
CORS(guitars, origins=['http://localhost:3000'], supports_credentials=True)
app.register_blueprint(guitars, url_prefix='/api/v1/guitars')
app.register_blueprint(users, url_prefix='/api/v1/users')


@app.route('/')
def hello():
  return 'server running'


if __name__ == '__main__':
  
  models.initialize()

  app.run(debug=DEBUG, port=PORT);