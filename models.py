from peewee import *
from flask_login import UserMixin

DATABASE = SqliteDatabase('guitar.sqlite')

class User(UserMixin, Model):
  username=CharField(unique=True)
  password=CharField()

  class Meta:
    database = DATABASE

class Guitar(Model):
  name = CharField()
  is_electric = BooleanField()
  price = DoubleField()

  class Meta:
    database = DATABASE

def initialize():
  DATABASE.connect()

  DATABASE.create_tables([Guitar, User], safe=True)
  print('connect to database and create tables')

DATABASE.close()