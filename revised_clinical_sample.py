#!/usr/bin/env python3
"""
Script to create an enhanced clinical sample with significant elevations across multiple scales.

This script creates a new respondent with a clinically significant profile
to demonstrate comprehensive narrative output in the MMPI-2 report,
including detailed scale interpretations and graphical representations.
"""
import os
import sys
import json
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.gridspec as gridspec

# Add the current directory to the path to make imports work
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import necessary modules for interpretations
from src.interpretation.scale_interpretations import get_scale_interpretation

# Create a standalone clinical sample without database dependencies
output_dir = os.path.join(os.path.dirname(__file__), "revised_clinical_output")
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

# Generate traditional MMPI-2 profile graph
def generate_traditional_profile_graph(profile, output_dir):
    """Generate a traditional MMPI-2 profile graph."""
    # Create a PDF to hold the traditional profile graph
    pdf_path = os.path.join(output_dir, "traditional_profile_graph.pdf")
    
    with PdfPages(pdf_path) as pdf:
        # Set up the figure
        plt.figure(figsize=(11, 8.5))  # US Letter size
        
        # Define the scales and their T-scores
        validity_scales = ["L", "F", "K"]
        validity_scores = [profile["scale_scores"].get(scale, 0) for scale in validity_scales]
        
        clinical_scales = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        clinical_scores = [profile["scale_scores"].get(scale, 0) for scale in clinical_scales]
        
        # Combine all scales for the x-axis
        all_scales = validity_scales + clinical_scales
        all_scores = validity_scores + clinical_scores
        
        # Create the plot
        plt.plot(range(len(all_scales)), all_scores, 'o-', color='blue', markersize=8)
        
        # Add a horizontal line at T=65 (clinical significance)
        plt.axhline(y=65, color='r', linestyle='--', alpha=0.7)
        
        # Set the y-axis limits and ticks
        plt.ylim(30, 120)
        plt.yticks(range(30, 121, 10))
        
        # Set the x-axis ticks and labels
        plt.xticks(range(len(all_scales)), all_scales)
        
        # Add grid lines
        plt.grid(True, axis='y', linestyle='--', alpha=0.7)
        
        # Add labels and title
        plt.xlabel('MMPI-2 Scales', fontsize=12)
        plt.ylabel('T-Score', fontsize=12)
        plt.title('MMPI-2 Traditional Profile', fontsize=16)
        
        # Add T-score values above each point
        for i, score in enumerate(all_scores):
            plt.text(i, score + 3, str(score), ha='center', fontsize=10)
        
        # Add a legend
        plt.legend(['Profile', 'Clinical Significance (T=65)'], loc='upper right')
        
        # Adjust layout
        plt.tight_layout()
        
        # Save the figure to the PDF
        pdf.savefig()
        plt.close()
    
    return pdf_path

