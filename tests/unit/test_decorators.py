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