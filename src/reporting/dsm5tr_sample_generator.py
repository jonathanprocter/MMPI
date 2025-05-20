#!/usr/bin/env python3
"""
Script to generate a sample report with DSM-5-TR diagnostic impressions.

This script creates a sample MMPI-2 profile with clinically significant elevations
and generates a comprehensive report that includes DSM-5-TR aligned diagnostic
impressions based on the decision tree algorithms.
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
from src.interpretation.dsm5tr_decision_trees import get_diagnostic_impressions, get_treatment_recommendations

# Create output directory if it doesn't exist
output_dir = os.path.join(os.path.dirname(__file__), "dsm5tr_sample_output")
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
            "id": "DSM5TR-SAMPLE-001",
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
            "7": 78,  # Pt (Psychasthenia)
            "8": 70,  # Sc (Schizophrenia)
            "9": 58,  # Ma (Hypomania)
            "0": 68,  # Si (Social Introversion)
            
            # RC Scales
            "RCd": 75,  # Demoralization
            "RC1": 70,  # Somatic Complaints
            "RC2": 78,  # Low Positive Emotions
            "RC3": 60,  # Cynicism
            "RC4": 62,  # Antisocial Behavior
            "RC6": 58,  # Ideas of Persecution
            "RC7": 76,  # Dysfunctional Negative Emotions
            "RC8": 65,  # Aberrant Experiences
            "RC9": 55,  # Hypomanic Activation
            
            # Content Scales
            "ANX": 75,  # Anxiety
            "FRS": 65,  # Fears
            "OBS": 72,  # Obsessiveness
            "DEP": 80,  # Depression
            "HEA": 70,  # Health Concerns
            "BIZ": 60,  # Bizarre Mentation
            "ANG": 58,  # Anger
            "CYN": 60,  # Cynicism
            "ASP": 55,  # Antisocial Practices
            "TPA": 62,  # Type A
            "LSE": 75,  # Low Self-Esteem
            "SOD": 70,  # Social Discomfort
            "FAM": 65,  # Family Problems
            "WRK": 72,  # Work Interference
            "TRT": 68,  # Negative Treatment Indicators
            
            # PSY-5 Scales
            "AGGR": 55,  # Aggressiveness
            "PSYC": 62,  # Psychoticism
            "DISC": 58,  # Disconstraint
            "NEGE": 75,  # Negative Emotionality/Neuroticism
            "INTR": 70,  # Introversion/Low Positive Emotionality
            
            # Supplementary Scales
            "A": 70,     # Anxiety
            "R": 65,     # Repression
            "Es": 40,    # Ego Strength
            "Do": 45,    # Dominance
            "Re": 50,    # Social Responsibility
            "Mt": 72,    # College Maladjustment
            "GM": 55,    # Gender Role - Masculine
            "GF": 60,    # Gender Role - Feminine
            "PK": 68,    # PTSD - Keane
            "PS": 65,    # PTSD - Schlenger
            "MDS": 70,   # Marital Distress
            "APS": 55,   # Addiction Potential
            "AAS": 50,   # Addiction Acknowledgment
            "O-H": 45,   # Overcontrolled Hostility
            "MAC-R": 58, # MacAndrew Alcoholism-Revised
            "FPTSD": 62  # Fake PTSD
        }
    }
    
    return profile_data

def generate_report(profile_data):
    """
    Generate a comprehensive report with DSM-5-TR diagnostic impressions.
    
    Args:
        profile_data: Dictionary containing the profile data
        
    Returns:
        Dictionary containing the report data
    """
    # Get diagnostic impressions using the DSM-5-TR decision trees
    diagnostic_impressions = get_diagnostic_impressions(profile_data)
    
    # Get treatment recommendations
    treatment_recommendations = get_treatment_recommendations(profile_data, diagnostic_impressions)
    
    # Create the report
    report = {
        "respondent_info": profile_data["respondent_info"],
        "validity_summary": generate_validity_summary(profile_data["scale_scores"]),
        "clinical_scales_summary": generate_clinical_scales_summary(profile_data["scale_scores"]),
        "rc_scales_summary": generate_rc_scales_summary(profile_data["scale_scores"]),
        "content_scales_summary": generate_content_scales_summary(profile_data["scale_scores"]),
        "psy5_scales_summary": generate_psy5_scales_summary(profile_data["scale_scores"]),
        "supplementary_scales_summary": generate_supplementary_scales_summary(profile_data["scale_scores"]),
        "two_point_code_analysis": generate_two_point_code_analysis(profile_data["scale_scores"]),
        "diagnostic_impressions": diagnostic_impressions,
        "treatment_recommendations": treatment_recommendations,
        "integrative_summary": generate_integrative_summary(profile_data["scale_scores"], diagnostic_impressions)
    }
    
    return report

def generate_validity_summary(scale_scores):
    """Generate validity scales summary."""
    return {
        "narrative": "The validity scales suggest a valid profile with possible slight exaggeration of symptoms. The elevated F scale (T=68) indicates acknowledgment of significant psychological distress, while the low K scale (T=40) suggests limited psychological resources and poor self-concept. The profile is likely an accurate representation of the respondent's current psychological functioning."
    }

def generate_clinical_scales_summary(scale_scores):
    """Generate clinical scales summary."""
    return {
        "narrative": "The clinical scales show significant elevations on Scale 2 (Depression, T=80), Scale 7 (Psychasthenia, T=78), Scale 1 (Hypochondriasis, T=72), and Scale 8 (Schizophrenia, T=70). This 2-7-1-8 profile suggests a person experiencing significant depression with anxiety, somatic concerns, and possible cognitive difficulties. The individual likely feels overwhelmed, worried, and may have trouble concentrating."
    }

def generate_rc_scales_summary(scale_scores):
    """Generate RC scales summary."""
    return {
        "narrative": "The RC scales confirm the clinical scale findings with elevations on RC2 (Low Positive Emotions, T=78), RC7 (Dysfunctional Negative Emotions, T=76), RCd (Demoralization, T=75), and RC1 (Somatic Complaints, T=70). This pattern indicates significant depressive symptoms, anxiety, general distress, and somatic concerns. The moderate elevation on RC8 (Aberrant Experiences, T=65) suggests some unusual thinking or perceptual experiences, possibly related to high anxiety."
    }

def generate_content_scales_summary(scale_scores):
    """Generate content scales summary."""
    return {
        "narrative": "The content scales show significant elevations on DEP (Depression, T=80), ANX (Anxiety, T=75), LSE (Low Self-Esteem, T=75), WRK (Work Interference, T=72), and OBS (Obsessiveness, T=72). This pattern indicates a person experiencing significant depression, anxiety, low self-esteem, difficulty functioning at work, and obsessive thinking. The individual likely feels worthless, worried, and has trouble concentrating on tasks."
    }

def generate_psy5_scales_summary(scale_scores):
    """Generate PSY-5 scales summary."""
    return {
        "narrative": "The PSY-5 scales show elevations on NEGE (Negative Emotionality/Neuroticism, T=75) and INTR (Introversion/Low Positive Emotionality, T=70). This pattern indicates a person who experiences significant negative emotions, worry, and anxiety, along with social withdrawal and anhedonia. The individual likely has difficulty experiencing positive emotions and tends to withdraw from social interactions."
    }

def generate_supplementary_scales_summary(scale_scores):
    """Generate supplementary scales summary."""
    return {
        "narrative": "The supplementary scales show elevations on A (Anxiety, T=70), Mt (College Maladjustment, T=72), and MDS (Marital Distress, T=70). This pattern indicates significant anxiety, general psychological distress, and possible relationship difficulties. The low Es (Ego Strength, T=40) score suggests limited psychological resources and coping abilities."
    }

def generate_two_point_code_analysis(scale_scores):
    """Generate two-point code analysis."""
    return {
        "code_type": "2-7/7-2",
        "narrative": "The 2-7/7-2 code type indicates a person experiencing significant depression and anxiety. Individuals with this profile typically feel sad, worried, tense, and overwhelmed. They often ruminate about problems, have difficulty concentrating, and may experience somatic symptoms related to anxiety. They tend to be self-critical, have low self-esteem, and may feel hopeless about the future. This profile is commonly associated with Major Depressive Disorder with anxious distress, Generalized Anxiety Disorder, or mixed anxiety-depressive presentations."
    }

def generate_integrative_summary(scale_scores, diagnostic_impressions):
    """Generate integrative summary."""
    return {
        "narrative": "This profile presents a consistent picture across all scale families, indicating a person experiencing significant depression with anxious features, somatic concerns, and possible cognitive difficulties. The individual likely feels sad, worried, tense, and overwhelmed, with poor self-esteem and limited coping resources. The 2-7/7-2 code type, along with elevations on corresponding RC and Content scales, strongly suggests a diagnosis of Major Depressive Disorder with anxious distress features. The somatic concerns indicated by elevations on Scale 1 and RC1 suggest that the individual may be experiencing physical manifestations of psychological distress. The moderate elevation on Scale 8 and RC8 may reflect cognitive difficulties related to depression and anxiety rather than a thought disorder. Treatment should focus on addressing depressive symptoms, anxiety management, and building coping skills."
    }

def create_profile_graphs(profile_data, output_dir):
    """
    Create graphical representations of the MMPI-2 profile.
    
    Args:
        profile_data: Dictionary containing the profile data
        output_dir: Directory to save the graphs
    """
    scale_scores = profile_data["scale_scores"]
    
    # Create traditional profile graph (Validity and Clinical Scales)
    with PdfPages(os.path.join(output_dir, "traditional_profile_graph.pdf")) as pdf:
        plt.figure(figsize=(12, 8))
        
        # Validity Scales
        validity_scales = ["L", "F", "K", "Fb", "Fp", "FBS"]
        validity_scores = [scale_scores.get(scale, 50) for scale in validity_scales]
        
        # Clinical Scales
        clinical_scales = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        clinical_scores = [scale_scores.get(scale, 50) for scale in clinical_scales]
        
        # Combined scales for x-axis
        all_scales = validity_scales + clinical_scales
        all_scores = validity_scores + clinical_scores
        
        # Create x-axis positions
        x_pos = np.arange(len(all_scales))
        
        # Create the bar chart
        plt.bar(x_pos, all_scores, color=['blue' if i < len(validity_scales) else 'red' for i in range(len(all_scales))])
        
        # Add horizontal lines for clinical significance
        plt.axhline(y=65, color='orange', linestyle='--', alpha=0.7)
        plt.axhline(y=70, color='red', linestyle='--', alpha=0.7)
        
        # Add labels and title
        plt.xlabel('MMPI-2 Scales')
        plt.ylabel('T-Scores')
        plt.title('MMPI-2 Validity and Clinical Scales Profile')
        plt.xticks(x_pos, all_scales, rotation=45)
        
        # Add grid
        plt.grid(axis='y', alpha=0.3)
        
        # Add T-score values above bars
        for i, v in enumerate(all_scores):
            plt.text(i, v + 2, str(v), ha='center')
        
        # Adjust layout
        plt.tight_layout()
        
        # Save to PDF
        pdf.savefig()
        plt.close()
        
        # Create separate graphs for each scale family
        # RC Scales
        plt.figure(figsize=(12, 8))
        rc_scales = ["RCd", "RC1", "RC2", "RC3", "RC4", "RC6", "RC7", "RC8", "RC9"]
        rc_scores = [scale_scores.get(scale, 50) for scale in rc_scales]
        
        x_pos = np.arange(len(rc_scales))
        plt.bar(x_pos, rc_scores, color='green')
        
        plt.axhline(y=65, color='orange', linestyle='--', alpha=0.7)
        plt.axhline(y=70, color='red', linestyle='--', alpha=0.7)
        
        plt.xlabel('RC Scales')
        plt.ylabel('T-Scores')
        plt.title('MMPI-2 Restructured Clinical Scales Profile')
        plt.xticks(x_pos, rc_scales, rotation=45)
        
        plt.grid(axis='y', alpha=0.3)
        
        for i, v in enumerate(rc_scores):
            plt.text(i, v + 2, str(v), ha='center')
        
        plt.tight_layout()
        pdf.savefig()
        plt.close()
        
        # Content Scales
        plt.figure(figsize=(14, 8))
        content_scales = ["ANX", "FRS", "OBS", "DEP", "HEA", "BIZ", "ANG", "CYN", "ASP", "TPA", "LSE", "SOD", "FAM", "WRK", "TRT"]
        content_scores = [scale_scores.get(scale, 50) for scale in content_scales]
        
        x_pos = np.arange(len(content_scales))
        plt.bar(x_pos, content_scores, color='purple')
        
        plt.axhline(y=65, color='orange', linestyle='--', alpha=0.7)
        plt.axhline(y=70, color='red', linestyle='--', alpha=0.7)
        
        plt.xlabel('Content Scales')
        plt.ylabel('T-Scores')
        plt.title('MMPI-2 Content Scales Profile')
        plt.xticks(x_pos, content_scales, rotation=45)
        
        plt.grid(axis='y', alpha=0.3)
        
        for i, v in enumerate(content_scores):
            plt.text(i, v + 2, str(v), ha='center')
        
        plt.tight_layout()
        pdf.savefig()
        plt.close()
        
        # PSY-5 Scales
        plt.figure(figsize=(10, 8))
        psy5_scales = ["AGGR", "PSYC", "DISC", "NEGE", "INTR"]
        psy5_scores = [scale_scores.get(scale, 50) for scale in psy5_scales]
        
        x_pos = np.arange(len(psy5_scales))
        plt.bar(x_pos, psy5_scores, color='brown')
        
        plt.axhline(y=65, color='orange', linestyle='--', alpha=0.7)
        plt.axhline(y=70, color='red', linestyle='--', alpha=0.7)
        
        plt.xlabel('PSY-5 Scales')
        plt.ylabel('T-Scores')
        plt.title('MMPI-2 PSY-5 Scales Profile')
        plt.xticks(x_pos, psy5_scales, rotation=45)
        
        plt.grid(axis='y', alpha=0.3)
        
        for i, v in enumerate(psy5_scores):
            plt.text(i, v + 2, str(v), ha='center')
        
        plt.tight_layout()
        pdf.savefig()
        plt.close()

def save_report(report, output_dir):
    """
    Save the report in various
(Content truncated due to size limit. Use line ranges to read in chunks)
