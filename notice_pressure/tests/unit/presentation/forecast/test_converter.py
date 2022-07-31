from typing import List
from app.forecast import ForecastDto
from app.presentation.forecast import Converter


def test_DTOのリストをdictに変換する():
    # 事前準備： forecastDTOのリストを作成する。
    forecast_dto_list: List[ForecastDto] = [
        ForecastDto("202207250600", 1000, 1),
        ForecastDto("202207250900", 1001, 1),
        ForecastDto("202207251200", 1005, 4),
    ]
    # 操作： dictに変換する。
    daily_forecast_dict: dict = Converter.to_dict(forecast_dto_list)

    # 想定結果： 正しく変換できている
    assert isinstance(daily_forecast_dict, dict)
    assert isinstance(daily_forecast_dict["forecast"], list)
    # 先頭の要素
    assert daily_forecast_dict["forecast"][0]["datetime"] == "202207250600"
    assert daily_forecast_dict["forecast"][0]["pressure"] == 1000
    assert daily_forecast_dict["forecast"][0]["difference"] == 1

    # 2個目の要素
    assert daily_forecast_dict["forecast"][1]["datetime"] == "202207250900"
    assert daily_forecast_dict["forecast"][1]["pressure"] == 1001
    assert daily_forecast_dict["forecast"][1]["difference"] == 1

    # 3個目の要素
    assert daily_forecast_dict["forecast"][2]["datetime"] == "202207251200"
    assert daily_forecast_dict["forecast"][2]["pressure"] == 1005
    assert daily_forecast_dict["forecast"][2]["difference"] == 4
