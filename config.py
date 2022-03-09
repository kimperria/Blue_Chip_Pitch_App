import os


class Config(object):
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False #configuration to disable auto updates to database

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')