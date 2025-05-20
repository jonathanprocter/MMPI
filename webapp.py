"""
Web Application for MMPI-2 Assessment Platform

This module provides a Flask-based web application for the MMPI-2 assessment platform,
allowing users to input client information, enter assessment scores, and generate
comprehensive psychological reports with personalized narratives and professional graphics.
"""

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, jsonify, session
import os
import json
import uuid
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import numpy as np
from datetime import datetime

from src.reporting.comprehensive_report_generator import ComprehensiveReportGenerator
from src.reporting.profile_graph_generator import ProfileGraphGenerator
from src.constants.scale_constants import (
    VALIDITY_SCALES_MAP, CLINICAL_SCALES_MAP, HARRIS_LINGOES_SUBSCALES_MAP,
    CONTENT_SCALES_MAP, RC_SCALES_MAP, PSY5_SCALES_MAP, SUPPLEMENTARY_SCALES_MAP
)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['REPORT_FOLDER'] = 'reports'

# Ensure upload and report directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['REPORT_FOLDER'], exist_ok=True)

# RC Scale full names mapping
RC_SCALES_FULL_NAMES = {
    'RCd': 'Demoralization',
    'RC1': 'Somatic Complaints',
    'RC2': 'Low Positive Emotions',
    'RC3': 'Cynicism',
    'RC4': 'Antisocial Behavior',
    'RC6': 'Ideas of Persecution',
    'RC7': 'Dysfunctional Negative Emotions',
    'RC8': 'Aberrant Experiences',
    'RC9': 'Hypomanic Activation'
}

@app.route('/')
def index():
    """Render the home page."""
    return render_template('index.html')

@app.route('/client_info', methods=['GET', 'POST'])
def client_info():
    """Handle client information input."""
    if request.method == 'POST':
        # Store client info in session
        session['client_info'] = {
            'name': request.form.get('name', ''),
            'age': request.form.get('age', ''),
            'sex': request.form.get('sex', 'female'),
            'date': request.form.get('date', datetime.now().strftime('%Y-%m-%d')),
            'referral_source': request.form.get('referral_source', ''),
            'reason_for_referral': request.form.get('reason_for_referral', '')
        }
        return redirect(url_for('score_entry'))
    
    return render_template('client_info.html')

@app.route('/score_entry', methods=['GET', 'POST'])
def score_entry():
    """Handle MMPI-2 score entry."""
    if request.method == 'POST':
        # Process and store scores in session
        validity_scales = {}
        for scale in VALIDITY_SCALES_MAP.keys():
            if scale in request.form:
                try:
                    validity_scales[scale] = int(request.form[scale])
                except ValueError:
                    validity_scales[scale] = 50  # Default value
        
        clinical_scales = {}
        for scale in CLINICAL_SCALES_MAP.keys():
            if scale in request.form:
                try:
                    clinical_scales[scale] = int(request.form[scale])
                except ValueError:
                    clinical_scales[scale] = 50  # Default value
        
        harris_lingoes_subscales = {}
        for scale in HARRIS_LINGOES_SUBSCALES_MAP.keys():
            if scale in request.form:
                try:
                    harris_lingoes_subscales[scale] = int(request.form[scale])
                except ValueError:
                    harris_lingoes_subscales[scale] = 50  # Default value
        
        content_scales = {}
        for scale in CONTENT_SCALES_MAP.keys():
            if scale in request.form:
                try:
                    content_scales[scale] = int(request.form[scale])
                except ValueError:
                    content_scales[scale] = 50  # Default value
        
        rc_scales = {}
        for scale in RC_SCALES_MAP.keys():
            if scale in request.form:
                try:
                    rc_scales[scale] = int(request.form[scale])
                except ValueError:
                    rc_scales[scale] = 50  # Default value
        
        psy5_scales = {}
        for scale in PSY5_SCALES_MAP.keys():
            if scale in request.form:
                try:
                    psy5_scales[scale] = int(request.form[scale])
                except ValueError:
                    psy5_scales[scale] = 50  # Default value
        
        supplementary_scales = {}
        for scale in SUPPLEMENTARY_SCALES_MAP.keys():
            if scale in request.form:
                try:
                    supplementary_scales[scale] = int(request.form[scale])
                except ValueError:
                    supplementary_scales[scale] = 50  # Default value
        
        # Store all scores in session
        session['scores'] = {
            'validity_scales': validity_scales,
            'clinical_scales': clinical_scales,
            'harris_lingoes_subscales': harris_lingoes_subscales,
            'content_scales': content_scales,
            'rc_scales': rc_scales,
            'psy5_scales': psy5_scales,
            'supplementary_scales': supplementary_scales
        }
        
        # Generate report
        return redirect(url_for('generate_report'))
    
    # Prepare scale maps for the template
    scale_maps = {
        'validity_scales_map': VALIDITY_SCALES_MAP,
        'clinical_scales_map': CLINICAL_SCALES_MAP,
        'harris_lingoes_subscales_map': HARRIS_LINGOES_SUBSCALES_MAP,
        'content_scales_map': CONTENT_SCALES_MAP,
        'rc_scales_map': RC_SCALES_MAP,
        'rc_scales_full_names': RC_SCALES_FULL_NAMES,
        'psy5_scales_map': PSY5_SCALES_MAP,
        'supplementary_scales_map': SUPPLEMENTARY_SCALES_MAP
    }
    
    return render_template('score_entry.html', **scale_maps)

