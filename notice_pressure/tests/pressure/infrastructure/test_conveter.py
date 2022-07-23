from datetime import datetime
import json
from typing import Final, List
from app.pressure import Converter


def test_レスポンスから日時と気圧を抽出():
    # 事前準備： レスポンスデータを読み込み
    file = open("notice_pressure/tests/pressure/infrastructure/forecast.json", "r")
    response_object = json.load(file)

    # 操作：extractメソッドを呼び出し
    extracted_list: Final[List] = Converter.extract(response_object)

    # 想定結果：

    ## list型で抽出されている
    assert isinstance(extracted_list, list)

    ## 48時間分のデータが取得されている
    assert len(extracted_list) == 48

    ## unix時間と気圧情報が取得できている
    assert extracted_list[0]["dt"] == 1658494800
    assert extracted_list[0]["pressure"] == 1004
    ## humidityキーが除外されている
    assert not "humidity" in extracted_list[0]


def test_レスポンスのUNIXタイムを日付に変換():
    # 事前準備： レスポンスデータから日時と気圧を抽出する
    file = open("notice_pressure/tests/pressure/infrastructure/forecast.json", "r")
    response_object = json.load(file)
    extracted_list: Final[List] = Converter.extract(response_object)

    # 操作： convert_unixtimeメソッドを呼び出す
    conveted_list: Final[List] = Converter.convert_unixtime(extracted_list)

    # 想定結果

    ## UNIX時間が日付に変換されている
    assert conveted_list[0]["dt"] == "202207222200"
    ## 気圧は変換されていない
    assert conveted_list[0]["pressure"] == 1004
