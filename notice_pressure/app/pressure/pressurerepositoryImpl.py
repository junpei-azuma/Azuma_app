from http.client import OK
import os
from typing import Final

from requests import Response
import requests
from .pressurerepository import PressureRepository


class PressureRepositoryImpl(PressureRepository):
    def __init__(self) -> None:
        self.__api_token: Final[str] = str(os.getenv("OPEN_WEATHER_API_TOKEN"))
        self.__latitude: Final[float] = 34.693741
        self.__longitude: Final[float] = 135.502182

    @property
    def api_token(self) -> str:
        return self.__api_token

    @property
    def latitude(self) -> float:
        return self.__latitude

    @property
    def longitude(self) -> float:
        return self.__longitude

    def get_tomorrow_list(self) -> list:
        response: Response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_token}&lang=ja&exclude=minutely,daily,current,alerts"
        )
        if self.request_fail(response):
            raise RuntimeError("気圧情報の取得に失敗しました。")

    @staticmethod
    def request_fail(response: Response) -> bool:
        """外部API呼び出しが失敗したか判定する

        Args:
            response (Response): レスポンスオブジェクト

        Returns:
            bool: 真偽値
        """
        return response.status_code != OK
