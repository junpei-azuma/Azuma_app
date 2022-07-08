from werkzeug.security import check_password_hash
from app.user.domain.user import User
from app.password.password import Password
from tests.util.factory import create_user
from app.password.passworddto import PasswordDto
from app.password.convertpassword import ConvertPassword

def test_Passwordをハッシュ化_正常系():
    # 事前準備： パスワードDTOを生成
    user: User = create_user()
    password: Password = Password(user.id, "Hogehoge_12")
    passworddto: PasswordDto = PasswordDto.from_entity(password)
    
    # 操作： パスワードをハッシュ化
    hashed_passworddto: PasswordDto = ConvertPassword.hash(passworddto)
    
    # 想定結果：ハッシュ値が一致
    assert check_password_hash(hashed_passworddto.value , passworddto.value)
    