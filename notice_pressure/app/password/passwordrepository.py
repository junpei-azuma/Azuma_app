from typing import Union
from app.password.Ipasswordrepository import IpassWordRepository
from app.configration.database.initdb import db
from app.password.hashedpassword import HashedPassword
from app.password.password import Password
from app.password.passworddto import PasswordDto
from app.password.convertpassword import ConvertPassword
from app.user.userdto import UserDto
from app.user.valueobject.userid import UserId

class PasswordRepository(IpassWordRepository):
    """パスワード集約のリポジトリ実装クラス

    Args:
        IpassWordRepository (_type_): リポジトリのインターフェース
    """    
    def __init__(self) -> None:
        """インスタンス初期化
        """        
        self.session = db.session
        
    # パスワードのハッシュ化はインフラ層のConvertPasswordクラスの責務とする
    # ※ ハッシュ化はドメイン知識の範疇からは外れるため
    def add(self, password: Password) -> None:
        """パスワードを追加

        Args:
            password (Password): パスワードエンティティ
        """     
        passworddto: PasswordDto = PasswordDto.from_entity(password)
        hashed_passworddto: PasswordDto = ConvertPassword.hash(passworddto)
        self.session.add(hashed_passworddto)
    
    def find_by_user_id(self, id: UserId) -> Union[HashedPassword, None]:
        """ユーザIDでパスワードを検索

        Args:
            id (UserId): ユーザID

        Returns:
            Union[Password, None]: パスワードエンティティ / None
        """        
        id_str: str = id.value
        passworddto: PasswordDto = self.session.query(PasswordDto).filter(PasswordDto.user_id == id_str).one_or_none()
        
        if passworddto is None:
            return passworddto
        
        hashed_password: HashedPassword = passworddto.to_hashed_entity()
        return hashed_password
        
        