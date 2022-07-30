from datetime import datetime
from http.client import (
    BAD_REQUEST,
    FORBIDDEN,
    INTERNAL_SERVER_ERROR,
    NOT_FOUND,
    UNAUTHORIZED,
)
import os
from typing import Final, List
import json

from requests import Response
import requests

from .converer import Converter
from ..pressurerepository import PressureRepository
from app.pressure import Pressure


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

    def call_openweather_api(self) -> Response:
        response: Response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?lat={self.latitude}&lon={self.longitude}&appid={self.api_token}&lang=ja&exclude=minutely,daily,current,alerts"
        )
        return response

    def get_daily_pressure(self) -> List[Pressure]:

        response: Response = self.call_openweather_api()

        if response.status_code == NOT_FOUND:
            raise RuntimeError("リクエスト先URLが存在しません。")

        if response.status_code == BAD_REQUEST:
            raise RuntimeError("パラメータが不正です。")

        if response.status_code == FORBIDDEN:
            raise RuntimeError("認証に失敗しました。")

        if response.status_code == UNAUTHORIZED:
            raise RuntimeError("認証情報が不正です。")

        if response.status_code == INTERNAL_SERVER_ERROR:
            raise RuntimeError("OpenWeatherAPIの不具合です。")

        response_object: dict = json.loads(response.text)

        extracted_list: Final[List] = Converter.extract(response_object)
        timeconveted_list: Final[List] = Converter.convert_unixtime(extracted_list)
        filterd_by_datetime_list: Final[List] = Converter.filter_by_datetime(
            timeconveted_list
        )
        filterd_by_time_list: Final[List] = Converter.filter_by_time(
            filterd_by_datetime_list
        )

        daily_pressure: List[Pressure] = [
            Pressure(
                datetime.strptime(element["dt"], "%Y%m%d%H%M"), element["pressure"]
            )
            for element in filterd_by_time_list
        ]

        return daily_pressure
