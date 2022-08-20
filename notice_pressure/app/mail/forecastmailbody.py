from datetime import datetime, timedelta
from typing import List


class ForecastMailBody:
    def __init__(self, daily_forecast: List[dict]) -> None:
        """インスタンスを生成する。
           本文全体の生成はここでは行わない

        Args:
            daily_forecast (List[dict]): _description_
        """
        self.__headline: str = self._set_headline()
        self.__forecast_content: str = self._set_main(daily_forecast)

    @property
    def headline(self) -> str:
        """インスタンス変数を隠蔽する。

        Returns:
            str: _description_
        """
        return self.__headline

    @property
    def forecast_content(self) -> str:
        """インスタンス変数を隠蔽する。

        Returns:
            str: _description_
        """
        return self.__forecast_content

    def compose(self) -> str:
        """見出しとメインコンテンツからメール本文を生成する。
           メール本文の例:

           08/15 (Mon) の気圧予想です。

           06:00: 1000hPa(2)
           09:00: 999hPa(-1)
           ⋮
        Returns:
            str: _description_
        """
        return self.headline + "\n\n" + self.forecast_content

    @staticmethod
    def _set_headline() -> str:
        """本文の見出しを作る

        Returns:
            str: _description_
        """
        tomorrow: datetime = datetime.now() + timedelta(days=1)
        tommorow_str: str = tomorrow.strftime("%m/%d (%a)")

        headline: str = f"{tommorow_str} の気圧予想です。"
        return headline

    @staticmethod
    def _set_main(daily_forecast: List[dict]) -> str:
        """本文のメインコンテンツを作る

        Args:
            daily_forecast (List[dict]):

        Returns:
            str: _description_
        """
        forecast: str = ""
        forecast = "\n".join(
            [
                f'{element["datetime"]}: {element["pressure"]}hPa({element["difference"]})'
                for element in daily_forecast
            ]
        )
        return forecast
