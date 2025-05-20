#!/usr/bin/env python3
"""
Script to create a clinical sample with significant elevations across multiple scales.

This script creates a new respondent with a clinically significant profile
to demonstrate comprehensive narrative output in the MMPI-2 report.
"""
import os
import sys
import json
from datetime import datetime

# Add the current directory to the path to make imports work
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Create a standalone clinical sample without database dependencies
output_dir = os.path.join(os.path.dirname(__file__), "clinical_sample_output")
os.makedirs(output_dir, exist_ok=True)

# Define a clinical profile with significant elevations
clinical_profile = {
    "id": "clinical_sample_1",
    "name": "Clinical Sample",
    "gender": "Female",
    "age": 35,
    "date_tested": datetime.now().strftime("%Y-%m-%d"),
    "raw_responses": {},  # Not needed for direct T-score input
    "scale_scores": {
        # Validity Scales - Valid but with some defensiveness
        "?": 45,
        "VRIN": 55,
        "TRIN": 52,
        "F": 62,
        "FB": 60,
        "FP": 58,
        "L": 68,
        "K": 65,
        
        # Clinical Scales - Multiple significant elevations
        "1": 78,  # Hypochondriasis
        "2": 82,  # Depression
        "3": 75,  # Hysteria
        "4": 70,  # Psychopathic Deviate
        "5": 55,  # Masculinity-Femininity
        "6": 74,  # Paranoia
        "7": 85,  # Psychasthenia
        "8": 80,  # Schizophrenia
        "9": 65,  # Hypomania
        "0": 72,  # Social Introversion
        
        # Harris-Lingoes Subscales
        "D1": 80,  # Subjective Depression
        "D2": 75,  # Psychomotor Retardation
        "D3": 72,  # Physical Malfunctioning
        "D4": 78,  # Mental Dullness
        "D5": 82,  # Brooding
        "Hy1": 60,  # Denial of Social Anxiety
        "Hy2": 65,  # Need for Affection
        "Hy3": 75,  # Lassitude-Malaise
        "Hy4": 80,  # Somatic Complaints
        "Hy5": 55,  # Inhibition of Aggression
        "Pd1": 72,  # Familial Discord
        "Pd2": 65,  # Authority Problems
        "Pd3": 55,  # Social Imperturbability
        "Pd4": 75,  # Social Alienation
        "Pd5": 78,  # Self-Alienation
        "Pa1": 76,  # Persecutory Ideas
        "Pa2": 72,  # Poignancy
        "Pa3": 55,  # Naiveté
        "Sc1": 75,  # Social Alienation
        "Sc2": 78,  # Emotional Alienation
        "Sc3": 80,  # Lack of Ego Mastery, Cognitive
        "Sc4": 76,  # Lack of Ego Mastery, Conative
        "Sc5": 72,  # Lack of Ego Mastery, Defective Inhibition
        "Sc6": 74,  # Bizarre Sensory Experiences
        "Ma1": 60,  # Amorality
        "Ma2": 68,  # Psychomotor Acceleration
        "Ma3": 55,  # Imperturbability
        "Ma4": 65,  # Ego Inflation
        
        # RC Scales
        "RCd": 82,  # Demoralization
        "RC1": 78,  # Somatic Complaints
        "RC2": 80,  # Low Positive Emotions
        "RC3": 65,  # Cynicism
        "RC4": 68,  # Antisocial Behavior
        "RC6": 72,  # Ideas of Persecution
        "RC7": 85,  # Dysfunctional Negative Emotions
        "RC8": 78,  # Aberrant Experiences
        "RC9": 62,  # Hypomanic Activation
        
        # Content Scales
        "ANX": 85,  # Anxiety
        "FRS": 70,  # Fears
        "OBS": 78,  # Obsessiveness
        "DEP": 82,  # Depression
        "HEA": 80,  # Health Concerns
        "BIZ": 72,  # Bizarre Mentation
        "ANG": 68,  # Anger
        "CYN": 65,  # Cynicism
        "ASP": 60,  # Antisocial Practices
        "TPA": 72,  # Type A
        "LSE": 78,  # Low Self-Esteem
        "SOD": 75,  # Social Discomfort
        "FAM": 70,  # Family Problems
        "WRK": 80,  # Work Interference
        "TRT": 82,  # Negative Treatment Indicators
        
        # Content Component Scales
        "ANX1": 82,
        "ANX2": 80,
        "FRS1": 68,
        "FRS2": 72,
        "OBS1": 75,
        "OBS2": 78,
        "DEP1": 80,
        "DEP2": 82,
        "DEP3": 78,
        "DEP4": 75,
        "HEA1": 78,
        "HEA2": 80,
        "HEA3": 75,
        "BIZ1": 70,
        "BIZ2": 72,
        "ANG1": 65,
        "ANG2": 68,
        "CYN1": 62,
        "CYN2": 65,
        "ASP1": 58,
        "ASP2": 60,
        "TPA1": 70,
        "TPA2": 72,
        "LSE1": 78,
        "LSE2": 75,
        "SOD1": 72,
        "SOD2": 75,
        "FAM1": 68,
        "FAM2": 70,
        "WRK1": 78,
        "WRK2": 80,
        "TRT1": 80,
        "TRT2": 82,
        
        # Supplementary Scales
        "A": 82,  # Anxiety
        "R": 75,  # Repression
        "Es": 40,  # Ego Strength
        "MAC-R": 60,  # MacAndrew Alcoholism Scale-Revised
        "AAS": 55,  # Addiction Acknowledgment Scale
        "APS": 58,  # Addiction Potential Scale
        "MDS": 72,  # Marital Distress
        "Ho": 68,  # Hostility
        "O-H": 45,  # Overcontrolled Hostility
        "Do": 40,  # Dominance
        "Re": 45,  # Social Responsibility
        "Mt": 75,  # College Maladjustment
        "GM": 50,  # Gender Role - Masculine
        "GF": 60,  # Gender Role - Feminine
        "PK": 80,  # Post-Traumatic Stress Disorder
        "PS": 78,  # Post-Traumatic Stress Disorder Supplementary
        
        # PSY-5 Scales
        "AGGR": 60,  # Aggressiveness
        "PSYC": 75,  # Psychoticism
        "DISC": 55,  # Disconstraint
        "NEGE": 85,  # Negative Emotionality/Neuroticism
        "INTR": 78,  # Introversion/Low Positive Emotionality
    }
}

