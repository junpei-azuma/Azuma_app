from datetime import datetime, timedelta
import time
from typing import Final
from .pressure import Pressure


class PressureChange:
    def __init__(
        self, current_pressure: Pressure, pressure_3hour_ago: Pressure
    ) -> None:
        """インスタンスを初期化する

        Args:
            current_pressure (Pressure): 現在日時の気圧
            pressure_3hour_ago (Pressure): 3時間前の気圧

        Raises:
            ValueError: 現在日時と過去日時の差分(hour)が2:00未満 3:59を超過している
        """
        # current_pressureはpressure_3hour_agoの2~3時間前である必要がある。
        if not self.validate_datetime_difference(current_pressure, pressure_3hour_ago):
            raise ValueError("不正な日時です。")

        self.__current_pressure: Final[Pressure] = current_pressure
        self.__pressure_3hour_ago: Final[Pressure] = pressure_3hour_ago

    @property
    def current_pressure(self) -> Pressure:
        """メンバ変数を隠蔽

        Returns:
            Pressure: 現在日時の気圧
        """
        return self.__current_pressure

    @property
    def pressure_3hour_ago(self) -> Pressure:
        """メンバ変数を隠蔽

        Returns:
            Pressure: 過去日時の気圧
        """
        return self.__pressure_3hour_ago

    def calculate(self) -> int:
        """現在日時と3時間前の気圧変化を計算する

        Returns:
            int: 気圧の変化量
        """
        return self.current_pressure.value - self.pressure_3hour_ago.value

    @classmethod
    def validate_datetime_difference(
        cls, current_pressure: Pressure, pressure_3hour_ago: Pressure
    ) -> bool:
        __MIN_INTERVAL: Final[int] = 2
        __MAX_INTERVAL: Final[int] = 3

        current_datetime: Final[datetime] = current_pressure.datetime
        datetime_3hours_ago: Final[datetime] = pressure_3hour_ago.datetime

        time_difference: Final[timedelta] = current_datetime - datetime_3hours_ago
        time_difference_hour: Final[int] = time_difference.seconds // 3600

        return (
            time_difference_hour == __MAX_INTERVAL
            or time_difference_hour == __MIN_INTERVAL
        )
