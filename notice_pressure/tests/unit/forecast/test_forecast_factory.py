from datetime import datetime
from app.forecast import ForecastFactory, Forecast
from app.pressure import Pressure, PressureChange


def test_AM06時の予報を生成する():
    # 事前準備： 気圧インスタンスを作成する
    pressure: Pressure = Pressure(datetime(2022, 7, 25, 12, 0, 0), 1000)

    # 操作： 予報インスタンスを作成する
    AM06_forecast: Forecast = ForecastFactory.create_AM06forecast(pressure)

    # 想定結果： 正しくインスタンス生成できている
    assert isinstance(AM06_forecast, Forecast)

    assert AM06_forecast.pressure.datetime == datetime(2022, 7, 25, 12, 00)
    assert AM06_forecast.pressure.value == 1000
    assert AM06_forecast.pressure_change == None


def test_AM09時以降の予報を生成する():
    # 事前準備： 気圧インスタンス・3時間前の気圧インスタンスを生成する。
    current_pressure: Pressure = Pressure(datetime(2022, 7, 25, 12, 0, 0), 1000)
    pressure_3hours_ago: Pressure = Pressure(datetime(2022, 7, 25, 9, 0, 0), 1005)

    # 操作： 予報インスタンスを生成する
    forecast: Forecast = ForecastFactory.create_forecast(
        current_pressure, pressure_3hours_ago
    )

    # 想定結果： 正しくインスタンス生成できている
    assert isinstance(forecast, Forecast)

    assert forecast.pressure.datetime == datetime(2022, 7, 25, 12, 0)
    assert forecast.pressure.value == 1000
    assert isinstance(forecast.pressure_change, PressureChange)
    assert forecast.pressure_change.calculate() == -5
