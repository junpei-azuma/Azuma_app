from ulid import ULID
from app.password.password import Password
from app.user.domain.userfactory import UserFactory
from app.user.domain.user import User
from app.user.valueobject.email import Email
from app.user.valueobject.userid import UserId
 
def create_userid() -> UserId:
    """ ユーザIDインスタンスを生成する

    Returns:
        UserId: _description_
    """    
    id: str = str(ULID())
    userid = UserId(id)
    return userid
    
def create_email() -> Email:
    """Emailインスタンスを生成する

    Returns:
        Email: _description_
    """    
    email = Email("hoge@example.com")
    return email


def create_user() -> User:
    """ ユーザインスタンスを生成する

    Returns:
        User: _description_
    """    
    email = create_email()
    user: User = UserFactory.create(email)
    return user