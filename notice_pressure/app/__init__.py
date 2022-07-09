from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, NOT_FOUND
from dotenv import load_dotenv
import os
from flask import (Flask)
from app.presentation.shared.exceptionhandler.notfoundexception import NotFoundException
from app.presentation.shared.exceptionhandler.badrequestexception import BadRequestException
from app.presentation.shared.exceptionhandler.internalservererrorexception import InternalServerErrorException

def create_app():
    
    load_dotenv()
    app = Flask(__name__, instance_relative_config=True)
    
    if os.getenv("FLASK_CONFIG"):
        app.config.from_envvar('FLASK_CONFIG')
    
    # エンドポイント設定
    #app.register_blueprint(UserView.user, url_prefix='/api/v1/users/')
    
    # エラーハンドリング設定
    app.register_error_handler(NOT_FOUND, NotFoundException.response)
    app.register_error_handler(BAD_REQUEST, BadRequestException.response)
    app.register_error_handler(INTERNAL_SERVER_ERROR, InternalServerErrorException.response)
    return app 


app = create_app()
