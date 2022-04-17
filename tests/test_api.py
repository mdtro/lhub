import pytest

from lhub.api import LogicHubAPI
from lhub import exceptions


def test_invalid_version_pattern_raises_exception():
    hostname = "testhostname"
    with pytest.raises(exceptions.formatting.InvalidVersionFormat):
        _lhub_api = LogicHubAPI(
            hostname=hostname,
            api_key="123456",
            init_version="999999999"
        )


def test_verify_ssl_true_as_default():
    hostname = "testhostname"
    lhub_api = LogicHubAPI(
        hostname=hostname,
        api_key="dummykey123456",
        init_version="m1.2"

    )
    assert lhub_api.verify_ssl is True


def test_apikey_and_password_raises_exception():
    hostname = "testhostname"
    with pytest.raises(exceptions.validation.InputValidationError):
        _lhub_api = LogicHubAPI(
            hostname=hostname,
            api_key="123456",
            password="123456password123456",
            init_version="m1.2"
        )


def test_password_without_username_raises_exception():
    hostname = "testhostname"
    with pytest.raises(exceptions.validation.InputValidationError):
        _lhub_api = LogicHubAPI(
            hostname=hostname,
            password="123456password123456",
            init_version="m1.2"
        )

