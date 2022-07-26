from typing import List
from injector import inject
from app.pressure import PressureRepository
from app.forecast import DailyForecast, Forecast, ForecastFactory
from app.pressure import Pressure, PressureChange


class CreateDailyForecast:
    @inject
    def __init__(self, pressurerepository: PressureRepository) -> None:
        self.pressurerepository: PressureRepository = pressurerepository

    def create_forecast(self) -> DailyForecast:
        # 1日分の気圧データを取得
        try:
            daily_pressure: List[
                Pressure
            ] = self.pressurerepository.get_daily_pressure()
        except RuntimeError as e:
            raise RuntimeError(str(e.value))

        # 1日分の気圧データから予報データを作成する。
        daily_forecast: DailyForecast = self.hoge(daily_pressure)

        return daily_forecast

    def hoge(self, daily_pressure: List[Pressure]) -> DailyForecast:

        forecast_list: List[Forecast] = list()

        for i, pressure in enumerate(daily_pressure):
            ## 先頭の要素(AM6時)は3時間前との差分を持たない
            if i == 0:
                forecast: Forecast = ForecastFactory.create_AM06forecast(pressure)

            ## AM09:00以降は3時間前との差分を持つ
            else:
                current_pressure: Pressure = pressure
                pressure_3hours_ago: Pressure = daily_pressure[i - 1]
                forecast: Forecast = ForecastFactory.create_forecast(
                    current_pressure, pressure_3hours_ago
                )
            forecast_list.append(forecast)

        daily_forecast: DailyForecast = DailyForecast(forecast_list)
        return daily_forecast
