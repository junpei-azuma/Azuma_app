from abc import ABCMeta, abstractmethod


class PressureRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_daily_pressure():
        pass
