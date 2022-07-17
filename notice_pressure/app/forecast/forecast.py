from datetime import datetime
from typing import Final
from app.pressure import Pressure, PressureChange


class Forecast:
    def __init__(
        self,
        target_datetime: datetime,
        pressure: Pressure,
        pressure_change: PressureChange,
    ) -> None:
        self.__target_datetime: Final[datetime] = target_datetime
        self.__pressure: Final[Pressure] = pressure
        self.__pressure_change: Final[PressureChange] = pressure_change

    @property
    def target_datetime(self) -> datetime:
        return self.__target_datetime

    @property
    def pressure(self) -> Pressure:
        return self.__pressure

    @property
    def pressure_change(self) -> PressureChange:
        return self.__pressure_change
