from injector import inject
from typing import Final, Union
from app.user.domain.Iuserrepository import IuserRepository
from app.user.domain.user import User
from app.user.valueobject.email import Email

class ValidateUser():
    
    @inject
    def __init__(self, iuserrepository: IuserRepository) -> None:
        """インスタンス初期化

        Args:
            iuserrepository (IuserRepository): userrepositoryのインターフェース
        """        
        self.iuserrepository: Final[IuserRepository] = iuserrepository
    
    
    def email_duplicate(self, email: Email) -> bool:
        """Userのメールアドレスが重複するか判定

        Args:
            email (Email): Emailインスタンス

        Returns:
            bool: メールアドレスが重複するか判定
        """        
        user: Union[User, None] = self.iuserrepository.find_by_email(email)
        
        return isinstance(user, User)