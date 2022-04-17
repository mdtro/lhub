import pytest
from lhub.api import LogicHubAPI
from lhub.exceptions.validation import VersionMinimumNotMet


def test_minimum_version_raises_when_not_met(monkeypatch):
    @property
    def mock_version(*args, **kwargs):
        return "m1.1"

    hostname = "testhostname"
    lhub_api = LogicHubAPI(
        hostname=hostname,
        api_key="dummykey123456",
        init_version="m1.1"
    )

    monkeypatch.setattr(LogicHubAPI, "version", mock_version)

    with pytest.raises(VersionMinimumNotMet):
        _ = lhub_api.system_field_lh_linked_alerts()


def test_minimum_version_does_not_raise_when_met(monkeypatch):
    @property
    def mock_version(*args, **kwargs):
        return "m99999.0"

    test_linked_alert = {
        "fieldName": "lh_linked_alerts",
        "foo": "bar"
    }

    def mock_list_fields(*args, **kwargs):
        # I'm not sure what is expected to be returned here?
        return [
            test_linked_alert
        ]

    hostname = "testhostname"
    lhub_api = LogicHubAPI(
        hostname=hostname,
        api_key="dummykey123456",
        init_version="m99999.0"
    )

    monkeypatch.setattr(LogicHubAPI, "version", mock_version)
    monkeypatch.setattr(LogicHubAPI, "fields", mock_list_fields)

    assert test_linked_alert == lhub_api.system_field_lh_linked_alerts
