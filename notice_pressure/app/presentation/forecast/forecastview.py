from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, OK
from typing import List
from app.configration import Dependency
from flask import Blueprint, jsonify, abort
from app.forecast import CreateDailyForecast, ForecastDto
from app.presentation.forecast import Converter


class ForecastView:
    forecast_route = Blueprint("forecast", __name__, url_prefix="/forecast")

    @forecast_route.route("/", methods=["GET"])
    def get():
        """翌日の気圧データを返す

        Returns:
            _type_: 翌日06~21時の3時間ごとの気圧データ
        """
        dependency: Dependency = Dependency()
        create_forecast: CreateDailyForecast = dependency.resolve(CreateDailyForecast)
        try:
            daily_forecast: List[ForecastDto] = create_forecast.create_forecast()
        except (RuntimeError) as e:
            abort(INTERNAL_SERVER_ERROR)
        except ValueError as e:
            abort(BAD_REQUEST)

        daily_forecst_dict: dict = Converter.to_dict(daily_forecast)
        return jsonify(daily_forecst_dict)
