# lhub
Python package for interacting with LogicHub APIs

## Running Tests

1. Make sure you have the _dev_ dependencies installed: `pip install -r requirements-dev.txt`
2. Run tests with: `pytest -vv`
   - Generate an HTML coverage report with: `pytest -vv --cov . --cov-report=html`
   - Then open the interactive report with: `open htmlcov/index.html`


# Version History
### 0.0.8
* LogicHubAPI.get_batches_by_stream_id: Added support for a limit of -1 in order to set it to unlimited
* LogicHub.action_get_batches_by_stream_id: Set the default limit to unlimited
