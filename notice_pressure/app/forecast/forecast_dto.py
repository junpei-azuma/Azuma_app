class ForecastDto:
    def __init__(self, datatime: str, pressure: int, pressure_difference: int) -> None:
        """ドメインオブジェクトをクライアントに公開できる形に変換する。

        Args:
            forecast (Forecast): _description_
        """
        self.datetime: str = datatime
        self.pressure: int = pressure
        self.difference: int = pressure_difference
