from app.mail import SendMail


class SendMailImpl(SendMail):
    """メール送信インタフェースの実装クラス
       Flask-Mailを利用する。

    Args:
        SendMail (_type_): _description_
    """

    def __init__(self) -> None:
        pass

    def send(self) -> None:
        pass
