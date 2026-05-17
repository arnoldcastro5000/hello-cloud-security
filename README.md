# hello-cloud-security

A portfolio starter project demonstrating a production-ready Python project structure for cloud security tooling.

## Project Structure

```
hello-cloud-security/
├── hello_cloud_security/   # Application package
│   ├── __init__.py
│   └── app.py              # Core logic and entry point
├── tests/
│   └── test_app.py
├── pyproject.toml
├── requirements.txt
├── requirements-dev.txt
└── .gitignore
```

## Getting Started

### Prerequisites

- Python 3.11+
- `pip`

### Setup

```bash
# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install runtime dependencies
pip install -r requirements.txt

# Install dev dependencies (includes pytest)
pip install -r requirements-dev.txt
```

### Configuration

Copy `.env.example` to `.env` and set values as needed:

```bash
APP_ENV=local   # local | staging | production
```

### Run

```bash
python -m hello_cloud_security.app
```

Or, after installing the package:

```bash
pip install -e .
hello-cloud-security
```

### Test

```bash
pytest
pytest --cov=hello_cloud_security   # with coverage
```

## License

MIT
