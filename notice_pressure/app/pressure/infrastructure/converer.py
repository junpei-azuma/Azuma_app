from datetime import datetime
from typing import Final, List

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
                "dt": datetime.fromtimestamp(element["dt"]).strftime("%Y%m%d%H%M"),
                "pressure": element["pressure"],
            }
            for element in extracted_list
        ]
        return converted_list
