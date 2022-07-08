import pytest
from app.user.domain.user import User
from app.password.password import Password
from tests.util.factory import create_user

def test_Passwordインスタンス生成_正常系():
    # 事前条件： ユーザインスタンス生成
    user: User = create_user()
    
    # 操作： パスワードインスタンス生成
    password: Password = Password(user.id, "Hogehoge_10")
    
    # 想定結果： インスタンスが正しく生成できる
    assert isinstance(password , Password)
    
    assert password.value == "Hogehoge_10"
    assert user.id == password.user_id
    
def test_Passwordインスタンス生成_最小文字数未満で例外発生():
    # 事前条件： ユーザインスタンス生成
    user: User = create_user()
    
    # 操作： 9文字を渡してパスワードインスタンス生成
    with pytest.raises(ValueError) as e:
        password: Password = Password(user.id, "Hogehog_1")
    
    assert str(e.value) == "パスワードは10文字以上で入力してください。"

def test_Passwordインスタンス生成_最大文字数超過で例外発生():
    # 事前条件： ユーザインスタンス生成
    user: User = create_user()
    
    # 操作： 21文字を渡してパスワードインスタンス生成
    with pytest.raises(ValueError) as e:
        password: Password = Password(user.id, "Hogehoge_1shgapsoegp@")
    
    assert str(e.value) == "パスワードは20文字以下で入力してください。"

@pytest.mark.parametrize('invalid_password', [
    "hogehogehoge", # 1種類の文字を使用
    "HOGEHOGEHOGE",
    "12345678910",
    "_@-%&#+_@-%&#+",
    "Hogehogehoge", # 2種類の文字を使用
    "hogehoge12",
    "hogehoge@#_",
    "HOGEHOGE@+!",
    "HOGEHOGE123",
    "_@-%&#+123",
    "HOGEHOGE_1@", # 3種類の文字を使用
    "hogehoge_12@#",
    "Hogehoge_@#",
    "Hogehoge12"
    ])
def test_不正な形式のパスワードで例外発生(invalid_password):
    # 事前条件： ユーザインスタンス生成
    user: User = create_user()
    
    # 操作： 不正な形式の文字を渡してパスワードインスタンス生成
    with pytest.raises(ValueError) as e:
        password: Password = Password(user.id, invalid_password)
    
    assert str(e.value) == "パスワードの形式が不正です。"
    

def test_パスワードの値を変更():
    # 事前準備： パスワードインスタンスを生成する
    user: User = create_user()
    password: Password = Password(user.id, "Hogehoge_12")
    
    # 操作： changeメソッドを呼び出し
    changed_password: Password = password.change("Fugafuga_12")
    
    # 想定結果： 
    # 1. 値が正常に変更されている
    assert changed_password.value == "Fugafuga_12"
    # 2. 変更前の変更後のユーザIDが一致
    assert password.user_id == changed_password.user_id