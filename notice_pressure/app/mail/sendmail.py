from abc import abstractclassmethod, ABCMeta


class SendMail(metaclass=ABCMeta):
    """メール送信ユースケースのインタフェース
       テストでは実際に送信せずに標準出力に出力したいため抽象化する
    Args:
        metaclass (_type_, optional): _description_. Defaults to ABCMeta.
    """

    @abstractclassmethod
    def send() -> None:
        pass
