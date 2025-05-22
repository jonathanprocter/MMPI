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

## Deployment

This application is designed to be deployed using Docker, which packages the application and all its dependencies into a container.

### Using Docker

1.  **Build the Docker Image**:
    Navigate to the root directory of the project (where the `Dockerfile` is located) and run:
    ```bash
    docker build -t mmpi-app .
    ```
    This will build a Docker image tagged as `mmpi-app`.

2.  **Run the Docker Container**:
    Once the image is built, you can run it as a container:
    ```bash
    docker run -p 8080:8080 -e SECRET_KEY='your_very_strong_and_unique_secret_key' mmpi-app
    ```
    Breakdown of the command:
    *   `-p 8080:8080`: Maps port 8080 from your host machine to port 8080 in the container (where Gunicorn is running). You can change the host port if needed (e.g., `-p 5000:8080`).
    *   `-e SECRET_KEY='your_very_strong_and_unique_secret_key'`: Sets the `SECRET_KEY` environment variable inside the container. **Important:** Replace `'your_very_strong_and_unique_secret_key'` with a strong, unique secret key for your production deployment.
    *   `mmpi-app`: The name of the Docker image to run.

    The application should then be accessible at `http://localhost:8080` (or whichever host port you used).

### Hosting the Application

To deploy this application on the web, you will need a hosting service that can run Docker containers. Some options include:

*   **Platform as a Service (PaaS)**: Heroku (using Docker deploy), Google Cloud Run, AWS Elastic Beanstalk, Azure App Service.
*   **Virtual Private Server (VPS)**: DigitalOcean, Linode, AWS EC2. You would install Docker on the VPS and run the container.
*   **Managed Kubernetes Services**: Google Kubernetes Engine (GKE), Amazon EKS, Azure Kubernetes Service (AKS).

### Note on GitHub Pages

GitHub Pages is designed for hosting **static websites** (HTML, CSS, JavaScript files). It cannot run Python web applications like this Flask app directly.

If you wish to use GitHub Pages, you would typically:
*   Deploy the dynamic Python Flask application to a suitable hosting service (as mentioned above).
*   Optionally, use GitHub Pages for a related static landing page, documentation, or a version of the questionnaire that communicates with the separately hosted backend via APIs (though this application is not currently structured for that kind of split). The existing `mmpi_copy.html` could be served via GitHub Pages as a static page, but it wouldn't have the Python backend functionality.
