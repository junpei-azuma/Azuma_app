from abc import ABCMeta, abstractmethod
from typing import List
from app.pressure import Pressure


class PressureRepository(metaclass=ABCMeta):
    @abstractmethod
    def get_daily_pressure() -> List[Pressure]:
        pass
