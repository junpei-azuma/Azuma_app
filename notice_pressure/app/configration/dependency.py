from typing import Final

from injector import Injector
from app.user.domain.Iuserrepository import IuserRepository
from app.user.userrepository import UserRepository
from app.password.Ipasswordrepository import IpassWordRepository
from app.password.passwordrepository import PasswordRepository

class Dependency():
    def __init__(self) -> None:
        self.injector: Final = Injector(self.__class__.config)
        
    
    @classmethod
    def config(cls, binder):
        binder.bind(IuserRepository, UserRepository)
        binder.bind(IpassWordRepository, PasswordRepository)
            
            
        
    def resolve(self, cls):
        return self.injector.get(cls)