from flask_mail import Mail

# Flask-Mailのインスタンスを初期化する
mail = Mail()


def init_mail(app):
    """Mailインスタンスをセットアップする。
      このメソッドはアプリケーションオブジェクトの初期化時にのみ呼び出されます。

    Args:
        app (_type_): _description_
    """
    mail.init_app(app)
