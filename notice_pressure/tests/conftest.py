import os
import sys
import pytest
from app import create_app


@pytest.fixture(scope="session", autouse=True)
def set_config():
    os.environ["FLASK_CONFIG"] = "/usr/local/project/notice_pressure/config/test.py"
    app = create_app()
    app.app_context().push()
