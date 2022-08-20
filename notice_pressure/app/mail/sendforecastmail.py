from http.client import OK
import json
from typing import List
from injector import inject
from .sendmail import SendMail
from .forecastmailbody import ForecastMailBody
import requests


class SendForecastMail:
    @inject
    def __init__(self, sendmail: SendMail):
        self.sendmail: SendMail = sendmail

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
        response: requests.Response = requests.get(
            "http://localhost:5000/api/v1/forecast/"
        )

        if response.status_code != OK:
            raise RuntimeError("気圧情報の取得に失敗しました。")

        # jsonをdictに変換してforecastを取り出す
        response_dict: dict = json.loads(response.text)
        # 取り出したリストを返す
        forecast_data: List[dict] = response_dict["forecast"]
        return forecast_data
