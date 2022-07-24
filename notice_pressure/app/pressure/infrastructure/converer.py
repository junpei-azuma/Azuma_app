from datetime import date, datetime, timedelta
from typing import Final, List
import time
from pytz import timezone
import re

# openweatherAPIから返ってくる値は固定であり、keyの抜け落ちは無いと想定する。
# そのため、例外処理は実装しない


class Converter:
    @staticmethod
    def extract(response_dict: dict) -> list:
        """OpenweatherAPIから取得したデータから、日時と気圧情報のみを抽出する。

        Args:
            response_dict (dict): openweatherAPIからのレスポンス

        Returns:
            list: 抽出後のリスト
        """
        extracted_list: list = [
            dict(
                filter(
                    lambda element: element[0] == "dt" or element[0] == "pressure",
                    element.items(),
                )
            )
            for element in response_dict["hourly"]
        ]
        return extracted_list

    @staticmethod
    def convert_unixtime(extracted_list: list) -> list:
        """抽出後リストのUNIX時間を日付に変換する。

        Args:
            extracted_list (list): 抽出後リスト

        Returns:
            list: 変換後リスト
        """
        converted_list: Final[List] = [
            {
                "dt": datetime.fromtimestamp(
                    element["dt"], timezone("Asia/Tokyo")
                ).strftime("%Y%m%d%H%M"),
                "pressure": element["pressure"],
            }
            for element in extracted_list
        ]
        return converted_list

    @staticmethod
    def filter_by_datetime(
        converted_list: list,
        __TOMORROW: date = (datetime.now() + timedelta(days=1)).date(),
    ) -> list:
        """日付が明日のデータのみ取得する

        Args:
            converted_list (list): UNIX時刻を日付に変換したデータのリスト

        Returns:
            list: 明日のデータを抽出したリスト
        """

        # 文字列をdatetime型に変換⇒datetime型をdate型に変換する
        filterd_by_date_list: Final[List] = [
            element
            for element in converted_list
            if Converter.convert_str_to_date(element["dt"]) == __TOMORROW
        ]
        return filterd_by_date_list

    @staticmethod
    def convert_str_to_date(datetime_str: str) -> date:
        """日付の文字列をdate型オブジェクトに変換する

        Raises:
            ValueError: 形式がyyyymmddHMでない場合

        Returns:
            _type_: date型オブジェクト
        """
        if not re.match("[0-9]{12}", datetime_str):
            raise ValueError("日付の形式が不正です。")

        tmp: datetime = datetime.strptime(datetime_str, "%Y%m%d%H%M")
        date_object: date = date(tmp.year, tmp.month, tmp.day)
        return date_object

    @staticmethod
    def filter_by_time(filtered_by_date_list: list) -> list:
        """

        Args:
            filtered_by_date_list (list): _description_

        Returns:
            list: _description_
        """
        # 取得対象の時間
        target_hours: List[int] = [6, 9, 12, 15, 18, 21]

        filtered_by_time_list: Final[List] = [
            element
            for element in filtered_by_date_list
            if datetime.strptime(element["dt"], "%Y%m%d%H%M").hour in target_hours
        ]
        return filtered_by_time_list
