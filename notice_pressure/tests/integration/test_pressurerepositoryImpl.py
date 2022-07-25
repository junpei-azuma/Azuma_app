from datetime import datetime, timedelta
from http.client import (
    BAD_REQUEST,
    FORBIDDEN,
    INTERNAL_SERVER_ERROR,
    NOT_FOUND,
    OK,
    UNAUTHORIZED,
)
import os
from typing import Final, List
from unittest import mock
import pytest
from requests import Response
from app.pressure import PressureRepositoryImpl, PressureRepository, Pressure


def test_OpenweatherAPIの呼び出し失敗_400エラー(mocker):
    # 事前準備：呼び出し用のモック作成

    repository: PressureRepository = PressureRepositoryImpl()
    response_mock = mock.Mock(spec=Response)
    response_mock.status_code = BAD_REQUEST

    mocker.patch.object(
        repository,
        "call_openweather_api",
        return_value=response_mock,
    )

    with pytest.raises(RuntimeError) as e:
        repository.get_daily_pressure()

    assert str(e.value) == "パラメータが不正です。"


def test_OpenweatherAPIの呼び出し失敗_404エラー(mocker):
    # 事前準備：呼び出し用のモック作成

    repository: PressureRepository = PressureRepositoryImpl()
    response_mock = mock.Mock(spec=Response)
    response_mock.status_code = NOT_FOUND

    mocker.patch.object(
        repository,
        "call_openweather_api",
        return_value=response_mock,
    )

    with pytest.raises(RuntimeError) as e:
        repository.get_daily_pressure()

    assert str(e.value) == "リクエスト先URLが存在しません。"


def test_OpenweatherAPIの呼び出し失敗_403エラー(mocker):
    # 事前準備：呼び出し用のモック作成

    repository: PressureRepository = PressureRepositoryImpl()
    response_mock = mock.Mock(spec=Response)
    response_mock.status_code = FORBIDDEN

    mocker.patch.object(
        repository,
        "call_openweather_api",
        return_value=response_mock,
    )

    with pytest.raises(RuntimeError) as e:
        repository.get_daily_pressure()

    assert str(e.value) == "認証に失敗しました。"


def test_OpenweatherAPIの呼び出し失敗_401エラー(mocker):
    # 事前準備：呼び出し用のモック作成

    repository: PressureRepository = PressureRepositoryImpl()
    response_mock = mock.Mock(spec=Response)
    response_mock.status_code = UNAUTHORIZED

    mocker.patch.object(
        repository,
        "call_openweather_api",
        return_value=response_mock,
    )

    with pytest.raises(RuntimeError) as e:
        repository.get_daily_pressure()

    assert str(e.value) == "認証情報が不正です。"


def test_OpenweatherAPIの呼び出し失敗_500エラー(mocker):
    # 事前準備：呼び出し用のモック作成

    repository: PressureRepository = PressureRepositoryImpl()
    response_mock = mock.Mock(spec=Response)
    response_mock.status_code = INTERNAL_SERVER_ERROR

    mocker.patch.object(
        repository,
        "call_openweather_api",
        return_value=response_mock,
    )

    with pytest.raises(RuntimeError) as e:
        repository.get_daily_pressure()

    assert str(e.value) == "OpenWeatherAPIの不具合です。"


def test_OpenweatherAPIの呼び出し成功():
    # 事前準備： 明日の午前6時と21時を定義する
    # 0分が取得されるので、現在時刻は0分とする

    tommorw_AM0600: datetime = datetime.today().replace(
        hour=0, minute=0, second=0, microsecond=0
    ) + timedelta(days=1, hours=6)

    tomorrow_PM2100: datetime = datetime.today().replace(
        hour=0, minute=0, second=0, microsecond=0
    ) + timedelta(days=1, hours=21)
    respository: PressureRepository = PressureRepositoryImpl()

    # 操作： OpenweatherAPIを呼び出し
    response: Final[List[Pressure]] = respository.get_daily_pressure()

    # 想定結果： listが取得される
    assert isinstance(response, list)

    # 現在時刻 ~ 48時間後まで取得される
    assert response[0].datetime == tommorw_AM0600
    assert response[-1].datetime == tomorrow_PM2100
    assert len(response) == 6
