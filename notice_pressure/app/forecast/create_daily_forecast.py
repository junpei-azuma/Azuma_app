from typing import List
from injector import inject
from app.pressure import PressureRepository
from app.forecast import DailyForecast, Forecast, ForecastFactory
from app.pressure import Pressure
from app.forecast.forecast_dto import ForecastDto


class CreateDailyForecast:
    @inject
    def __init__(self, pressurerepository: PressureRepository) -> None:
        self.pressurerepository: PressureRepository = pressurerepository

    def create_forecast(self) -> List[ForecastDto]:
        """1日分の気圧データを取得し、DTOに変換して返す。

        Raises:
            RuntimeError: OpenWeatherMapAPIの呼び出し時にエラーが発生した場合

        Returns:
            List[ForecastDto]: DTOを要素に持つリスト
        """
        # 1日分の気圧データを取得
        try:
            daily_pressure: List[
                Pressure
            ] = self.pressurerepository.get_daily_pressure()
        except RuntimeError as e:
            raise RuntimeError(e)

        # 1日分の気圧データから予報データを作成する。
        daily_forecast: DailyForecast = self.hoge(daily_pressure)
        daily_forecast_data: List[ForecastDto] = [
            self.getForecastData(element) for element in daily_forecast.forecastlist
        ]
        return daily_forecast_data

    def hoge(self, daily_pressure: List[Pressure]) -> DailyForecast:
        """OpenWeatherMapから取得したデータをDailyForeCastインスタンスに変換する。

        Args:
            daily_pressure (List[Pressure]): 気圧データのリスト

        Returns:
            DailyForecast: _description_
        """
        forecast_list: List[Forecast] = list()

        for i, pressure in enumerate(daily_pressure):
            ## 先頭の要素(AM3時)はスキップする
            if i == 0:
                continue
            ## AM06:00以降は3時間前との差分を持つ
            current_pressure: Pressure = pressure
            pressure_3hours_ago: Pressure = daily_pressure[i - 1]
            forecast: Forecast = ForecastFactory.create_forecast(
                current_pressure, pressure_3hours_ago
            )
            forecast_list.append(forecast)

        daily_forecast: DailyForecast = DailyForecast(forecast_list)
        return daily_forecast

    def getForecastData(self, forecast: Forecast) -> ForecastDto:
        """ForecastインスタンスをDTOに変換する

        Args:
            forecast (Forecast): Forecastインスタンス

        Returns:
            ForecastDto: ForeCastDTO
        """
        forecast_dto: ForecastDto = ForecastDto(
            forecast.pressure.datetime.strftime("%Y%m%d%H%M"),
            forecast.pressure.value,
            forecast.pressure_change.calculate(),
        )
        return forecast_dto
