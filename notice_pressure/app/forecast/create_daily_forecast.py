from typing import List
from colorama import Fore
from injector import inject
from app.pressure import PressureRepository
from app.forecast import DailyForecast, Forecast, ForecastFactory
from app.pressure import Pressure


class CreateDailyForecast:
    @inject
    def __init__(self, pressurerepository: PressureRepository) -> None:
        self.pressurerepository: PressureRepository = pressurerepository

    def create_forecast(self) -> DailyForecast:
        # 1日分の気圧データを取得
        daily_pressure: List[Pressure] = self.pressurerepository.get_daily_pressure()
