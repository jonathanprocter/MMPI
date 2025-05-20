"""
README for MMPI-2 Assessment Platform Web Application

This web application provides a comprehensive platform for administering, scoring, and interpreting MMPI-2 assessments with personalized narratives and professional graphical representations.

## Features

1. **Personalized Narrative Interpretations**
   - Uses client's name instead of generic "this man" or "this woman" references
   - Maintains sex-specific scoring and interpretation logic
   - Provides comprehensive narratives for all scale families

2. **Full RC Scale Names**
   - Includes complete names for all Restructured Clinical (RC) scales
   - RCd: Demoralization
   - RC1: Somatic Complaints
   - RC2: Low Positive Emotions
   - RC3: Cynicism
   - RC4: Antisocial Behavior
   - RC6: Ideas of Persecution
   - RC7: Dysfunctional Negative Emotions
   - RC8: Aberrant Experiences
   - RC9: Hypomanic Activation

3. **Professional Graphical Representations**
   - Traditional MMPI-2 profile visualization
   - Scale family graphs (Clinical, Content, RC, PSY-5, Supplementary)
   - Clinical significance indicators with proper formatting
   - Raw score and T-score displays

4. **Comprehensive Psychological Reports**
   - Detailed narrative interpretations for all scales
   - Diagnostic impressions based on assessment results
   - Differential diagnoses considerations
   - Treatment recommendations
   - Multi-format output (HTML, PDF, TXT, JSON)

## Installation and Usage

1. **Requirements**
   - Python 3.8+
   - Flask
   - Matplotlib
   - NumPy
   - Other dependencies in requirements.txt

2. **Setup**
   ```
   pip install -r requirements.txt
   ```

3. **Running the Application**
   ```
   python webapp.py
   ```
   The application will be available at http://localhost:5000

4. **Using the Application**
   - Enter client information (name, age, sex, etc.)
   - Input T-scores for all relevant scales
   - Alternatively, open the legacy questionnaire via `/mmpi_test` to complete
     the full MMPI-2 in your browser
   - Generate comprehensive report
   - View and download reports in multiple formats

## File Structure

- `webapp.py` - Main Flask application
- `src/` - Core modules
  - `constants/` - Scale definitions and constants
  - `interpretation/` - Scale interpretation modules
  - `models/` - Data models
  - `reporting/` - Report generation modules
- `templates/` - HTML templates for web interface
- `static/` - CSS, JavaScript, and other static files
- `reports/` - Generated reports (created at runtime)
- `uploads/` - Uploaded files (created at runtime)

## Sample Data

The application includes sample data for both male and female profiles with identical T-scores to demonstrate sex-specific narrative differences while maintaining clinical accuracy.

## License

For educational and clinical use only.
"""
