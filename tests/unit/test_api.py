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


def test_expected_default_http_headers_with_apikey():
    hostname = "testhostname"
    lhub_api = LogicHubAPI(
        hostname=hostname,
        api_key="dummykey123456",
        init_version="m1.2"

    )

    headers = lhub_api.default_http_headers
    assert "User-Agent" in headers, "Missing 'User-Agent' header in default headers"
    assert "X-Auth-Token" in headers, "Missing 'X-Auth-Token' header in default headers (used with API key auth)"


def test_raises_exception_on_session_cookie_with_apikey():
    hostname = "testhostname"
    lhub_api = LogicHubAPI(
        hostname=hostname,
        api_key="dummykey123456",
        init_version="m1.2"

    )

    with pytest.raises(exceptions.LhBaseException):
        _cookie = lhub_api.session_cookie