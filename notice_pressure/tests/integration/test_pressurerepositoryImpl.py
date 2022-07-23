from datetime import datetime, timedelta
from http.client import OK
import os
from time import strftime, strptime, time
from typing import List
import pytest
from requests import Response
from app.pressure import PressureRepositoryImpl, PressureRepository


def test_リクエストが成功():
    response: Response = Response()
    response.status_code = OK

    assert not PressureRepositoryImpl.request_fail(response)


@pytest.mark.parametrize("status", [400, 404, 403, 500])
def test_リクエストが失敗(status: int):
    response: Response = Response()
    response.status_code = status

    assert PressureRepositoryImpl.request_fail(response)


@pytest.mark.parametrize("response_status_code", [400, 404, 403, 500, 503])
def test_OpenweatherAPIの呼び出し失敗(response_status_code: int, mocker):
    # 事前準備：呼び出し用のモック作成

    repository: PressureRepository = PressureRepositoryImpl()

    mocker.patch.object(repository, "request_fail", return_value=response_status_code)

    with pytest.raises(RuntimeError) as e:
        repository.get_tomorrow_list()

    assert str(e.value) == "気圧情報の取得に失敗しました。"


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
