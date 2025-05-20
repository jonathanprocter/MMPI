"""
Main application file for the MMPI-2 Assessment Platform web application.
This file is configured for deployment with proper host and port settings.
"""

from webapp import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
