from datetime import date, datetime, timedelta
import json
from typing import Final, List
from app.pressure import Converter


def test_レスポンスから日時と気圧を抽出():
    # 事前準備： レスポンスデータを読み込み
    original_data = {"hourly": [{"dt": 1658494800, "pressure": 1004}]}

    # 操作：extractメソッドを呼び出し
    extracted_list: Final[List] = Converter.extract(original_data)

    # 想定結果：

    ## list型で抽出されている
    assert isinstance(extracted_list, list)

    ## データを取得できている
    assert len(extracted_list) == 1

    ## unix時間と気圧情報が取得できている
    assert extracted_list[0]["dt"] == 1658494800
    assert extracted_list[0]["pressure"] == 1004
    ## humidityキーが除外されている
    assert not "humidity" in extracted_list[0]


def test_レスポンスのUNIXタイムを日付に変換():
    # 事前準備： レスポンスデータから日時と気圧を抽出する
    original_data = {"hourly": [{"dt": 1658494800, "pressure": 1004}]}
    extracted_list: Final[List] = Converter.extract(original_data)

    # 操作： convert_unixtimeメソッドを呼び出す
    conveted_list: Final[List] = Converter.convert_unixtime(extracted_list)

    # 想定結果

    ## UNIXタイムが日付に変換されている
    assert conveted_list[0]["dt"] == "202207222200"
    ## 気圧は変換されていない
    assert conveted_list[0]["pressure"] == 1004


def test_日付型文字列をdate型に変換する():
    # 事前準備： 日付型文字列を作成する
    datetime_str: str = "202207222100"

    # 操作： 日付型文字列をdate型に変換する。
    converted_date: date = Converter.convert_str_to_date(datetime_str)

    # 想定結果： 正常に変換されている
    assert isinstance(converted_date, date)

    # 日付が正しく取得できている。
    assert converted_date == date(2022, 7, 22)


def test_レスポンスから翌日のデータのみを抽出():
    # 事前準備： UNIXタイムを日付に変換する
    json_open = open(
        "notice_pressure/tests/unit/pressure/infrastructure/forecast.json", "r"
    )
    original_data: dict = json.load(json_open)
    extracted_list: Final[List] = Converter.extract(original_data)
    converted_list: Final[List] = Converter.convert_unixtime(extracted_list)

    # 操作： 日付で絞り込む
    filterd_by_datetime_list: Final[List] = Converter.filter_by_datetime(
        converted_list, date(2022, 7, 23)
    )

    # 想定結果： 正常にデータを抽出できている
    assert isinstance(filterd_by_datetime_list, list)

    # 明日1日分のデータのみ取得されている
    assert len(filterd_by_datetime_list) == 24

    assert filterd_by_datetime_list[0]["dt"] == "202207230000"
    assert filterd_by_datetime_list[0]["pressure"] == 1004

    assert filterd_by_datetime_list[-1]["dt"] == "202207232300"
    assert filterd_by_datetime_list[-1]["pressure"] == 1007


# 意図した時間帯(6,9,12,15,18,21時)のデータが取れていることを担保したいため、
# リストの全データを確認します。
def test_レスポンスから特定の時間帯のデータを抽出する():
    # 事前準備：レスポンスから明日のデータを抽出する。
    json_open = open(
        "notice_pressure/tests/unit/pressure/infrastructure/forecast.json", "r"
    )
    original_data: dict = json.load(json_open)
    extracted_list: Final[List] = Converter.extract(original_data)
    converted_list: Final[List] = Converter.convert_unixtime(extracted_list)
    filterd_by_datetime_list: Final[List] = Converter.filter_by_datetime(
        converted_list, date(2022, 7, 23)
    )

    # 操作： 特定時間帯のデータを抽出する。
    filterd_by_time_list: Final[List] = Converter.filter_by_time(
        filterd_by_datetime_list
    )

    # 想定結果：必要なデータのみ取得されている
    assert isinstance(filterd_by_time_list, list)

    # 6,9,12,15,18,21時のデータが取得されている
    assert len(filterd_by_time_list) == 6

    assert filterd_by_time_list[0]["dt"] == "202207230600"
    assert filterd_by_time_list[0]["pressure"] == 1005

    assert filterd_by_time_list[1]["dt"] == "202207230900"
    assert filterd_by_time_list[1]["pressure"] == 1005

    assert filterd_by_time_list[2]["dt"] == "202207231200"
    assert filterd_by_time_list[2]["pressure"] == 1005

    assert filterd_by_time_list[3]["dt"] == "202207231500"
    assert filterd_by_time_list[3]["pressure"] == 1005

    assert filterd_by_time_list[4]["dt"] == "202207231800"
    assert filterd_by_time_list[4]["pressure"] == 1005

    assert filterd_by_time_list[5]["dt"] == "202207232100"
    assert filterd_by_time_list[5]["pressure"] == 1007
