

from abc import ABCMeta
from abc import ABCMeta, abstractmethod
from app.password.password import Password
from app.user.valueobject.userid import UserId

class IpassWordRepository(metaclass=ABCMeta):
    """Passwordリポジトリのインターフェース

    Args:
        metaclass (_type_, optional): _description_. Defaults to ABCMeta.
    """    
    @abstractmethod
    def add(self, password: Password) -> None:
        """パスワード追加処理

        Args:
            password (Password): パスワードエンティティ
        """        
        pass
    
    @abstractmethod
    def find_by_user_id(self, id: UserId) -> None:
        """ユーザIDでパスワードを検索

        Args:
            id (UserId): ユーザID
        """
        pass
    