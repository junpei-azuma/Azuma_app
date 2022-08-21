from http.client import OK
import json
from typing import List
from injector import inject
from .sendmail import SendMail
from .forecastmailbody import ForecastMailBody
from ..forecast import CreateDailyForecast, ForecastDto
import requests


class SendForecastMail:
    @inject
    def __init__(self, sendmail: SendMail, createdailyforecast: CreateDailyForecast):
        self.sendmail: SendMail = sendmail
        self.createdailyforecast: CreateDailyForecast = createdailyforecast

    def send(self) -> None:
        """予報メールを送信するユースケース

        Raises:
            RuntimeError: メールの送信に失敗した場合
        """
        forecast_data: List[dict] = self.fetch_forecast_data()
        forecastmailbody: ForecastMailBody = ForecastMailBody(forecast_data)
        mailbody: str = forecastmailbody.compose()
        try:
            self.sendmail.send(mailbody)
        except Exception as e:
            raise Exception(e)

    def fetch_forecast_data(self) -> List[dict]:
        """予報データを取得する

        Raises:
            RuntimeError: 予報データ取得APIのレスポンスコードが200以外の場合

        Returns:
            List[dict]: 予報データ
        """

        forecast_dto: List[ForecastDto] = self.createdailyforecast.create_forecast()
        forecast_data: List[dict] = [element.__dict__ for element in forecast_dto]
        forecast_data_dict: dict = {"forecast": forecast_data}

        # response_dict: dict = {
        #     "forecast": [
        #         {"datetime": "06:00", "difference": 0, "pressure": 1005},
        #         {"datetime": "09:00", "difference": 1, "pressure": 1006},
        #         {"datetime": "12:00", "difference": -2, "pressure": 1004},
        #         {"datetime": "15:00", "difference": 0, "pressure": 1004},
        #         {"datetime": "18:00", "difference": 1, "pressure": 1005},
        #         {"datetime": "21:00", "difference": 1, "pressure": 1006},
        #     ]
        # }
        # 取り出したリストを返す
        forecast_data: List[dict] = forecast_data_dict["forecast"]
        return forecast_data
