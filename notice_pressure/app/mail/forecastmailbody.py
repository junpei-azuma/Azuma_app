from datetime import datetime, timedelta
from typing import List


class ForecastMailBody:
    def __init__(self, daily_forecast: List[dict]) -> None:
        self.__headline: str = self._set_headline()
        self.__forecast_content: str
        self.__body: str

    @staticmethod
    def _set_headline() -> str:
        tomorrow: datetime = datetime.now() + timedelta(days=1)
        tommorow_str: str = tomorrow.strftime("%m/%d (%a)")

        headline: str = f"{tommorow_str} の気圧予想です。"
        return headline

    @staticmethod
    def _set_main(daily_forecast: List[dict]) -> str:
        forecast: str = ""
        forecast = "\n".join(
            [
                f'{element["date"]}: {element["pressure"]}hPa({element["difference"]})'
                for element in daily_forecast
            ]
        )
        return forecast
