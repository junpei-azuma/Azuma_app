from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR
from typing import List
from app.configration import Dependency
from flask import Blueprint, jsonify, abort
from app.forecast import CreateDailyForecast, ForecastDto
from app.pressure.pressurerepository import PressureRepository


class ForecastView:
    forecast_route = Blueprint("forecast", __name__, url_prefix="/forecast")

    @forecast_route.route("/", methods=["GET"])
    def get():
        dependency: Dependency = Dependency()
        create_forecast: CreateDailyForecast = dependency.resolve(PressureRepository)
        try:
            daily_forecast: List[ForecastDto] = create_forecast.create_forecast()
        except RuntimeError as e:
            abort(INTERNAL_SERVER_ERROR)
        except ValueError as e:
            abort(BAD_REQUEST)

        # 辞書に変換する
        # {'forecast' : [daily_forecast]}

        # jsonに変換する。
