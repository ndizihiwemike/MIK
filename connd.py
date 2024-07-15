'part2: connecting postgreSQL to python'
import psycopg2
from config import config
 # connection = psycopg2.connect(
  #  host = "mike", user="postgres",
  #  password="m18989422")

def connect():
    connection = None
    try:
        params = config()
        print('connecting to the postgreSQL database ...')
        connection = psycopg2.connect(**params)

        # create a curser
        curser = connection.curser()
        print('postgreSQL database version: ')
        curser.execute('SELECT version()')
        db_version = curser.fetchone()
        print(db_version)
    except(Exception, psycopg2.databaseError) as error:
      print(error)