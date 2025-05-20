# MMPI-2 Assessment Platform Web Application

This document provides an overview of the Flask application included in this repository. The app allows entry of MMPI-2 scores, generates narrative interpretations and produces profile graphs.

## Features

1. **Personalized narrative interpretations** that reference the client's name while respecting sex-specific scoring.
2. **Full RC scale names** displayed throughout the interface.
3. **Professional graphical profiles** including traditional and scale-family graphs.
4. **Comprehensive reports** available in HTML and PDF formats.

## Usage

Install the dependencies and run the application:

```bash
pip install -r requirements.txt
python app.py
```

Browse to `http://localhost:8080` and follow the prompts to enter client information and scale scores. Generated reports are stored under the `reports/` directory.

## Directory Layout

```
src/
    constants/            # Numeric constants and scale definitions
    interpretation/       # Interpretation logic for each scale family
    models/               # Database models
    reporting/            # Report and graph generation utilities
templates/                # Flask Jinja2 templates
```

Additional sample reports (`*.html`, `*.pdf`, `*.txt`) are provided for reference and are not required to run the application.
