from flask import Flask
import os


def create_app():
    application = Flask(__name__)
    application.secret_key = os.urandom(24)
    
    from .views import views
    
    application.register_blueprint(views, url_prefix='/')
           
    return application
    