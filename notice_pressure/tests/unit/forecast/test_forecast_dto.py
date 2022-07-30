from app.forecast import Forecast, ForecastFactory
from app.pressure import Pressure
from datetime import datetime

from app.forecast import ForecastDto


def test_ForecastオブジェクトをDTOに変換する():
    # 準備： Forecastインスタンスを生成する。
    current_pressure: Pressure = Pressure(datetime(2022, 7, 25, 12, 0, 0), 1000)
    pressure_3hours_ago: Pressure = Pressure(datetime(2022, 7, 25, 9, 0, 0), 1005)

    forecast: Forecast = ForecastFactory.create_forecast(
        current_pressure, pressure_3hours_ago
    )

    # 操作： ForeCastDtoインスタンスを生成する。
    forecast_dto: ForecastDto = ForecastDto(
        forecast.pressure.datetime.strftime("%Y%m%d%H%M"),
        forecast.pressure.value,
        forecast.pressure_change.calculate(),
    )

    # 想定結果： 正しくインスタンス生成できている
    assert forecast_dto.pressure == 1000
    assert forecast_dto.datetime == "202207251200"
    assert forecast_dto.difference == -5
