from typing import List
from app.mail import ForecastMailBody, SendMail, SendMailImpl
from app.mail.config import mail
from flask_mail import Mail
import pytest


@pytest.mark.freeze_time("2022-08-14")
def test_メール送信():
    # 事前準備： メール本文インスタンスを生成する。
    daily_forecast: List[dict] = [
        {"datetime": "06:00", "pressure": "1000", "difference": "1"},
        {"datetime": "09:00", "pressure": "1003", "difference": "3"},
        {"datetime": "12:00", "pressure": "1002", "difference": "-1"},
    ]
    forecastmailbody: ForecastMailBody = ForecastMailBody(daily_forecast)
    body: str = forecastmailbody.compose()
    # 操作： メールを送信する。
    sendmailImpl: SendMail = SendMailImpl()

    with mail.record_messages() as outbox:
        sendmailImpl.send(body)

    # outboxにメールが1通届いている
    assert len(outbox) == 1
    assert outbox[0].subject == "明日の気圧予想"
    assert (
        outbox[0].body
        == "08/15 (Mon) の気圧予想です。\n\n06:00: 1000hPa(1)\n09:00: 1003hPa(3)\n12:00: 1002hPa(-1)"
    )
