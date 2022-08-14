from datetime import datetime, timedelta
from typing import List


class ForecastMailBody:
    def __init__(self, daily_forecast: List[dict]) -> None:
        self.__headline: str = self.set_headline()
        self.__body: str

    @staticmethod
    def set_headline() -> str:
        tomorrow: datetime = datetime.now() + timedelta(days=1)
        tommorow_str: str = tomorrow.strftime("%m/%d (%a)")

        headline: str = f"{tommorow_str} の気圧予想です。"
        return headline
