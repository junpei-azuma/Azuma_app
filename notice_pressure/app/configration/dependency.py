from typing import Final

from injector import Injector
from app.pressure import PressureRepository, PressureRepositoryImpl
from app.mail import SendMail, SendMailImpl


class Dependency:
    def __init__(self) -> None:
        self.injector: Final = Injector(self.__class__.config)

    @classmethod
    def config(cls, binder):
        binder.bind(PressureRepository, PressureRepositoryImpl)
        binder.bind(SendMail, SendMailImpl)

    def resolve(self, cls):
        return self.injector.get(cls)
