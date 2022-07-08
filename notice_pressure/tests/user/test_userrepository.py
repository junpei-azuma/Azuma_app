from audioop import add
from app.user.domain.user import User
from app.user.domain.Iuserrepository import IuserRepository
from app.user.userrepository import UserRepository
from tests.util.factory import create_user

def test_User追加_正常系():
    # 事前準備: Userインスタンス作成
    user: User = create_user()
    
    # 操作： ユーザ保存処理実行
    userrepository: IuserRepository = UserRepository()
    userrepository.add(user)
    userrepository.session.commit()
    
    # 想定結果： ユーザが追加されている
    added_user: User = userrepository.find_by_email(user.email)
    
    assert user.id.value == added_user.id.value
    assert user.email.value == added_user.email.value
    assert user.is_active == added_user.is_active
    assert user.is_deleted == added_user.is_deleted
    