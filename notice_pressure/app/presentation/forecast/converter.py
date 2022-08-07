import json
from typing import Dict, List
from app.forecast import ForecastDto


class Converter:
    @staticmethod
    def to_dict(daily_forecast: List[ForecastDto]) -> dict:
        """ユースケース層から渡されたDTOのリストをdictに変換する

        Args:
            daily_forecast (List[ForecastDto]): DTO

        Returns:
            dict: 辞書形式のデータ
        """
        daily_forecast_value: List[dict] = [
            element.__dict__ for element in daily_forecast
        ]
        daily_forecast_dict: dict = {"forecast": daily_forecast_value}
        return daily_forecast_dict