@app.route('/generate_report', methods=['GET'])
def generate_report():
    """Generate comprehensive MMPI-2 report."""
    # Check if client info and scores are in session
    if 'client_info' not in session or 'scores' not in session:
        return redirect(url_for('index'))
    
    # Create unique report directory
    report_id = str(uuid.uuid4())
    report_dir = os.path.join(app.config['REPORT_FOLDER'], report_id)
    os.makedirs(report_dir, exist_ok=True)
    
    # Generate report
    report_generator = ComprehensiveReportGenerator(output_dir=report_dir)
    report_data = report_generator.generate_report(session['scores'], session['client_info'])
    
    # Generate profile graphs
    graph_generator = ProfileGraphGenerator(output_dir=report_dir)
    graph_paths = graph_generator.generate_all_graphs(session['scores'], session['client_info'])
    
    # Store report ID in session
    session['report_id'] = report_id
    
    return redirect(url_for('view_report', report_id=report_id))

@app.route('/view_report/<report_id>', methods=['GET'])
def view_report(report_id):
    """View generated report."""
    report_dir = os.path.join(app.config['REPORT_FOLDER'], report_id)
    
    # Check if report exists
    if not os.path.exists(report_dir):
        return redirect(url_for('index'))
    
    # Get paths to report files
    html_path = os.path.join(report_dir, 'comprehensive_report.html')
    pdf_path = os.path.join(report_dir, 'comprehensive_report.pdf')
    traditional_graph_path = os.path.join(report_dir, 'traditional_profile_graph.png')
    
    # Check if files exist
    html_exists = os.path.exists(html_path)
    pdf_exists = os.path.exists(pdf_path)
    graph_exists = os.path.exists(traditional_graph_path)
    
    return render_template('view_report.html', 
                          report_id=report_id,
                          html_exists=html_exists,
                          pdf_exists=pdf_exists,
                          graph_exists=graph_exists)

@app.route('/reports/<report_id>/<filename>', methods=['GET'])
def report_file(report_id, filename):
    """Serve report files."""
    report_dir = os.path.join(app.config['REPORT_FOLDER'], report_id)
    return send_from_directory(report_dir, filename)

# Serve the original MMPI questionnaire page
@app.route('/mmpi_test', methods=['GET'])
def mmpi_test():
    """Serve the legacy MMPI HTML questionnaire."""
    return send_from_directory('.', 'mmpi copy.html')

