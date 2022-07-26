from datetime import datetime
from typing import List
from unittest import mock
from unittest.mock import Mock
from app.pressure import PressureRepository, Pressure, PressureRepositoryImpl
from app.forecast import CreateDailyForecast, DailyForecast, Forecast


# コンストラクタのテスト
def test_インスタンスを生成する():
    repository_mock: PressureRepository = Mock(spec=PressureRepository)

    create_daily_forecast: CreateDailyForecast = CreateDailyForecast(repository_mock)

    assert isinstance(create_daily_forecast, CreateDailyForecast)
    assert isinstance(create_daily_forecast.pressurerepository, PressureRepository)


# hoge関数のテスト
def test_Pressureインスタンスから1日分の予報を生成する():
    # 事前準備： Pressureインスタンスのリストを作成する
    daily_pressure: List[Pressure] = [
        Pressure(datetime(2022, 7, 25, 6, 0, 0), 1000),
        Pressure(datetime(2022, 7, 25, 9, 0, 0), 1005),
        Pressure(datetime(2022, 7, 25, 12, 0, 0), 1001),
    ]
    # 操作： 気圧データから予報データを生成
    repository_mock: PressureRepository = Mock(spec=PressureRepository)

    create_daily_forecast: CreateDailyForecast = CreateDailyForecast(repository_mock)
    daily_forecast: DailyForecast = create_daily_forecast.hoge(daily_pressure)

    # 想定結果： 正しくインスタンス生成できている
    assert isinstance(daily_forecast, DailyForecast)
    assert isinstance(daily_forecast.forecastlist, list)

    assert len(daily_forecast.forecastlist) == 3

    # リスト内の予報インスタンスを検証する

    ## AM06時の予報
    AM06_forecast: Forecast = daily_forecast.forecastlist[0]
    isinstance(AM06_forecast, Forecast)
    assert AM06_forecast.pressure.value == 1000
    assert AM06_forecast.pressure.datetime == datetime(2022, 7, 25, 6, 0, 0)
    assert AM06_forecast.pressure_change is None

    ## AM09時の予報
    AM09_forecast: Forecast = daily_forecast.forecastlist[1]
    isinstance(AM09_forecast, Forecast)
    assert AM09_forecast.pressure.datetime == datetime(2022, 7, 25, 9, 0, 0)
    assert AM09_forecast.pressure.value == 1005
    assert AM09_forecast.pressure_change.calculate() == 5

    ## AM12時の予報
    AM12_forecast: Forecast = daily_forecast.forecastlist[2]
    isinstance(AM12_forecast, Forecast)
    assert AM12_forecast.pressure.datetime == datetime(2022, 7, 25, 12, 0, 0)
    assert AM12_forecast.pressure.value == 1001
    assert AM12_forecast.pressure_change.calculate() == -4


def test_ユースケース_正常系(mocker):
    # 事前準備：ユースケースクラスのインスタンスを作成
    pressurerepository: PressureRepository = mock.MagicMock()
    daily_pressure: List[Pressure] = [
        Pressure(datetime(2022, 7, 25, 6, 0, 0), 1000),
        Pressure(datetime(2022, 7, 25, 9, 0, 0), 1005),
        Pressure(datetime(2022, 7, 25, 12, 0, 0), 1001),
    ]
    mocker.patch.object(
        pressurerepository,
        "get_daily_pressure",
        return_value=daily_pressure,
    )
    create_daily_forecast: CreateDailyForecast = CreateDailyForecast(pressurerepository)

    # 操作： 気圧データ生成処理を実行する
    daily_forecast: DailyForecast = create_daily_forecast.create_forecast()

    # 想定結果： 正しくインスタンス生成できている
    assert isinstance(daily_forecast, DailyForecast)
    assert isinstance(daily_forecast.forecastlist, list)

    assert len(daily_forecast.forecastlist) == 3
    ## AM06時の予報
    AM06_forecast: Forecast = daily_forecast.forecastlist[0]
    isinstance(AM06_forecast, Forecast)
    assert AM06_forecast.pressure.value == 1000
    assert AM06_forecast.pressure.datetime == datetime(2022, 7, 25, 6, 0, 0)
    assert AM06_forecast.pressure_change is None

    ## AM09時の予報
    AM09_forecast: Forecast = daily_forecast.forecastlist[1]
    isinstance(AM09_forecast, Forecast)
    assert AM09_forecast.pressure.datetime == datetime(2022, 7, 25, 9, 0, 0)
    assert AM09_forecast.pressure.value == 1005
    assert AM09_forecast.pressure_change.calculate() == 5

    ## AM12時の予報
    AM12_forecast: Forecast = daily_forecast.forecastlist[2]
    isinstance(AM12_forecast, Forecast)
    assert AM12_forecast.pressure.datetime == datetime(2022, 7, 25, 12, 0, 0)
    assert AM12_forecast.pressure.value == 1001
    assert AM12_forecast.pressure_change.calculate() == -4
