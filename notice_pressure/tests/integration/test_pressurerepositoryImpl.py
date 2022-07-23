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
from typing import List
from unittest import mock
import pytest
from requests import Response
from app.pressure import PressureRepositoryImpl, PressureRepository


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
        repository.get_tomorrow_list()

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
        repository.get_tomorrow_list()

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
        repository.get_tomorrow_list()

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
        repository.get_tomorrow_list()

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
        repository.get_tomorrow_list()

    assert str(e.value) == "OpenWeatherAPIの不具合です。"


def test_OpenweatherAPIの呼び出し成功():
    # 事前準備： 現在時刻と48時間後の時刻(時まで)を定義
    # 0分が取得されるので、現在時刻は0分とする
    now: str = datetime.now().strftime("%Y%m%d%H00")

    two_days_later: str = (datetime.now() + timedelta(hours=47)).strftime("%Y%m%d%H00")

    respository: PressureRepository = PressureRepositoryImpl()

    # 操作： OpenweatherAPIを呼び出し
    response: list = respository.get_tomorrow_list()

    # 想定結果： listが取得される
    assert isinstance(response, list)

    # 現在時刻 ~ 48時間後まで取得される
    assert response[0]["dt"] == now
    assert response[-1]["dt"] == two_days_later
    assert len(response) == 48
