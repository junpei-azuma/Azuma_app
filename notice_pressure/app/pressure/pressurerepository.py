from abc import ABCMeta, abstractmethod


class PressureRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_tomorrow_list():
        pass
