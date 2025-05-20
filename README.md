# MMPI Assessment Platform

This repository contains a Flask-based web application for generating MMPI-2 reports.

## Setup

1. Install the required dependencies from `requirements.txt`.
   ```bash
   pip install -r requirements.txt
   ```
2. Run the application using the provided `app.py` or via a WSGI server with `wsgi.py`.
   ```bash
   python app.py
   ```
   or
   ```bash
   gunicorn wsgi:application
   ```

## Tests

A minimal test suite is located under `tests/`. Execute it with:

```bash
python -m pytest -q
```

Note: The test runner is a small built-in stub so external dependencies are not required, but the real Flask package must be installed for the tests to run.
