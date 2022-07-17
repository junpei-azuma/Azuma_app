from datetime import datetime
from typing import List
from app.forecast import DailyForecast
from app.forecast import Forecast
from app.pressure import Pressure
from app.pressure import PressureChange


def test_空の状態でインスタンス初期化():
    # 事前準備： なし

    # 操作： 引数無しでインスタンス生成
    dailyforecast: DailyForecast = DailyForecast()

    # 想定結果： 正常にインスタンス生成できている
    assert isinstance(dailyforecast, DailyForecast)


def test_配列を渡してインスタンス初期化():
    # 事前準備： Forecastインスタンスを作成
    pressure: Pressure = Pressure(datetime(2022, 7, 17, 15, 0, 0), 1000)
    pressure_3hour_ago: Pressure = Pressure(datetime(2022, 7, 17, 12, 0, 0), 995)
    pressure_change: PressureChange = PressureChange(pressure, pressure_3hour_ago)
    forecast: Forecast = Forecast(datetime.now(), pressure, pressure_change)

    # 操作： 配列を引数に渡してインスタンス生成
    forecastlist: List[Forecast] = [forecast]
    dailyforecast: DailyForecast = DailyForecast(forecastlist)

    # 想定結果： 正常にインスタンス生成できている
    assert isinstance(dailyforecast, DailyForecast)

    assert isinstance(dailyforecast.forecastlist, list)
    assert len(dailyforecast.forecastlist) == 1


def test_配列に要素追加():
    # 事前準備1： Forecastインスタンスを作成
    pressure: Pressure = Pressure(datetime(2022, 7, 17, 15, 0, 0), 1000)
    pressure_3hour_ago: Pressure = Pressure(datetime(2022, 7, 17, 12, 0, 0), 995)
    pressure_change: PressureChange = PressureChange(pressure, pressure_3hour_ago)
    forecast: Forecast = Forecast(datetime.now(), pressure, pressure_change)

    added_pressure: Pressure = Pressure(datetime(2022, 7, 17, 18, 0, 0), 1005)
    added_pressure_3hour_ago: Pressure = Pressure(datetime(2022, 7, 17, 15, 0, 0), 995)
    added_pressure_change: PressureChange = PressureChange(
        added_pressure, added_pressure_3hour_ago
    )
    added_forecast: Forecast = Forecast(
        datetime.now(), added_pressure, added_pressure_change
    )

    # 事前準備2:  配列を引数に渡してインスタンス生成
    forecastlist: List[Forecast] = [forecast]
    dailyforecast: DailyForecast = DailyForecast(forecastlist)

    # 事前準備3: Forecastインスタンスを追加
    added_dailyforecast: DailyForecast = dailyforecast.add(added_forecast)

    # 想定結果： 2つの要素を持つ配列が作成されている
    assert isinstance(added_dailyforecast, DailyForecast)
    assert len(added_dailyforecast.forecastlist) == 2

    # 元の配列は変化していない
    assert len(dailyforecast.forecastlist) == 1
