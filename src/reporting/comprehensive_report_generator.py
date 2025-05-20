#!/usr/bin/env python3
"""
Script to generate a comprehensive MMPI-2 report with detailed narratives and DSM-5-TR diagnostic impressions.

This script creates a sample MMPI-2 profile with clinically significant elevations
and generates a comprehensive report that includes both detailed scale interpretations
and DSM-5-TR aligned diagnostic impressions.
"""

import os
import sys
import json
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import necessary modules
from src.interpretation.scale_interpretations import get_scale_interpretation
from src.interpretation.dsm5tr_decision_trees import get_diagnostic_impressions, get_treatment_recommendations

# Create output directory if it doesn't exist
output_dir = os.path.join(os.path.dirname(__file__), "comprehensive_report_output")
os.makedirs(output_dir, exist_ok=True)

def create_sample_profile():
    """
    Create a sample MMPI-2 profile with clinically significant elevations.
    
    Returns:
        Dictionary containing the sample profile data
    """
    # Create a sample profile with clinically significant elevations
    profile_data = {
        "respondent_info": {
            "id": "COMPREHENSIVE-SAMPLE-001",
            "name": "Sample Respondent",
            "age": 35,
            "gender": "Female",
            "date_tested": datetime.now().strftime("%Y-%m-%d"),
            "education": "College Graduate",
            "referral_source": "Self-referred",
            "presenting_concerns": "Anxiety, depression, difficulty concentrating"
        },
        "scale_scores": {
            # Validity Scales
            "?": 45,
            "VRIN": 55,
            "TRIN": 57,
            "F": 68,
            "Fb": 72,
            "Fp": 60,
            "FBS": 65,
            "L": 45,
            "K": 40,
            
            # Clinical Scales
            "1": 72,  # Hs (Hypochondriasis)
            "2": 80,  # D (Depression)
            "3": 68,  # Hy (Hysteria)
            "4": 65,  # Pd (Psychopathic Deviate)
            "5": 55,  # Mf (Masculinity-Femininity)
            "6": 62,  # Pa (Paranoia)
            "7": 85,  # Pt (Psychasthenia)
            "8": 70,  # Sc (Schizophrenia)
            "9": 58,  # Ma (Hypomania)
            "0": 72,  # Si (Social Introversion)
            
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
    
    return profile_data

def generate_all_graphs(profile_data, output_dir):
    """
    Generate all graphs for the MMPI-2 profile.
    
    Args:
        profile_data: Dictionary containing the profile data
        output_dir: Directory to save the graphs
        
    Returns:
        Dictionary with paths to all generated graph files
    """
    graph_paths = {}
    
    # Generate traditional profile graph
    graph_paths["traditional"] = generate_traditional_profile_graph(profile_data, output_dir)
    
    # Generate scale family graphs
    graph_paths["scale_families"] = generate_scale_family_graphs(profile_data, output_dir)
    
    return graph_paths

def generate_traditional_profile_graph(profile_data, output_dir):
    """
    Generate a traditional MMPI-2 profile graph.
    
    Args:
        profile_data: Dictionary containing the profile data
        output_dir: Directory to save the graph
        
    Returns:
        Path to the generated graph file
    """
    # Create a PDF to hold the traditional profile graph
    pdf_path = os.path.join(output_dir, "traditional_profile_graph.pdf")
    
    with PdfPages(pdf_path) as pdf:
        # Set up the figure
        plt.figure(figsize=(11, 8.5))  # US Letter size
        
        # Define the scales and their T-scores
        validity_scales = ["L", "F", "K"]
        validity_scores = [profile_data["scale_scores"].get(scale, 0) for scale in validity_scales]
        
        clinical_scales = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        clinical_scores = [profile_data["scale_scores"].get(scale, 0) for scale in clinical_scales]
        
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

def generate_scale_family_graphs(profile_data, output_dir):
    """
    Generate individual graphs for each scale family.
    
    Args:
        profile_data: Dictionary containing the profile data
        output_dir: Directory to save the graphs
        
    Returns:
        Path to the generated graph file
    """
    # Create a PDF to hold all graphs
    pdf_path = os.path.join(output_dir, "scale_family_graphs.pdf")
    
    with PdfPages(pdf_path) as pdf:
        # Validity Scales Graph
        validity_scales = ["?", "VRIN", "TRIN", "F", "Fb", "Fp", "FBS", "L", "K"]
        validity_scores = [profile_data["scale_scores"].get(scale, 0) for scale in validity_scales]
        
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
        clinical_scores = [profile_data["scale_scores"].get(scale, 0) for scale in clinical_scales]
        
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
        d_scores = [profile_data["scale_scores"].get(scale, 0) for scale in d_subscales]
        
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
        
        # Harris-Lingoes Subscales Graph - Hysteria
        hy_subscales = ["Hy1", "Hy2", "Hy3", "Hy4", "Hy5"]
        hy_scores = [profile_data["scale_scores"].get(scale, 0) for scale in hy_subscales]
        
        plt.figure(figsize=(10, 6))
        plt.bar(hy_subscales, hy_scores, color='khaki')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('Hysteria (Scale 3) Harris-Lingoes Subscales', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()
        
        for i, score in enumerate(hy_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=12)
            
        pdf.savefig()
        plt.close()
        
        # Harris-Lingoes Subscales Graph - Psychopathic Deviate
        pd_subscales = ["Pd1", "Pd2", "Pd3", "Pd4", "Pd5"]
        pd_scores = [profile_data["scale_scores"].get(scale, 0) for scale in pd_subscales]
        
        plt.figure(figsize=(10, 6))
        plt.bar(pd_subscales, pd_scores, color='lightcoral')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('Psychopathic Deviate (Scale 4) Harris-Lingoes Subscales', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()
        
        for i, score in enumerate(pd_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=12)
            
        pdf.savefig()
        plt.close()
        
        # Harris-Lingoes Subscales Graph - Paranoia
        pa_subscales = ["Pa1", "Pa2", "Pa3"]
        pa_scores = [profile_data["scale_scores"].get(scale, 0) for scale in pa_subscales]
        
        plt.figure(figsize=(10, 6))
        plt.bar(pa_subscales, pa_scores, color='palegreen')
        plt.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance Threshold')
        plt.title('Paranoia (Scale 6) Harris-Lingoes Subscales', fontsize=16)
        plt.ylabel('T-Score', fontsize=14)
        plt.ylim(0, 120)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend()
        
        for i, score in enumerate(pa_scores):
            plt.text(i, score + 2, str(score), ha='center', fontsize=12)
            
        pdf.savefig()
        plt.close()
        
        # Harris-Lingoes Subscales Graph - Schizophrenia
        sc_subscales = ["Sc1", "Sc2", "Sc3", "Sc4", "Sc5", "Sc6"]
        sc_scores = [profile_data["scale_scores"].get(scale, 0) for scale in sc_subscales]
        
        plt.figure(figsize=(12, 6))
        plt.bar(sc_subscales, sc_scores, color='mediumpurple')
        plt.axhline(y=65, color='r', linestyle='
(Content truncated due to size limit. Use line ranges to read in chunks)