@app.route('/sample_data', methods=['GET'])
def sample_data():
    """Load sample data for demonstration."""
    # Sample client info
    session['client_info'] = {
        'name': 'John Smith',
        'age': '35',
        'sex': 'male',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'referral_source': 'Dr. Jane Doe',
        'reason_for_referral': 'Diagnostic clarification and treatment planning'
    }
    
    # Sample scores based on provided screenshots
    session['scores'] = {
        'validity_scales': {
            'L': 45, 'F': 51, 'K': 51, 'VRIN': 73, 'TRIN': 57, 'Fb': 51, 'Fp': 56, 'FBS': 43, 'S': 34
        },
        'clinical_scales': {
            'L': 45, 'F': 51, 'K': 51, '1': 51, '2': 51, '3': 51, '4': 68, '5': 62, '6': 53, '7': 44, '8': 56, '9': 56, '0': 44
        },
        'content_scales': {
            'ANX': 62, 'FRS': 67, 'OBS': 53, 'DEP': 55, 'HEA': 56, 'BIZ': 57, 'ANG': 63, 'CYN': 56, 'ASP': 53, 'TPA': 60, 'LSE': 53, 'SOD': 49, 'FAM': 66, 'WRK': 61, 'TRT': 56
        },
        'rc_scales': {
            'RCd': 54, 'RC1': 63, 'RC2': 46, 'RC3': 56, 'RC4': 71, 'RC6': 62, 'RC7': 52, 'RC8': 59, 'RC9': 61
        },
        'psy5_scales': {
            'AGGR': 74, 'PSYC': 49, 'DISC': 51, 'NEGE': 64, 'INTR': 43
        },
        'supplementary_scales': {
            'A': 51, 'R': 36, 'Es': 38, 'Do': 38, 'Re': 37, 'Mt': 57, 'PK': 58, 'MDS': 69, 'Ho': 58, 'O-H': 45, 'MAC-R': 55, 'APS': 65, 'GM': 41, 'GF': 30
        },
        'harris_lingoes_subscales': {
            'D1': 54, 'D2': 50, 'D3': 52, 'D4': 48, 'D5': 56,
            'Hy1': 52, 'Hy2': 48, 'Hy3': 54, 'Hy4': 50, 'Hy5': 49,
            'Pd1': 65, 'Pd2': 58, 'Pd3': 52, 'Pd4': 60, 'Pd5': 55,
            'Pa1': 54, 'Pa2': 52, 'Pa3': 50,
            'Sc1': 58, 'Sc2': 55, 'Sc3': 52, 'Sc4': 54, 'Sc5': 56, 'Sc6': 53,
            'Ma1': 58, 'Ma2': 54, 'Ma3': 52, 'Ma4': 50
        }
    }
    
    return redirect(url_for('generate_report'))

@app.route('/female_sample_data', methods=['GET'])
def female_sample_data():
    """Load female sample data for demonstration."""
    # Sample client info
    session['client_info'] = {
        'name': 'Jane Smith',
        'age': '35',
        'sex': 'female',
        'date': datetime.now().strftime('%Y-%m-%d'),
        'referral_source': 'Dr. John Doe',
        'reason_for_referral': 'Diagnostic clarification and treatment planning'
    }
    
    # Sample scores based on provided screenshots (same T-scores as male sample)
    session['scores'] = {
        'validity_scales': {
            'L': 45, 'F': 51, 'K': 51, 'VRIN': 73, 'TRIN': 57, 'Fb': 51, 'Fp': 56, 'FBS': 43, 'S': 34
        },
        'clinical_scales': {
            'L': 45, 'F': 51, 'K': 51, '1': 51, '2': 51, '3': 51, '4': 68, '5': 62, '6': 53, '7': 44, '8': 56, '9': 56, '0': 44
        },
        'content_scales': {
            'ANX': 62, 'FRS': 67, 'OBS': 53, 'DEP': 55, 'HEA': 56, 'BIZ': 57, 'ANG': 63, 'CYN': 56, 'ASP': 53, 'TPA': 60, 'LSE': 53, 'SOD': 49, 'FAM': 66, 'WRK': 61, 'TRT': 56
        },
        'rc_scales': {
            'RCd': 54, 'RC1': 63, 'RC2': 46, 'RC3': 56, 'RC4': 71, 'RC6': 62, 'RC7': 52, 'RC8': 59, 'RC9': 61
        },
        'psy5_scales': {
            'AGGR': 74, 'PSYC': 49, 'DISC': 51, 'NEGE': 64, 'INTR': 43
        },
        'supplementary_scales': {
            'A': 51, 'R': 36, 'Es': 38, 'Do': 38, 'Re': 37, 'Mt': 57, 'PK': 58, 'MDS': 69, 'Ho': 58, 'O-H': 45, 'MAC-R': 55, 'APS': 65, 'GM': 41, 'GF': 30
        },
        'harris_lingoes_subscales': {
            'D1': 54, 'D2': 50, 'D3': 52, 'D4': 48, 'D5': 56,
            'Hy1': 52, 'Hy2': 48, 'Hy3': 54, 'Hy4': 50, 'Hy5': 49,
            'Pd1': 65, 'Pd2': 58, 'Pd3': 52, 'Pd4': 60, 'Pd5': 55,
            'Pa1': 54, 'Pa2': 52, 'Pa3': 50,
            'Sc1': 58, 'Sc2': 55, 'Sc3': 52, 'Sc4': 54, 'Sc5': 56, 'Sc6': 53,
            'Ma1': 58, 'Ma2': 54, 'Ma3': 52, 'Ma4': 50
        }
    }
    
    return redirect(url_for('generate_report'))

@app.route('/clear_session', methods=['GET'])
def clear_session():
    """Clear session data."""
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
