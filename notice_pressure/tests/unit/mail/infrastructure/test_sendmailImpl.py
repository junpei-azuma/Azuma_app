from typing import List
from app.mail import ForecastMailBody, SendMail, SendMailImpl
from app.mail.config import mail
from flask_mail import Mail


def test_メール送信():
    # 事前準備： メール本文インスタンスを生成する。
    daily_forecast: List[dict] = [
        {"date": "06:00", "pressure": "1000", "difference": "1"},
        {"date": "09:00", "pressure": "1003", "difference": "3"},
        {"date": "12:00", "pressure": "1002", "difference": "-1"},
    ]
    forecastmailbody: ForecastMailBody = ForecastMailBody(daily_forecast)
    body: str = forecastmailbody.compose()
    # 操作： メールを送信する。
    sendmailImpl: SendMail = SendMailImpl()

    with mail.record_messages() as outbox:
        sendmailImpl.send(body)

    # outboxにメールが1通届いている
    assert len(outbox) == 1