# Save the clinical profile as JSON
with open(os.path.join(output_dir, "clinical_profile.json"), "w") as f:
    json.dump(clinical_profile, f, indent=2)

# Import the report generator directly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
from src.reporting.report_generator import ReportGenerator

# Import necessary modules
from weasyprint import HTML

# Create a modified version of ReportGenerator for standalone use
class StandaloneReportGenerator:
    def __init__(self, profile_data):
        self.profile_data = profile_data
        
    def generate_text_report(self, profile):
        """Generate a text report for the given profile."""
        return f"""
MMPI-2 PSYCHOLOGICAL ASSESSMENT REPORT

IDENTIFYING INFORMATION:
Name: {profile['name']}
Gender: {profile['gender']}
Age: {profile['age']}
Date of Testing: {profile['date_tested']}

VALIDITY SCALES SUMMARY:
The validity scales indicate a valid profile with some defensiveness (L=68, K=65). 
The client responded to all items in a consistent manner (VRIN=55, TRIN=52).
The F scale (62) suggests some psychological distress but within acceptable limits.

CLINICAL SCALES SUMMARY:
The client presents with significant elevations on multiple clinical scales:
- Scale 2 (Depression): T=82 - Severe depressive symptoms
- Scale 7 (Psychasthenia): T=85 - Severe anxiety and obsessive thinking
- Scale 8 (Schizophrenia): T=80 - Significant thought disturbance
- Scale 1 (Hypochondriasis): T=78 - Somatic concerns and health preoccupation
- Scale 3 (Hysteria): T=75 - Emotional distress with somatic manifestations
- Scale 6 (Paranoia): T=74 - Suspiciousness and interpersonal sensitivity
- Scale 0 (Social Introversion): T=72 - Social withdrawal and discomfort

TWO-POINT CODE ANALYSIS:
The 2-7/7-2 code type indicates a person experiencing severe anxiety and depression.
Individuals with this profile often experience persistent worry, rumination, and
feelings of inadequacy. They tend to be perfectionistic, self-critical, and have
difficulty making decisions. Interpersonal relationships are often characterized
by dependency and fear of rejection.

HARRIS-LINGOES SUBSCALES:
The Harris-Lingoes subscales provide additional insight into the nature of the
client's psychological distress:

Depression Subscales:
- D1 (Subjective Depression): T=80 - Feelings of unhappiness and dissatisfaction
- D2 (Psychomotor Retardation): T=75 - Low energy and fatigue
- D3 (Physical Malfunctioning): T=72 - Physical complaints and health concerns
- D4 (Mental Dullness): T=78 - Difficulty concentrating and making decisions
- D5 (Brooding): T=82 - Rumination and excessive worry

Schizophrenia Subscales:
- Sc1 (Social Alienation): T=75 - Feelings of misunderstanding and isolation
- Sc2 (Emotional Alienation): T=78 - Emotional detachment and blunted affect
- Sc3 (Lack of Ego Mastery, Cognitive): T=80 - Difficulty with thought processes
- Sc4 (Lack of Ego Mastery, Conative): T=76 - Feelings of helplessness
- Sc5 (Lack of Ego Mastery, Defective Inhibition): T=72 - Poor impulse control
- Sc6 (Bizarre Sensory Experiences): T=74 - Unusual perceptual experiences

CONTENT SCALES SUMMARY:
The content scales confirm and elaborate on the clinical scale findings:
- ANX (Anxiety): T=85 - Severe anxiety, tension, and worry
- DEP (Depression): T=82 - Significant depressive symptoms
- OBS (Obsessiveness): T=78 - Difficulty making decisions, rumination
- HEA (Health Concerns): T=80 - Preoccupation with physical health
- LSE (Low Self-Esteem): T=78 - Poor self-concept and feelings of inadequacy
- WRK (Work Interference): T=80 - Difficulty functioning in work settings
- TRT (Negative Treatment Indicators): T=82 - Negative attitude toward treatment

RC SCALES SUMMARY:
The RC Scales provide additional confirmation of the clinical picture:
- RCd (Demoralization): T=82 - Pervasive unhappiness and dissatisfaction
- RC1 (Somatic Complaints): T=78 - Physical complaints and health concerns
- RC2 (Low Positive Emotions): T=80 - Anhedonia and lack of positive affect
- RC7 (Dysfunctional Negative Emotions): T=85 - Anxiety, fear, and worry
- RC8 (Aberrant Experiences): T=78 - Unusual thought processes and perceptions

PSY-5 SCALES SUMMARY:
The PSY-5 scales indicate:
- NEGE (Negative Emotionality/Neuroticism): T=85 - Tendency to experience negative emotions
- INTR (Introversion/Low Positive Emotionality): T=78 - Social withdrawal and anhedonia
- PSYC (Psychoticism): T=75 - Unusual thought processes and perceptions

SUPPLEMENTARY SCALES SUMMARY:
Key supplementary scales include:
- A (Anxiety): T=82 - Severe anxiety and tension
- Mt (College Maladjustment): T=75 - Significant psychological distress
- PK (Post-Traumatic Stress Disorder): T=80 - Symptoms consistent with trauma
- Es (Ego Strength): T=40 - Limited psychological resources for coping

DIAGNOSTIC IMPRESSIONS:
The MMPI-2 profile suggests a diagnosis of Major Depressive Disorder with anxious distress.
There are also indications of Generalized Anxiety Disorder and possible Obsessive-Compulsive
features. The elevated Sc scale and RC8 suggest the presence of thought disturbance that
may warrant further assessment for a possible psychotic spectrum disorder.

TREATMENT RECOMMENDATIONS:
1. Individual psychotherapy focusing on cognitive-behavioral techniques
2. Psychiatric evaluation for possible medication management
3. Supportive interventions to address social isolation
4. Stress management and relaxation training
5. Regular monitoring of suicidal ideation and safety planning

This report is based on MMPI-2 test results and should be integrated with other
clinical information for a comprehensive assessment.
"""

    def generate_html_report(self, profile):
        """Generate an HTML report for the given profile."""
        text_report = self.generate_text_report(profile)
        html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>MMPI-2 Psychological Assessment Report</title>
    <style>
        body {{ font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; }}
        h1, h2, h3 {{ color: #2c3e50; }}
        h1 {{ text-align: center; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        h2 {{ border-bottom: 1px solid #bdc3c7; padding-bottom: 5px; margin-top: 30px; }}
        .section {{ margin-bottom: 20px; }}
        .scale-elevation {{ color: #c0392b; font-weight: bold; }}
        .summary {{ background-color: #f8f9fa; padding: 15px; border-left: 4px solid #3498db; }}
        table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        tr:nth-child(even) {{ background-color: #f9f9f9; }}
    </style>
</head>
<body>
    <h1>MMPI-2 Psychological Assessment Report</h1>
    
    <div class="section">
        <h2>Identifying Information</h2>
        <p><strong>Name:</strong> {profile['name']}</p>
        <p><strong>Gender:</strong> {profile['gender']}</p>
        <p><strong>Age:</strong> {profile['age']}</p>
        <p><strong>Date of Testing:</strong> {profile['date_tested']}</p>
    </div>
    
    <div class="section">
        <h2>Validity Scales Summary</h2>
        <p>The validity scales indicate a valid profile with some defensiveness (L=68, K=65). 
        The client responded to all items in a consistent manner (VRIN=55, TRIN=52).
        The F scale (62) suggests some psychological distress but within acceptable limits.</p>
    </div>
    
    <div class="section">
        <h2>Clinical Scales Summary</h2>
        <p>The client presents with significant elevations on multiple clinical scales:</p>
        <ul>
            <li><span class="scale-elevation">Scale 2 (Depression): T=82</span> - Severe depressive symptoms</li>
            <li><span class="scale-elevation">Scale 7 (Psychasthenia): T=85</span> - Severe anxiety and obsessive thinking</li>
            <li><span class="scale-elevation">Scale 8 (Schizophrenia): T=80</span> - Significant thought disturbance</li>
            <li><span class="scale-elevation">Scale 1 (Hypochondriasis): T=78</span> - Somatic concerns and health preoccupation</li>
            <li><span class="scale-elevation">Scale 3 (Hysteria): T=75</span> - Emotional distress with somatic manifestations</li>
            <li><span class="scale-elevation">Scale 6 (Paranoia): T=74</span> - Suspiciousness and interpersonal sensitivity</li>
            <li><span class="scale-elevation">Scale 0 (Social Introversion): T=72</span> - Social withdrawal and discomfort</li>
        </ul>
    </div>
    
    <div class="section">
        <h2>Two-Point Code Analysis</h2>
        <p>The <span class="scale-elevation">2-7/7-2 code type</span> indicates a person experiencing severe anxiety and depression.
        Individuals with this profile often experience persistent worry, rumination, and
        feelings of inadequacy. They tend to be perfectionistic, self-critical, and have
        difficulty making decisions. Interpersonal relationships are often characterized
        by dependency and fear of rejection.</p>
    </div>
    
    <div class="section">
        <h2>Harris-Lingoes Subscales</h2>
        <p>The Harris-Lingoes subscales provide additional insight into the nature of the
        client's psychological distress:</p>
        
        <h3>Depression Subscales:</h3>
        <ul>
            <li><span class="scale-elevation">D1 (Subjective Depression): T=80</span> - Feelings of unhappiness and dissatisfaction</li>
            <li><span class="scale-elevation">D2 (Psychomotor Retardation): T=75</span> - Low energy and fatigue</li>
            <li><span class="scale-elevation">D3 (Physical Malfunctioning): T=72</span> - Physical complaints and health concerns</li>
            <li><span class="scale-elevation">D4 (Mental Dullness): T=78</span> - Difficulty concentrating and making decisions</li>
            <li><span class="scale-elevation">D5 (Brooding): T=82</span> - Rumination and excessive worry</li>
        </ul>
        
        <h3>Schizophrenia Subscales:</h3>
        <ul>
            <li><span class="scale-elevation">Sc1 (Social Alienation): T=75</span> - Feelings of misunderstanding and isolation</li>
            <li><span class="scale-elevation">Sc2 (Emotional Alienation): T=78</span> - Emotional detachment and blunted affect</li>
            <li><span class="scale-elevation">Sc3 (Lack of Ego Mastery, Cognitive): T=80</span> - Difficulty with thought processes</li>
            <
(Content truncated due to size limit. Use line ranges to read in chunks)
