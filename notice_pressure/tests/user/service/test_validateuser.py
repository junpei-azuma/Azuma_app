from unittest import mock
import pytest
from app.user.domain.Iuserrepository import IuserRepository
from app.user.service.validateuser import ValidateUser
from app.user.domain.user import User
from app.user.valueobject.email import Email
from tests.util.factory import create_email, create_user

def test_メールアドレスが重複する(mocker):
    #事前準備：リポジトリとuserインスタンスのモックを作成
    userrepository_mock: IuserRepository = mock.MagicMock()
    user: User = create_user()
    mocker.patch.object(userrepository_mock, 'find_by_email' , return_value=user)
    
    # 操作： テスト対象メソッドを実行
    email: Email = create_email()
    validateuser: ValidateUser = ValidateUser(userrepository_mock)
    
    # 想定結果： True
    assert validateuser.email_duplicate(email)


def test_メールアドレスが重複しない(mocker):
    #事前準備：リポジトリとuserインスタンスのモックを作成
    userrepository_mock: IuserRepository = mock.MagicMock()
    mocker.patch.object(userrepository_mock, 'find_by_email' , return_value=None)
    
    # 操作： テスト対象メソッドを実行
    email: Email = create_email()
    validateuser: ValidateUser = ValidateUser(userrepository_mock)
    
    # 想定結果： True
    assert not validateuser.email_duplicate(email)