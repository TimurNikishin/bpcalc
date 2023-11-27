from flask import Flask
from flask_wtf.csrf import CSRFProtect
import os


def create_app():
    application = Flask(__name__)
    application.secret_key = os.urandom(24)
    csrf = CSRFProtect()
    csrf.init_app(application)
    
    from .views import views
    
    application.register_blueprint(views, url_prefix='/')
           
    return application
    