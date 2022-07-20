from http.client import OK
from urllib import response
import pytest
from requests import Response
from app.pressure import PressureRepositoryImpl


def test_リクエストが成功():
    response: Response = Response()
    response.status_code = OK

    assert not PressureRepositoryImpl.request_fail(response)


@pytest.mark.parametrize("status", [400, 404, 403, 500])
def test_リクエストが失敗(status: int):
    response: Response = Response()
    response.status_code = status

    assert PressureRepositoryImpl.request_fail(response)
