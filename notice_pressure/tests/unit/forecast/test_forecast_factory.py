from datetime import datetime

from colorama import Fore
from app.forecast import ForecastFactory, Forecast
from app.pressure import Pressure


def AM06時の予報を生成する():
    # 事前準備： 気圧インスタンスを作成する
    pressure: Pressure = Pressure(datetime(2022, 7, 25, 12, 00), 1000)

    # 操作： 予報インスタンスを作成する
    AM06_forecast: Forecast = ForecastFactory.create_AM06forecast(pressure)

    # 想定結果： 正しくインスタンス生成できている
    assert isinstance(AM06_forecast, Forecast)

    assert AM06_forecast.pressure.datetime == datetime(2022, 7, 25, 12, 00)
    assert AM06_forecast.pressure.value == 1000
    assert AM06_forecast.pressure_change == None
