# MMPI-2 Assessment Platform

This repository contains a Flask-based web application for administering, scoring and interpreting MMPI-2 assessments. It produces personalized narrative reports and professional profile graphs in multiple formats.

## Features
- Personalized narratives that use the client's name while keeping sex-specific scoring and interpretation.
- Full names for all Restructured Clinical (RC) scales.
- Graphical representations, including the traditional profile and scale family graphs for Clinical, Content, RC, PSY-5 and Supplementary scales.
- Comprehensive psychological reports with diagnostic impressions, differential diagnoses and treatment recommendations.
- Output formats include HTML, PDF, TXT and JSON.

## Setup
1. Ensure Python 3.8 or newer is installed.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Running the Application
To start the development server run:
```
python webapp.py
```
The application will be available at [http://localhost:5000](http://localhost:5000).

### Deployment
For production or containerized deployment you can use the simplified entry point:
```
python app.py
```
This runs the Flask application on `0.0.0.0:8080`. You may also serve `webapp:app` with a WSGI server such as Gunicorn.

## Using the Application
1. Enter client information (name, age, sex, etc.).
2. Manually input T-scores for the desired scales.
3. Generate the comprehensive report and download it in your preferred format.

## Limitations
- The repository does **not** include the official MMPI questionnaire items or any raw response data.
- All T-scores must be entered manually.

## File Structure
- `webapp.py` – main Flask application.
- `app.py` – deployment entry point.
- `src/` – core modules with constants, interpretation logic, models and report generation.
- `templates/` – HTML templates for the web interface.
- `static/` – CSS, JavaScript and other static files.
- `reports/` and `uploads/` – created at runtime for generated reports and uploaded files.

## Sample Data
The repository includes sample data for male and female clients with identical T-scores to demonstrate sex-specific narrative differences.

## License
For educational and clinical use only.
