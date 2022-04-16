import pytest

from lhub.api import LogicHubAPI
from lhub import exceptions


def test_verify_ssl_true_as_default(monkeypatch):
    def mock_api_version():
        return 999

    monkeypatch.setattr(LogicHubAPI, "version", mock_api_version)

    hostname = "testhostname"
    lhub_api = LogicHubAPI(
        hostname=hostname,
        api_key="dummykey123456"
    )
    assert lhub_api.verify_ssl is True


def test_apikey_and_password_raises_exception(monkeypatch):
    def mock_api_version():
        return 999

    monkeypatch.setattr(LogicHubAPI, "version", mock_api_version)

    hostname = "testhostname"

    with pytest.raises(exceptions.validation.InputValidationError):
        _lhub_api = LogicHubAPI(
            hostname=hostname,
            api_key="123456",
            password="123456password123456"
        )


def test_password_without_username_raises_exception(monkeypatch):
    def mock_api_version():
        return 999

    monkeypatch.setattr(LogicHubAPI, "version", mock_api_version)

    hostname = "testhostname"

    with pytest.raises(exceptions.validation.InputValidationError):
        _lhub_api = LogicHubAPI(
            hostname=hostname,
            password="123456password123456"
        )

