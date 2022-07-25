from colorama import Fore
from app.pressure import Pressure, PressureChange
from app.forecast import Forecast


class ForecastFactory:
    """forecastインスタンスを生成するクラス
    "" forecastインスタンスはAM06:00とそれ以外で生成方法が異なるため、
    "" 生成を責務とするクラスを作成しています
    """

    @staticmethod
    def create_AM06forecast(pressure: Pressure) -> Forecast:
        """翌日午前6時の気圧予報を生成する
        ""
        ""
        Args:
            pressure (Pressure): pressureインスタンス

        Returns:
            Forecast: 午前6時の予報
        """
        am06_forecast: Forecast = Forecast(pressure, None)
        return am06_forecast

    @staticmethod
    def create_forecast(current_pressure: Pressure, pressure_3hours_ago: Pressure):
        """午前9時以降の気圧予報を生成する。

        Args:
            current_pressure (Pressure): 現在日時の気圧
            pressure_3hours_ago (Pressure): 3時間前の気圧

        Returns:
            _type_: 予報インスタンス
        """

        pressure_change: PressureChange = PressureChange(
            current_pressure, pressure_3hours_ago
        )
        forecast: Forecast = Forecast(current_pressure, pressure_change)
        return forecast
