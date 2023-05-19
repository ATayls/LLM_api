import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CHATGPT_API_URL = os.environ.get('CHATGPT_API_URL')