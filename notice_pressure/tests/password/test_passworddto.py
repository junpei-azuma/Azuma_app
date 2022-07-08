from app.password.password import Password
from app.password.passworddto import PasswordDto
from app.user.domain.user import User
from app.user.domain.userfactory import UserFactory
from app.user.valueobject.email import Email

def test_PasswordエンティティからDTOに変換():
    # 事前条件：パスワードインスタンス生成
    user: User = UserFactory.create(Email("hoge@example.com"))
    password: Password = Password(user.id, "Hogehoge_12")
    
    # 操作： パスワードインスタンスをDTOに変換
    passworddto: PasswordDto = PasswordDto.from_entity(password)
    
    # 想定結果： 正常に変換されている
    assert isinstance(passworddto, PasswordDto)
    
    assert password.user_id.value == passworddto.user_id
    assert password.value == passworddto.value