from logging import debug
from ulid import ULID
from tests.util.factory import create_user
from app.user.domain.user import User
from app.user.userdto import UserDto

def test_初期化したUserエンティティからDTOに変換():
    # 事前条件：Userインスタンス生成
    user: User = create_user()
    
    # 操作： DTOに変換
    userdto: UserDto = UserDto.from_entity(user)
    # 想定結果： 正常に変換されている
    assert isinstance(userdto, UserDto)

    assert user.id.value == userdto.id
    assert user.email.value == userdto.email
    assert user.is_active == userdto.is_active
    assert user.is_deleted == userdto.is_deleted