from typing import Union
from abc import ABCMeta, abstractmethod
from app.user.domain.user import User
from app.user.valueobject.email import Email

class IuserRepository(metaclass=ABCMeta):
    """Userリポジトリのインターフェース

    Args:
        metaclass (_type_, optional): _description_. Defaults to ABCMeta.
    """    
    @abstractmethod
    def add(self, user: User) -> None:
        """user追加処理

        Args:
            user (User): Userクラスのインスタンス
        """        
        pass
    
    @abstractmethod
    def find_by_email(self, email: Email) -> Union[User, None]:
        """ユーザ検索処理

        Args:
            email (Email): Email
        """        
        pass