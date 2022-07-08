from app.user.valueobject.email import Email
from tests.util.factory import create_email
import pytest

def test_Emailインスタンス生成_正常系():
    # 事前準備： なし
    
    # 操作： インスタンス生成
    email = create_email()
    
    # 想定結果：1. インスタンスが正しく生成されている
    assert isinstance(email, Email)
    
    # 2. メールアドレスの値が正常
    assert isinstance(email.value , str)
    assert email.value == "hoge@example.com"

@pytest.mark.parametrize("invalid_email_value" , [None, ""])
def test_Emailが未入力の場合に例外発生(invalid_email_value: str):
    # 事前準備： なし
    
    # 操作： 不正な値でEmailインスタンスを生成
    with pytest.raises(ValueError) as e:
        email: Email = Email(invalid_email_value)
    
    assert str(e.value) == "メールアドレスを入力してください。"
    
@pytest.mark.parametrize("invalid_email_value" , [123456, 1.5, {"hoge": "fufa"}, list("fuga")])
def test_Emailの型が文字列以外の場合に例外発生(invalid_email_value):
    # 事前準備： なし
    
    # 操作： 不正な値でEmailインスタンス生成
    with pytest.raises(ValueError) as e:
        email: Email = Email(invalid_email_value)
    
    assert str(e.value) == "メールアドレスを正しく入力してください。"

@pytest.mark.parametrize("invalid_email_value", ["aaaaa" , "aaa@@gmail.com"])
def test_Emailの形式が不正な場合に例外発生(invalid_email_value):
    # 事前準備： なし
    
    # 操作： 不正な形式の値でEmailインスタンス生成
    with pytest.raises(ValueError) as e:
        email: Email = Email(invalid_email_value)
    
    assert str(e.value) == "メールアドレスが不正な形式です。"