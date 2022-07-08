from app.user.domain.user import User
from tests.util.factory import create_user

def test_Userインスタンス生成_正常系():
    # 事前条件： なし
    
    # 操作： Userインスタンスを生成
    user: User = create_user()
    
    # 想定結果： Userインスタンスが正しく生成されている
    
    assert isinstance(user, User)
    
    assert user.email.value == "hoge@example.com"
    assert user.is_active == False
    assert user.is_deleted == False

def test_Userを有効化_正常系():
    
    # 事前条件： Userインスタンスを生成
    user: User = create_user()
    
    # 操作： 有効化
    activated_user: User = user.activate()
    
    # 想定結果： 1. IDが一致する
    assert user.id == activated_user.id
    
    # 想定結果: 2. 有効化されている
    assert activated_user.is_active
    
def test_Userを論理削除_正常系():
    
    # 事前条件： Userインスタンスを生成
    user: User = create_user()
    
    # 操作： 削除フラグを立てる
    deleted_user: User = user.delete()
    
    # 想定結果： 1. IDが一致する
    assert user.id == deleted_user.id

    # 想定結果： 2. 削除フラグが立っている
    assert deleted_user.is_deleted