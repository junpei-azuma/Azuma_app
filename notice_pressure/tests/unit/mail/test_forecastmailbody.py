from typing import List
from app.mail import ForecastMailBody
import pytest

from app.mail import ForecastMailBody


@pytest.mark.freeze_time("2022-08-14")
def test_本文見出しを生成():
    # 事前準備：なし

    # 操作： 見出しを生成する。
    headline = ForecastMailBody._set_headline()

    # 想定結果： 「08/15 (月)の気圧予想です。」という文字列が返る
    assert headline == "08/15 (Mon) の気圧予想です。"


def test_本文のメインコンテンツを生成():
    daily_forecast: List[dict] = [
        {"date": "06:00", "pressure": "1000", "difference": "1"},
        {"date": "09:00", "pressure": "1003", "difference": "3"},
        {"date": "12:00", "pressure": "1002", "difference": "-1"},
    ]

    main_content: str = ForecastMailBody._set_main(daily_forecast)

    assert main_content == "06:00: 1000hPa(1)\n09:00: 1003hPa(3)\n12:00: 1002hPa(-1)"


@pytest.mark.freeze_time("2022-08-14")
def test_本文を生成():
    # 事前準備： ForecastMailBodyインスタンスを生成する。
    daily_forecast: List[dict] = [
        {"date": "06:00", "pressure": "1000", "difference": "1"},
        {"date": "09:00", "pressure": "1003", "difference": "3"},
        {"date": "12:00", "pressure": "1002", "difference": "-1"},
    ]

    forecastmailbody: ForecastMailBody = ForecastMailBody(daily_forecast)

    # 操作： メール本文を生成
    body: str = forecastmailbody.compose()

    # 想定結果： メール本文が正しく作成されている。
    assert (
        body
        == "08/15 (Mon) の気圧予想です。\n\n06:00: 1000hPa(1)\n09:00: 1003hPa(3)\n12:00: 1002hPa(-1)"
    )
