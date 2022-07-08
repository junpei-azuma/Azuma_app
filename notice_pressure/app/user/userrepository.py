from typing import Union
from app.user.domain.Iuserrepository import IuserRepository
from app.configration.database.initdb import db
from app.user.domain.user import User
from app.user.valueobject.email import Email
from app.user.userdto import UserDto

class UserRepository(IuserRepository):
    
    def __init__(self) -> None:
        self.session = db.session
    
    def add(self, user: User) -> None:
        """ユーザ追加

        Args:
            user (User): Userエンティティ
        """        
        userdto: UserDto = UserDto.from_entity(user)
        self.session.add(userdto)
    
    def find_by_email(self, email: Email) -> Union[User, None]:
        """メールアドレスでユーザを検索

        Args:
            email (Email): Emailエンティティ

        Returns:
            Union[User, None]: UserエンティティまたはNone
        """        
        email_str: str = email.value
        userdto: UserDto = self.session.query(UserDto).filter(UserDto.email == email_str).one_or_none()
        
        if not userdto:
            return None
        
        user: User = userdto.to_entity()
        return user