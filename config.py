import os

class Config(object):
   SQLALCHEMY_TRACK_MODIFICATIONS = False 
   DEBUG = False

class LocalConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'sqlite:///local.db'
   DEBUG = True

class GithubCIConfig(Config):
   SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"  # In-memory SQLite for tests
   TESTING = True
   DEBUG = True

class DevelopmentConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}?sslmode=require'.format(
       dbuser=os.getenv('DBUSER'),
       dbpass=os.getenv('DBPASS'), 
       dbhost=os.getenv('DBHOST'),
       dbname=os.getenv('DBNAME')
   )
   DEBUG = True

class UatConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
       dbuser=os.getenv('DBUSER'),
       dbpass=os.getenv('DBPASS'),
       dbhost=os.getenv('DBHOST'), 
       dbname=os.getenv('DBNAME')
   )
   DEBUG = True
