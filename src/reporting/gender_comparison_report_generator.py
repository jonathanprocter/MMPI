Script to generate comparative MMPI-2 reports for male and female profiles with identical T-scores.

This script demonstrates how the MMPI-2 platform generates sex-specific narratives
for identical T-score profiles.
"""

import os
import sys
import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from weasyprint import HTML
from src.models.models import Score
from src.reporting.report_generator import generate_report_text, generate_report_html
from src.constants.scale_constants import (
    VALIDITY_SCALES, CLINICAL_SCALES, CONTENT_SCALES, 
    RC_SCALES, SUPPLEMENTARY_SCALES, PSY5_SCALES
)
from src.interpretation.scale_interpretations import get_scale_interpretation

# Ensure output directory exists
OUTPUT_DIR = "gender_comparison_output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define a sample profile with clinically significant elevations
def create_sample_profile(gender):
    """Create a sample profile with identical T-scores but different gender."""
    
    # Basic demographic information
    demographics = {
        "id": f"SAMPLE_{gender.upper()}",
        "age": 35,
        "sex": gender,
        "education": "College Degree",
        "occupation": "Professional",
        "marital_status": "Married",
        "referral_source": "Self-referred",
        "notes": f"Sample {gender} profile with identical T-scores to demonstrate sex-specific narratives",
        "test_started_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "test_completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    # Create identical T-scores for both genders to demonstrate narrative differences
    scores = {
        # Validity Scales
        "VRIN": 55,
        "TRIN": 57,
        "F": 68,
        "Fb": 65,
        "Fp": 60,
        "L": 45,
        "K": 40,
        "S": 38,
        
        # Clinical Scales
        "1": 70,  # Hs (Hypochondriasis)
        "2": 75,  # D (Depression)
        "3": 65,  # Hy (Hysteria)
        "4": 72,  # Pd (Psychopathic Deviate)
        "5": 60,  # Mf (Masculinity-Femininity)
        "6": 68,  # Pa (Paranoia)
        "7": 78,  # Pt (Psychasthenia)
        "8": 74,  # Sc (Schizophrenia)
        "9": 67,  # Ma (Hypomania)
        "0": 72,  # Si (Social Introversion)
        
        # Content Scales
        "ANX": 75,  # Anxiety
        "FRS": 68,  # Fears
        "OBS": 72,  # Obsessiveness
        "DEP": 76,  # Depression
        "HEA": 73,  # Health Concerns
        "BIZ": 65,  # Bizarre Mentation
        "ANG": 70,  # Anger
        "CYN": 68,  # Cynicism
        "ASP": 64,  # Antisocial Practices
        "TPA": 72,  # Type A
        "LSE": 74,  # Low Self-Esteem
        "SOD": 73,  # Social Discomfort
        "FAM": 69,  # Family Problems
        "WRK": 75,  # Work Interference
        "TRT": 77,  # Negative Treatment Indicators
        
        # RC Scales
        "RCd": 75,  # Demoralization
        "RC1": 70,  # Somatic Complaints
        "RC2": 72,  # Low Positive Emotions
        "RC3": 68,  # Cynicism
        "RC4": 72,  # Antisocial Behavior
        "RC6": 67,  # Ideas of Persecution
        "RC7": 76,  # Dysfunctional Negative Emotions
        "RC8": 69,  # Aberrant Experiences
        "RC9": 68,  # Hypomanic Activation
        
        # Component Scales
        "ANX1": 76,  # Generalized Anxiety
        "ANX2": 74,  # Performance Anxiety
        "FRS1": 67,  # Specific Fears
