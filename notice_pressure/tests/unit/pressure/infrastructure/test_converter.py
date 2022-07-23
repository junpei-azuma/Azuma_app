from datetime import datetime
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

    ## UNIX時間が日付に変換されている
    assert conveted_list[0]["dt"] == "202207222200"
    ## 気圧は変換されていない
    assert conveted_list[0]["pressure"] == 1004
