from datetime import datetime
from typing import Final

import pytest
from app.pressure import Pressure

# 最小値・最大値もテストする
@pytest.mark.parametrize("pressure_value", [1000, 967, 1039])
def test_インスタンス生成正常系(pressure_value: int):
    # 事前準備：なし

    # 操作： インスタンス生成
    date: Final[datetime] = datetime(2022, 7, 9, 12, 30, 21)
    value: Final[int] = pressure_value

    pressure: Pressure = Pressure(date, value)

    # 想定結果： インスタンスが正常に生成される
    assert isinstance(pressure, Pressure)
    assert pressure.datetime == datetime(2022, 7, 9, 12, 30, 21)
    assert pressure.value == pressure_value


def test_インスタンス生成異常系_最小値未満():
    # 事前準備： なし

    # 操作； インスタンス生成
    with pytest.raises(ValueError) as e:
        date: Final[datetime] = datetime(2022, 7, 9, 12, 30, 21)
        value: Final[int] = 966
        pressure: Pressure = Pressure(date, value)

    # 想定結果： 例外発生
    assert str(e.value) == "気圧の値が観測史上最低値未満です。"


def test_インスタンス生成異常系_最大値超過():
    # 事前準備： なし

    # 操作； インスタンス生成
    with pytest.raises(ValueError) as e:
        date: Final[datetime] = datetime(2022, 7, 9, 12, 30, 21)
        value: Final[int] = 1040
        pressure: Pressure = Pressure(date, value)

    # 想定結果： 例外発生
    assert str(e.value) == "気圧の値が観測史上最高値を超過しています。"
