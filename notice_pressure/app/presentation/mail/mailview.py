from http.client import INTERNAL_SERVER_ERROR, OK
import logging
from flask import Blueprint, abort, jsonify

from ...configration.dependency import Dependency
from app.mail import SendMail, SendForecastMail


class MailView:
    mail_route = Blueprint("mail", __name__, url_prefix="/mail")

    @mail_route.route("/", methods=["POST"])
    def send():
        logger = logging.getLogger(__name__)
        try:
            dependency: Dependency = Dependency()
            sendforecastmail: SendForecastMail = dependency.resolve(SendForecastMail)
            sendforecastmail.send()
        except Exception as e:
            logger.error(e)
            abort(INTERNAL_SERVER_ERROR, e)

        return jsonify({"code": OK, "message": "メールを送信しました。"})
