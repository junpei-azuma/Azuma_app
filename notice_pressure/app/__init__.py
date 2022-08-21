from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, NOT_FOUND
import logging.config
from dotenv import load_dotenv
import os
from flask import Flask
from .presentation.forecast.forecastview import ForecastView
from .presentation.mail.mailview import MailView
from .configration.logging.dictconfig import LOGGING_CONFIG
from .mail.config import init_mail
from flask_mail import Mail

# from app.presentation.shared.exceptionhandler.notfoundexception import NotFoundException
# from app.presentation.shared.exceptionhandler.badrequestexception import (
#     BadRequestException,
# )
from .presentation.shared.exceptionhandler.internalservererrorhandler import (
    InternalServerErrorHandler,
)


def create_app():

    load_dotenv()
    app = Flask(__name__)

    app.config.from_pyfile("configration/config.py")

    if os.getenv("FLASK_ENV") == "dev":
        # ログ設定
        logging.config.dictConfig(LOGGING_CONFIG)

    app.config["JSON_AS_ASCII"] = os.environ.get("JSON_AS_ASCII")

    # エンドポイント設定
    app.register_blueprint(ForecastView.forecast_route, url_prefix="/api/v1/forecast/")
    app.register_blueprint(MailView.mail_route, url_prefix="/api/v1/mail/")

    # エラーハンドリング設定
    # app.register_error_handler(NOT_FOUND, NotFoundException.response)
    # app.register_error_handler(BAD_REQUEST, BadRequestException.response)
    app.register_error_handler(INTERNAL_SERVER_ERROR, InternalServerErrorHandler.handle)

    # メール設定
    init_mail(app)

    return app


app = create_app()
