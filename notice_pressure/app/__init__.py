from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, NOT_FOUND
import logging.config
from dotenv import load_dotenv
import os
from flask import Flask
from app.presentation.forecast.forecastview import ForecastView
from app.configration.logging.dictconfig import LOGGING_CONFIG

# from app.presentation.shared.exceptionhandler.notfoundexception import NotFoundException
# from app.presentation.shared.exceptionhandler.badrequestexception import (
#     BadRequestException,
# )
from app.presentation.shared.exceptionhandler.internalservererrorhandler import (
    InternalServerErrorHandler,
)


def create_app():

    load_dotenv()
    app = Flask(__name__)

    if os.getenv("FLASK_CONFIG"):
        app.config.from_envvar("FLASK_CONFIG")

    if os.getenv("FLASK_ENV") == "dev":
        # ログ設定
        logging.config.dictConfig(LOGGING_CONFIG)

    app.config["JSON_AS_ASCII"] = os.environ.get("JSON_AS_ASCII")
    # エンドポイント設定
    app.register_blueprint(ForecastView.forecast_route, url_prefix="/api/v1/forecast/")

    # エラーハンドリング設定
    # app.register_error_handler(NOT_FOUND, NotFoundException.response)
    # app.register_error_handler(BAD_REQUEST, BadRequestException.response)
    app.register_error_handler(INTERNAL_SERVER_ERROR, InternalServerErrorHandler.handle)

    return app


app = create_app()
