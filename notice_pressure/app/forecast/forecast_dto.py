class ForecastDto:
    def __init__(self, datatime: str, pressure: int, pressure_difference: int) -> None:
        """ドメインオブジェクトをクライアントに公開できる形に変換する。

        Args:
            forecast (Forecast): _description_
        """
        self.__datetime_str: str = datatime
        self.__pressure: int = pressure
        self.__difference: int = pressure_difference

    @property
    def datetime(self) -> str:
        return self.__datetime_str

    @property
    def pressure(self) -> int:
        return self.__pressure

    @property
    def difference(self) -> int:
        return self.__difference
