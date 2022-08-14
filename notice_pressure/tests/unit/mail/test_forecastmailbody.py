from app.mail import ForecastMailBody
import pytest


@pytest.mark.freeze_time("2022-08-14")
def test_本文見出しを生成():
    # 事前準備：なし

    # 操作： 見出しを生成する。
    headline = ForecastMailBody.set_headline()

    # 想定結果： 「08/15 (月)の気圧予想です。」という文字列が返る
    assert headline == "08/15 (Mon) の気圧予想です。"