# Generate individual scale family graphs
def generate_scale_family_graphs(profile, output_dir):
    """Generate individual graphs for each scale family."""
    # Create a PDF to hold all graphs
    pdf_path = os.path.join(output_dir, "scale_family_graphs.pdf")
    
    with PdfPages(pdf_path) as pdf:
        # Validity Scales Graph
        validity_scales = ["?", "VRIN", "TRIN", "F", "FB", "FP", "L", "K"]
        validity_scores = [profile["scale_scores"].get(scale, 0) for scale in validity_scales]
        
        plt.figure(figsize=(12, 6))
        plt.bar(validity_scales, validity_scores, color='skyblue')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('Validity Scales T-Scores', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()
        
        for i, score in enumerate(validity_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=12)
            
        pdf.savefig()
        plt.close()
        
        # Clinical Scales Graph
        clinical_scales = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        clinical_names = ["Hs", "D", "Hy", "Pd", "Mf", "Pa", "Pt", "Sc", "Ma", "Si"]
        clinical_scores = [profile["scale_scores"].get(scale, 0) for scale in clinical_scales]
        
        plt.figure(figsize=(12, 6))
        bars = plt.bar(clinical_names, clinical_scores, color='lightgreen')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('Clinical Scales T-Scores', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()
        
        # Highlight the highest scales for two-point code
        sorted_indices = np.argsort(clinical_scores)
        highest_indices = sorted_indices[-2:]
        for i in highest_indices:
            bars[i].set_color('darkgreen')
            
        for i, score in enumerate(clinical_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=12)
            
        pdf.savefig()
        plt.close()
        
        # Harris-Lingoes Subscales Graph - Depression
        d_subscales = ["D1", "D2", "D3", "D4", "D5"]
        d_scores = [profile["scale_scores"].get(scale, 0) for scale in d_subscales]
        
        plt.figure(figsize=(10, 6))
        plt.bar(d_subscales, d_scores, color='salmon')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('Depression (Scale 2) Harris-Lingoes Subscales', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()
        
        for i, score in enumerate(d_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=12)
            
        pdf.savefig()
        plt.close()
        
        # Harris-Lingoes Subscales Graph - Schizophrenia
        sc_subscales = ["Sc1", "Sc2", "Sc3", "Sc4", "Sc5", "Sc6"]
        sc_scores = [profile["scale_scores"].get(scale, 0) for scale in sc_subscales]
        
        plt.figure(figsize=(12, 6))
        plt.bar(sc_subscales, sc_scores, color='mediumpurple')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('Schizophrenia (Scale 8) Harris-Lingoes Subscales', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()
        
        for i, score in enumerate(sc_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=12)
            
        pdf.savefig()
        plt.close()
        
        # RC Scales Graph
        rc_scales = ["RCd", "RC1", "RC2", "RC3", "RC4", "RC6", "RC7", "RC8", "RC9"]
        rc_scores = [profile["scale_scores"].get(scale, 0) for scale in rc_scales]
        
        plt.figure(figsize=(12, 6))
        plt.bar(rc_scales, rc_scores, color='coral')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('Restructured Clinical Scales T-Scores', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()
        
        for i, score in enumerate(rc_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=12)
            
        pdf.savefig()
        plt.close()
        
        # Content Scales Graph
        content_scales = ["ANX", "FRS", "OBS", "DEP", "HEA", "BIZ", "ANG", "CYN", "ASP", "TPA", "LSE", "SOD", "FAM", "WRK", "TRT"]
        content_scores = [profile["scale_scores"].get(scale, 0) for scale in content_scales]
        
        plt.figure(figsize=(15, 6))
        plt.bar(content_scales, content_scores, color='plum')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('Content Scales T-Scores', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.legend()
        
        for i, score in enumerate(content_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=10)
            
        plt.tight_layout()
        pdf.savefig()
        plt.close()
        
        # PSY-5 Scales Graph
        psy5_scales = ["AGGR", "PSYC", "DISC", "NEGE", "INTR"]
        psy5_scores = [profile["scale_scores"].get(scale, 0) for scale in psy5_scales]
        
        plt.figure(figsize=(10, 6))
        plt.bar(psy5_scales, psy5_scores, color='lightblue')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('PSY-5 Scales T-Scores', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()
        
        for i, score in enumerate(psy5_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=12)
            
        pdf.savefig()
        plt.close()
        
        # Supplementary Scales Graph (selected key scales)
        supp_scales = ["A", "R", "Es", "MAC-R", "AAS", "APS", "MDS", "Ho", "O-H", "PK", "PS"]
        supp_scores = [profile["scale_scores"].get(scale, 0) for scale in supp_scales]
        
        plt.figure(figsize=(14, 6))
        plt.bar(supp_scales, supp_scores, color='tan')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('Selected Supplementary Scales T-Scores', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.xticks(rotation=45)
        plt.legend()
        
        for i, score in enumerate(supp_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=12)
            
        plt.tight_layout()
        pdf.savefig()
        plt.close()
        
    return pdf_path

# Generate the profile graphs
traditional_graph_path = generate_traditional_profile_graph(clinical_profile, output_dir)
family_graphs_path = generate_scale_family_graphs(clinical_profile, output_dir)

# Create a revised report generator that uses the detailed interpretations

class RevisedReportGenerator:
    """Placeholder for revised report generation."""
    def __init__(self, profile_data):
        self.profile_data = profile_data

    def generate(self, output_dir):
        path = os.path.join(output_dir, "revised_report.txt")
        with open(path, "w") as f:
            f.write("Revised report generation not implemented.")
        return path

