from datetime import datetime

import pytest
from app.pressure import Pressure, PressureChange


@pytest.mark.parametrize(
    "current_datetime, past_datetime",
    [
        (datetime(2022, 7, 1, 21, 59, 0), datetime(2022, 7, 1, 19, 59, 0)),  # 時間差が2:00
        (datetime(2022, 7, 1, 21, 59, 0), datetime(2022, 7, 1, 18, 00, 0)),
    ],
)  # 時間差が3:59
def test_時間差分計算_戻り値が真(current_datetime: datetime, past_datetime: datetime):
    current_pressure: Pressure = Pressure(current_datetime, 1000)
    pressure_ago: Pressure = Pressure(past_datetime, 1005)
    assert PressureChange.validate_datetime_difference(current_pressure, pressure_ago)


@pytest.mark.parametrize(
    "current_datetime, past_datetime",
    [
        (datetime(2022, 7, 1, 21, 59, 0), datetime(2022, 7, 1, 20, 0, 0)),  # 時間差が1:59
        (datetime(2022, 7, 1, 23, 0, 0), datetime(2022, 6, 30, 19, 0, 0)),  # 時間差が4:00
        (datetime(2022, 7, 1, 23, 0, 0), datetime(2022, 6, 30, 23, 0, 1)),
    ],
)  # 過去日時の方が大きい
def test_時間差分計算_戻り値が偽(current_datetime: datetime, past_datetime: datetime):
    current_pressure: Pressure = Pressure(current_datetime, 1000)
    pressure_ago: Pressure = Pressure(past_datetime, 1005)
    print(current_pressure.datetime - pressure_ago.datetime)
    assert not PressureChange.validate_datetime_difference(
        current_pressure, pressure_ago
    )


def test_インスタンス生成正常系():
    # 事前準備： なし

    # 操作： インスタンス生成
    current_pressure: Pressure = Pressure(datetime(2022, 7, 1, 22, 0, 0), 1000)
    pressure_3hour_ago: Pressure = Pressure(datetime(2022, 7, 1, 20, 0, 0), 1005)

    pressure_change: PressureChange = PressureChange(
        current_pressure, pressure_3hour_ago
    )

    # 想定結果： インスタンスが生成されている
    assert isinstance(pressure_change, PressureChange)

    # プロパティの値が正しい
    assert pressure_change.current_pressure.datetime == datetime(2022, 7, 1, 22, 0, 0)
    assert pressure_change.current_pressure.value == 1000

    assert pressure_change.pressure_3hour_ago.datetime == datetime(2022, 7, 1, 20, 0, 0)
    assert pressure_change.pressure_3hour_ago.value == 1005


# 不正日時を判定するロジックは別のテストケースで検証済みのため、ここでは1パスのみでok
def test_インスタンス生成_異常系():
    # 事前準備： なし

    # 操作： インスタンス生成
    with pytest.raises(ValueError) as e:
        current_pressure: Pressure = Pressure(datetime(2022, 7, 1, 21, 59, 0), 1000)
        pressure_3hour_ago: Pressure = Pressure(datetime(2022, 7, 1, 20, 0, 0), 1005)

        pressure_change: PressureChange = PressureChange(
            current_pressure, pressure_3hour_ago
        )

    assert str(e.value) == "不正な日時です。"


def test_気圧の変化量計算_変化量が負の数値():
    # 事前準備： インスタンス生成
    current_pressure: Pressure = Pressure(datetime(2022, 7, 1, 22, 0, 0), 1000)
    pressure_3hour_ago: Pressure = Pressure(datetime(2022, 7, 1, 20, 0, 0), 1005)

    pressure_change: PressureChange = PressureChange(
        current_pressure, pressure_3hour_ago
    )

    # 操作： 気圧変化量計算
    pressure_change_value: int = pressure_change.calculate()

    # 想定結果： 正しく変化量が計算されている
    assert pressure_change_value == -5


def test_気圧の変化量計算_変化量が正の数値():
    # 事前準備： インスタンス生成
    current_pressure: Pressure = Pressure(datetime(2022, 7, 1, 22, 0, 0), 1000)
    pressure_3hour_ago: Pressure = Pressure(datetime(2022, 7, 1, 20, 0, 0), 995)

    pressure_change: PressureChange = PressureChange(
        current_pressure, pressure_3hour_ago
    )

    # 操作： 気圧変化量計算
    pressure_change_value: int = pressure_change.calculate()

    # 想定結果： 正しく変化量が計算されている
    assert pressure_change_value == 5
