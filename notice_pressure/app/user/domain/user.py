from typing import Final
from app.user.valueobject.userid import UserId
from app.user.valueobject.email import Email

class User():
    """システム利用者のエンティティ
    """    
    def __init__(self, id: UserId, email: Email, is_active: bool = False, is_deleted: bool = False) -> None:
        """インスタンスを初期化

        Args:
            id (UserId): 識別子
            email (Email): メールアドレス
            is_active (bool): 有効化フラグ(デフォルトはFalse)
            is_deleted (bool): 削除フラグ(デフォルトはFalse)
        """        
        self.__id: Final[UserId] = id
        self.__email: Final[Email] = email
        self.__is_active: Final[bool] = is_active
        self.__is_deleted: Final[bool] = is_deleted
    
    ## 外部から値を変更できないようにする。 参照は可能
    @property
    def id(self) -> UserId:
        """idを隠蔽

        Returns:
            UserId: userId
        """        
        return self.__id
    
    @property
    def email(self) -> Email:
        """Emailを隠蔽

        Returns:
            Email: Email
        """        
        return self.__email
    
    @property
    def is_active(self) -> bool:
        """有効化フラグを隠蔽

        Returns:
            bool:有効化フラグ
        """        
        return self.__is_active
    
    @property
    def is_deleted(self) -> bool:
        """削除フラグを隠蔽

        Returns:
            bool: 削除フラグ
        """        
        return self.__is_deleted
    
    
    def activate(self) -> 'User':
        """ユーザを有効化する

        Returns:
            User: 有効化されたユーザインスタンス
        """        
        activated_user: User = User(self.id, self.email, True)
        return activated_user
    
    def delete(self) -> 'User':
        """ユーザを論理削除する

        Returns:
            User: 削除フラグの立ったユーザ
        """        
        deleted_user: User = User(self.id, self.email, self.is_active, True)
        return deleted_user