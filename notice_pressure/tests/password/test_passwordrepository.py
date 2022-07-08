from typing import Union
from app.password.hashedpassword import HashedPassword
from app.password.password import Password
from app.user.domain.user import User
from app.user.domain.userfactory import UserFactory 
from app.user.domain.Iuserrepository import IuserRepository
from app.user.userrepository import UserRepository
from app.password.Ipasswordrepository import IpassWordRepository
from app.password.passwordrepository import PasswordRepository
from app.user.valueobject.email import Email

def test_パスワードエンティティ追加処理():
    # 事前準備： ユーザエンティティを追加
    user: User = UserFactory.create(Email("hoge@example.com"))
    userrepository: IuserRepository = UserRepository()
    userrepository.add(user)
    userrepository.session.commit()
    
    # 操作： パスワードエンティティを追加
    passwordrepository: IpassWordRepository = PasswordRepository()
    password: Password = Password(user.id, "Hogehoge_12")
    passwordrepository.add(password)
    passwordrepository.session.commit()
    
    # 想定結果： パスワードが追加されている
    added_password: Union[HashedPassword, None] = passwordrepository.find_by_user_id(user.id)
    assert isinstance(added_password , HashedPassword)
    assert added_password.check("Hogehoge_12")
    