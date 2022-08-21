from app.mail import SendMail

from app.mail.config import mail
from flask_mail import Message, Mail


class SendMailImpl(SendMail):
    """メール送信インタフェースの実装クラス
       Flask-Mailを利用する。

    Args:
        SendMail (_type_): _description_
    """

    def __init__(self) -> None:
        self.__message: Message = Message()

    @property
    def message(self) -> Message:
        return self.__message

    def send(self, forecastmailbody: str) -> None:
        """メールを送信する。

        Args:
            forecastmailbody (ForecastMailBody): _description_
        """
        self.message.add_recipient("azumanotdetail@gmail.com")
        self.message.body = forecastmailbody
        self.message.subject = "明日の気圧予想"
        mail.send(self.message)
