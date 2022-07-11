import os
import sys
import pytest
from app import create_app

@pytest.fixture(scope='session', autouse=True)
def set_config():
    # GitHubActionsでエラーにならないように相対パスを使用
    os.environ["FLASK_CONFIG"] = "True"
    app = create_app()
    app.app_context().push()