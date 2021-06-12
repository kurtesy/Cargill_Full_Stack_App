import os
import json

config_path = os.path.dirname(__file__)
with open(os.path.join(config_path, 'configs.json')) as config_file:
    config_data = json.load(config_file)


class DevConfig(object):
    dev = config_data['dev']
    DEBUG = dev['DEBUG']
    DB_NAME = dev['DB_NAME']
    DB_USER = dev['DB_USER']
    DB_PASS = dev['DB_PASS']
    DB_SERVICE = dev['DB_SERVICE']
    DB_PORT = dev['DB_PORT']
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME
    )
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
