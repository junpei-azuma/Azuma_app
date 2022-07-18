import copy
from typing import Final, List
from .pressure import Pressure


class DailyPressure:
    def __init__(self, daily_pressure: List[Pressure] = list()) -> None:
        """配列を初期化(引数無しの場合、空の配列で初期化)

        Args:
            daily_pressure (List[Pressure], optional): _description_. Defaults to list().
        """
        self.__pressurelist: Final[List[Pressure]] = daily_pressure

    @property
    def pressurelist(self) -> List[Pressure]:
        """インスタンスを隠蔽する

        Returns:
            List[Pressure]: _description_
        """
        return self.__pressurelist

    def add(self, pressure: Pressure) -> "DailyPressure":
        """リストにPressureインスタンスを追加する。
           リストの不変性を担保するために新しいインスタンスを生成して返す

        Args:
            pressure (Pressure): 気圧情報

        Returns:
            DailyPressure: 新規リスト
        """
        added_list: List[Pressure] = copy.deepcopy(self.pressurelist)
        added_list.append(pressure)
        return DailyPressure(added_list)
