from typing import Final

from injector import Injector
from app.pressure import PressureRepository, PressureRepositoryImpl


class Dependency:
    def __init__(self) -> None:
        self.injector: Final = Injector(self.__class__.config)

    @classmethod
    def config(cls, binder):
        binder.bind(PressureRepository, PressureRepositoryImpl)

    def resolve(self, cls):
        return self.injector.get(cls)
