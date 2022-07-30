from datetime import datetime
from typing import Final, Optional
from app.pressure import Pressure, PressureChange


class Forecast:
    def __init__(
        self,
        pressure: Pressure,
        pressure_change: PressureChange,
    ) -> None:
        """インスタンスを作成する

        Args:
            pressure (Pressure): 気圧情報
            pressure_change (Optional[PressureChange]): 3時間前からの変化(06:00分は3時間前のデータが存在しないためNone)
        """
        self.__pressure: Final[Pressure] = pressure
        self.__pressure_change: Final[PressureChange] = pressure_change

    @property
    def pressure(self) -> Pressure:
        return self.__pressure

    @property
    def pressure_change(self) -> PressureChange:
        return self.__pressure_change
