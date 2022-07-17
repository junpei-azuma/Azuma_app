from typing import Final, List
import copy
from .forecast import Forecast


class DailyForecast:
    def __init__(self, daily_forecast: List[Forecast] = list()) -> None:
        """配列を初期化(引数を渡さない場合、空の配列)"""
        self.__forecastlist: Final[List[Forecast]] = daily_forecast

    @property
    def forecastlist(self) -> List[Forecast]:
        """インスタンスを隠蔽する

        Returns:
            List[Forecast]: プロパティ
        """
        return self.__forecastlist

    def add(self, forecast: Forecast) -> "DailyForecast":
        """
        リストにForecastインスタンスを追加する。
        リストの不変性を担保するために新しいインスタンスを生成して返す
        Args:
            forecast (Forecast): 予報インスタンス

        Returns:
            DailyForecast: 新規リスト
        """
        added_list: List[Forecast] = copy.deepcopy(self.__forecastlist)
        added_list.append(forecast)
        return DailyForecast(added_list)
