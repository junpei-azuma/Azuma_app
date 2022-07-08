from app.user.valueobject.userid import UserId
from typing import Final
from werkzeug.security import check_password_hash

class HashedPassword():
    """ハッシュ化されたパスワード
       DBからパスワードを取得する時のみ使う
    """    
    def __init__(self, user_id: UserId, value: str) -> None:
        """インスタンス初期化

        Args:
            user_id (UserId): UserのID
            value (str): ハッシュ化された値
        """        
        self.__user_id: Final[UserId] = user_id
        self.__value: Final[str] = value
    
    @property
    def user_id(self) -> UserId:
        """ユーザIDの値

        Returns:
            UserId: UserID
        """        
        return self.__user_id
    
    @property
    def value(self) -> str:
        """パスワードのハッシュ値

        Returns:
            str: ハッシュ値
        """        
        return self.__value
    
    def check(self, input_value: str) -> bool:
        """入力された値とパスワードのハッシュ値を比較

        Args:
            input_value (str): ユーザの入力値

        Returns:
            bool: 真偽値
        """        
        return check_password_hash(self.value , input_value)
    