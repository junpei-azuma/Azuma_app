from unittest import mock
import pytest
from sqlalchemy.exc import SQLAlchemyError
from app.configration.dependency import Dependency
from app.user.usecase.createuser import CreateUser

def test_DIコンテナ経由でインスタンス生成_正常系():
    # 事前準備： なし
    
    # 操作： DIコンテナでユースケースのインスタンス生成
    dependency = Dependency()
    createuser: CreateUser = dependency.resolve(CreateUser)
    
    # 想定結果：正しくインスタンスが生成されている
    assert isinstance(createuser, CreateUser)
    
    assert hasattr(createuser, 'iuserrepository')
    assert hasattr(createuser, 'ipasswordrepository')
    assert hasattr(createuser, 'validateuser')


def test_User追加_正常系(mocker):
    # 事前準備1： モック生成
    user_add_mock = mock.Mock()
    password_add_mock = mock.Mock()
    
    # 事前準備2: インスタンス生成
    dependency = Dependency()
    createuser: CreateUser = dependency.resolve(CreateUser)
    
    mocker.patch.object(createuser.validateuser, 'email_duplicate' ,return_value=False)
    mocker.patch.object(createuser.iuserrepository, 'add' , side_effect=user_add_mock)
    mocker.patch.object(createuser.ipasswordrepository, 'add' , side_effect=password_add_mock)
       
    # 操作： テスト対象メソッド呼び出し
    param_dict: dict = {"email" : "hoge@exmaple.com" , "password" : "Hogehoge_12"}
    createuser.create_user(param_dict)
    
    # 想定結果： リポジトリのメソッドが正しく呼び出されている
    user_add_mock.assert_called_once()
    password_add_mock.assert_called_once()

def test_メールアドレスが重複している場合例外発生(mocker):
    # 事前準備1： モック生成
    user_add_mock = mock.Mock()
    password_add_mock = mock.Mock()
    
    # 事前準備2: インスタンス生成
    dependency = Dependency()
    createuser: CreateUser = dependency.resolve(CreateUser)
    
    mocker.patch.object(createuser.validateuser, 'email_duplicate' ,return_value=True)
    mocker.patch.object(createuser.iuserrepository, 'add' , side_effect=user_add_mock)
    mocker.patch.object(createuser.ipasswordrepository, 'add' , side_effect=password_add_mock)
       
    # 操作： テスト対象メソッド呼び出し
    param_dict: dict = {"email" : "hoge@exmaple.com" , "password" : "Hogehoge_12"}
    
    with pytest.raises(ValueError) as e:
        createuser.create_user(param_dict)
        
    assert str(e.value) == "メールアドレスが重複しています。"


def test_User登録後トランザクション内でDBエラー発生(mocker):
    # 事前準備1： モック生成
    user_add_mock = mock.Mock()
    password_add_mock = mock.Mock()
    
    # 事前準備2: インスタンス生成
    dependency = Dependency()
    createuser: CreateUser = dependency.resolve(CreateUser)
    
    mocker.patch.object(createuser.validateuser, 'email_duplicate' ,return_value=False)
    mocker.patch.object(createuser.iuserrepository, 'add' , side_effect=user_add_mock)
    mocker.patch.object(createuser.ipasswordrepository, 'add' , side_effect=SQLAlchemyError)
       
    # 操作： テスト対象メソッド呼び出し
    param: dict = {"email" : "hoge@exmaple.com" , "password" : "Hogehoge_12"}
    
    with pytest.raises(SQLAlchemyError) as e:
        createuser.create_user(param)
    
    # 想定結果：例外が発生し、後続の処理が実行されないこと
    assert str(e.value) == "ユーザ登録中にエラーが発生しました。"
    password_add_mock.assert_not_called()
    
def test_User登録中にトランザクション内でDBエラー発生(mocker):
    # 事前準備1： モック生成
    user_add_mock = mock.Mock()
    password_add_mock = mock.Mock()
    
    # 事前準備2: インスタンス生成
    dependency = Dependency()
    createuser: CreateUser = dependency.resolve(CreateUser)
    
    mocker.patch.object(createuser.validateuser, 'email_duplicate' ,return_value=False)
    mocker.patch.object(createuser.iuserrepository, 'add' , side_effect=SQLAlchemyError)
    mocker.patch.object(createuser.ipasswordrepository, 'add' , side_effect=password_add_mock)
       
    # 操作： テスト対象メソッド呼び出し
    param: dict = {"email" : "hoge@exmaple.com" , "password" : "Hogehoge_12"}
    
    with pytest.raises(SQLAlchemyError) as e:
        createuser.create_user(param)
    
    # 想定結果： 例外が発生し、後続の処理が呼ばれないこと
    assert str(e.value) == "ユーザ登録中にエラーが発生しました。"
    password_add_mock.assert_not_called()