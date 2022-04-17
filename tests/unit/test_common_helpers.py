import pytest
import lhub.common.helpers as helpers
import lhub.exceptions as exceptions


def test_format_alert_id_str_to_int():
    alert_id = helpers.format_alert_id("123")
    assert 123 == alert_id
    assert type(alert_id) == int


@pytest.mark.xfail(reason = "Should this function accept floats?")
def test_format_alert_id_float_to_int():
    alert_id = helpers.format_alert_id(1.9)
    assert 1.9 == alert_id


def test_format_str_case_id_with_prefix():
    case_prefix = "testprefix"
    case_id = "12345"

    formatted_case_id = helpers.format_case_id_with_prefix(
        case_id,
        case_prefix
    )

    assert f"{case_prefix}-{case_id}" == formatted_case_id


def test_format_non_num_str_case_id_raises_invalid_format():
    case_id = "NotANumber"

    with pytest.raises(exceptions.formatting.InvalidCaseIdFormat):
        _ = helpers.format_case_id(case_id)


@pytest.mark.xfail(reason="Should this function accept floats?")
def test_format_notebook_id():
    notebook_id = 1.23
    assert 1.23 == helpers.format_notebook_id(notebook_id)


def test_format_notebook_id_as_str():
    notebook_id = "123"
    assert 123 == helpers.format_notebook_id(notebook_id)


def test_format_notebook_id_as_nan_str_raises_invalid_format():
    notebook_id = "NotANumber"

    with pytest.raises(exceptions.formatting.InvalidNotebookIdFormat):
        _ = helpers.format_notebook_id(notebook_id)


def test_format_notebook_id_as_dict_returns_expected_id():
    notebook_dict = {
        "key": "notebook",
        "id": "12345"
    }

    assert 12345 == helpers.format_notebook_id(notebook_dict)


@pytest.mark.xfail(reason="Should the nested dict work here?")
def test_format_notebook_id_as_nested_dict():
    notebook_dict = {
        "id": {
            "key": "notebook",
            "id": "12345"
        }
    }
    assert 12345 == helpers.format_notebook_id(notebook_dict)


def test_format_notebook_id_dict_wo_id_raises():
    notebook_dict = {
        "foo": "bar"
    }

    with pytest.raises(exceptions.formatting.InvalidNotebookIdFormat):
        _ = helpers.format_notebook_id(notebook_dict)

