from datetime import datetime
from typing import List

from pyrsistent import PRecord
from app.pressure import DailyPressure, Pressure


def test_空の状態でインスタンス初期化():
    # 事前準備： なし

    # 操作： 引数無しでインスタンス生成
    dailypressure: DailyPressure = DailyPressure()

    # 想定結果： 正常にインスタンス生成できている
    assert isinstance(dailypressure, DailyPressure)


def test_配列を渡してインスタンス初期化():
    # 事前準備: Pressureインスタンスを生成
    pressure: Pressure = Pressure(datetime(2022, 7, 17, 15, 0, 0), 1000)

    # 操作： 配列を引数に渡してインスタンス生成
    pressurelist: List[Pressure] = [pressure]
    dailypressure: DailyPressure = DailyPressure(pressurelist)

    # 想定結果： 正常にインスタンス生成できている
    assert isinstance(dailypressure, DailyPressure)

    assert isinstance(dailypressure.pressurelist, list)
    assert len(dailypressure.pressurelist) == 1


def test_配列に要素追加():
    # 事前準備1: Pressureインスタンス生成
    pressure: Pressure = Pressure(datetime(2022, 7, 17, 15, 0, 0), 1000)

    added_pressure: Pressure = Pressure(datetime(2022, 7, 17, 18, 0, 0), 1005)

    # 事前準備2: 配列を引数に渡してインスタンス生成
    pressurelist: List[Pressure] = [pressure]
    dailypressure: DailyPressure = DailyPressure(pressurelist)

    # 操作： Pressureインスタンスを追加
    added_dailypressure: DailyPressure = dailypressure.add(added_pressure)

    # 想定結果： 2つの要素を持つ配列が生成されている
    assert isinstance(added_dailypressure, DailyPressure)
    assert len(added_dailypressure.pressurelist) == 2

    # 元の配列は変化していない
    assert len(dailypressure.pressurelist) == 1
