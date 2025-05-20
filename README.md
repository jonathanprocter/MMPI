# MMPI-2 Assessment Platform

This repository contains a Flask-based prototype for administering the Minnesota Multiphasic Personality Inventory–2 (MMPI-2) and generating narrative reports with accompanying profile graphs.

## Installation

1. Ensure Python 3.8+ is installed.
2. (Optional) Create and activate a virtual environment.
3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Run the Flask application using the helper script:

```bash
python app.py
```

The application will start on port `8080` and can be accessed at `http://localhost:8080`.

Reports and uploads are saved in the `reports/` and `uploads/` folders which are created automatically at runtime.

## Project Structure

```
.
├── app.py                # Entry point that runs the Flask app
├── webapp.py             # Core Flask routes and logic
├── src/                  # Application modules
│   ├── constants/        # Scale definitions and other constants
│   ├── interpretation/   # Scale interpretation code
│   ├── models/           # SQLAlchemy models
│   └── reporting/        # Report generation utilities
├── templates/            # HTML templates for the web interface
├── requirements.txt      # Python dependencies
└── ...                   # Sample reports and documentation
```

The repository also contains example PDF and HTML reports produced by the generator for reference.
