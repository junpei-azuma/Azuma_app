from .forecast import Forecast


class ForecastDto:
    def __init__(self, forecast: Forecast) -> None:
        """ドメインオブジェクトをクライアントに公開できる形に変換する。

        Args:
            forecast (Forecast): _description_
        """
        self.__datetime_str: str = forecast.pressure.datetime.strftime("%Y%m%d%H%M")
        self.__pressure: int = forecast.pressure.value
        self.__difference: int = forecast.pressure_change.calculate()

    @property
    def datetime(self) -> str:
        return self.__datetime_str

    @property
    def pressure(self) -> int:
        return self.__pressure

    @property
    def difference(self) -> int:
        return self.__difference
