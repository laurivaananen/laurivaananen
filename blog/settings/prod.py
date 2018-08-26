from blog.settings.base import *

DEBUG = False

STATIC_ROOT = "/static_files/"
STATIC_URL = "/static/"

SECRET_KEY = 'jdfs78f4uqisd78fhu2nvjkdsn84'

ALLOWED_HOSTS = [
    "127.0.0.1:8080/",
    "127.0.0.1",
    "localhost",
]

