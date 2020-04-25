from peewee import *


DATABASE = SqliteDatabase('guitar.sqlite')

class Guitar(Model):
  name = CharField()
  is_electric = BooleanField()
  price = DoubleField()

  class Meta:
    database = DATABASE

def initialize():
  DATABASE.connect()

  DATABASE.create_tables([Guitar], safe=True)
  print('connect to database and create tables')

DATABASE.close()