#!/usr/bin/env python3
"""
Script to generate a final comprehensive MMPI-2 report with embedded graphs,
detailed narrative interpretations, and DSM-5-TR diagnostic impressions.

This script integrates all improvements including:
1. Detailed component scale interpretations
2. Embedded graphs for all scale families
3. DSM-5-TR diagnostic decision trees
4. Proper formatting and professional clinical presentation
"""

import os
import sys
import json
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
from datetime import datetime

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import interpretation modules
from src.interpretation.validity_scales import get_validity_scale_interpretation
from src.interpretation.clinical_scales import get_clinical_scale_interpretation
from src.interpretation.harris_lingoes_subscales import get_harris_lingoes_interpretation
from src.interpretation.content_scales import get_content_scale_interpretation
from src.interpretation.content_component_scales import get_content_component_interpretation
from src.interpretation.rc_scales import get_rc_scale_interpretation
from src.interpretation.psy5_scales import get_psy5_scale_interpretation
from src.interpretation.supplementary_scales import get_supplementary_scale_interpretation
from src.interpretation.dsm5tr_decision_trees import get_dsm5tr_diagnostic_impressions
from src.interpretation.component_scales import get_component_scale_interpretation, get_component_scale_integration, get_component_scale_diagnostic_considerations

# Create output directory if it doesn't exist
output_dir = "final_comprehensive_output"
os.makedirs(output_dir, exist_ok=True)

def create_clinically_significant_profile():
    """
    Create a clinically significant MMPI-2 profile with elevations across multiple scales.
    """
    # Basic respondent information
    profile_data = {
        "id": "comprehensive_sample",
        "name": "Jane Smith",
        "age": 35,
        "gender": "Female",
        "date_tested": datetime.now().strftime("%Y-%m-%d"),
        "education": "Bachelor's Degree",
        "marital_status": "Divorced",
        "referral_source": "Self-referred",
        "presenting_concerns": "Anxiety, depression, relationship difficulties, physical complaints"
    }
    
    # Validity Scales (T-scores)
    validity_scales = {
        "VRIN": 58,
        "TRIN": 57,
        "F": 75,
        "Fb": 78,
        "Fp": 65,
        "L": 45,
        "K": 40,
        "S": 38
    }
    
    # Clinical Scales (T-scores)
    clinical_scales = {
        "1": 78,  # Hs (Hypochondriasis)
        "2": 82,  # D (Depression)
        "3": 70,  # Hy (Hysteria)
        "4": 68,  # Pd (Psychopathic Deviate)
        "5": 55,  # Mf (Masculinity-Femininity)
        "6": 72,  # Pa (Paranoia)
        "7": 85,  # Pt (Psychasthenia)
        "8": 76,  # Sc (Schizophrenia)
        "9": 45,  # Ma (Hypomania)
        "0": 70   # Si (Social Introversion)
    }
    
    # Harris-Lingoes Subscales (T-scores)
    harris_lingoes_subscales = {
        "D1": 80,  # Subjective Depression
        "D2": 75,  # Psychomotor Retardation
        "D3": 78,  # Physical Malfunctioning
        "D4": 72,  # Mental Dullness
        "D5": 68,  # Brooding
        "Hy1": 45, # Denial of Social Anxiety
        "Hy2": 72, # Need for Affection
        "Hy3": 78, # Lassitude-Malaise
        "Hy4": 74, # Somatic Complaints
        "Hy5": 65, # Inhibition of Aggression
        "Pd1": 70, # Familial Discord
        "Pd2": 65, # Authority Problems
        "Pd3": 72, # Social Imperturbability
        "Pd4": 68, # Social Alienation
        "Pd5": 72, # Self-Alienation
        "Pa1": 74, # Persecutory Ideas
        "Pa2": 70, # Poignancy
        "Pa3": 65, # Naivete
        "Sc1": 75, # Social Alienation
        "Sc2": 78, # Emotional Alienation
        "Sc3": 80, # Lack of Ego Mastery, Cognitive
        "Sc4": 76, # Lack of Ego Mastery, Conative
        "Sc5": 72, # Lack of Ego Mastery, Defective Inhibition
        "Sc6": 74, # Bizarre Sensory Experiences
        "Ma1": 45, # Amorality
        "Ma2": 48, # Psychomotor Acceleration
        "Ma3": 50, # Imperturbability
        "Ma4": 45, # Ego Inflation
        "Si1": 72, # Shyness/Self-Consciousness
        "Si2": 70, # Social Avoidance
        "Si3": 65  # Self/Other Alienation
    }
    
    # Content Scales (T-scores)
    content_scales = {
        "ANX": 82, # Anxiety
        "FRS": 72, # Fears
        "OBS": 78, # Obsessiveness
        "DEP": 80, # Depression
        "HEA": 78, # Health Concerns
        "BIZ": 68, # Bizarre Mentation
        "ANG": 65, # Anger
        "CYN": 70, # Cynicism
        "ASP": 60, # Antisocial Practices
        "TPA": 65, # Type A
        "LSE": 78, # Low Self-Esteem
        "SOD": 75, # Social Discomfort
        "FAM": 70, # Family Problems
        "WRK": 75, # Work Interference
        "TRT": 82  # Negative Treatment Indicators
    }
    
    # Content Component Scales (T-scores)
    content_component_scales = {
        "ANX1": 82, # Generalized Anxiety
        "ANX2": 80, # Performance Anxiety
        "FRS1": 68, # Specific Fears
        "FRS2": 72, # Social Anxiety
        "OBS1": 75, # Obsessive Thoughts
        "OBS2": 78, # Compulsive Behaviors
        "DEP1": 80, # Lack of Drive
        "DEP2": 82, # Dysphoria
        "DEP3": 78, # Self-Depreciation
        "DEP4": 75, # Suicidal Ideation
        "HEA1": 78, # Gastrointestinal Symptoms
        "HEA2": 80, # Neurological Symptoms
        "HEA3": 75, # General Health Concerns
        "BIZ1": 70, # Psychotic Thinking
        "BIZ2": 65, # Bizarre Sensory Experiences
        "ANG1": 68, # Anger Proneness
        "ANG2": 65, # Irritability
        "CYN1": 72, # Misanthropic Beliefs
        "CYN2": 68, # Interpersonal Suspiciousness
        "ASP1": 62, # Antisocial Attitudes
        "ASP2": 58, # Antisocial Behavior
        "TPA1": 68, # Impatience
        "TPA2": 65, # Competitive Drive
        "LSE1": 78, # Self-Doubt
        "LSE2": 75, # Submissiveness
        "SOD1": 72, # Introversion
        "SOD2": 75, # Shyness
        "FAM1": 68, # Family Discord
        "FAM2": 70, # Familial Alienation
        "WRK1": 72, # Work Aversion
        "WRK2": 75, # Poor Concentration
        "TRT1": 80, # Low Motivation
        "TRT2": 82  # Inability to Disclose
    }
    
    # RC (Restructured Clinical) Scales (T-scores)
    rc_scales = {
        "RCd": 80, # Demoralization
        "RC1": 75, # Somatic Complaints
        "RC2": 78, # Low Positive Emotions
        "RC3": 65, # Cynicism
        "RC4": 62, # Antisocial Behavior
        "RC6": 70, # Ideas of Persecution
        "RC7": 82, # Dysfunctional Negative Emotions
        "RC8": 72, # Aberrant Experiences
        "RC9": 45  # Hypomanic Activation
    }
    
    # PSY-5 (Personality Psychopathology Five) Scales (T-scores)
    psy5_scales = {
        "AGGR": 45, # Aggressiveness
        "PSYC": 68, # Psychoticism
        "DISC": 50, # Disconstraint
        "NEGE": 80, # Negative Emotionality/Neuroticism
        "INTR": 75  # Introversion/Low Positive Emotionality
    }
    
    # Supplementary Scales (T-scores)
    supplementary_scales = {
        "A": 78,    # Anxiety
        "R": 45,    # Repression
        "Es": 35,   # Ego Strength
        "Do": 40,   # Dominance
        "Re": 45,   # Social Responsibility
        "Mt": 75,   # College Maladjustment
        "GM": 45,   # Masculine Gender Role
        "GF": 55,   # Feminine Gender Role
        "PK": 78,   # Post-traumatic Stress Disorder
        "PS": 75,   # Post-traumatic Stress Disorder Supplementary
        "MDS": 70,  # Marital Distress
        "APS": 55,  # Addiction Potential
        "AAS": 45,  # Addiction Acknowledgment
        "O-H": 40,  # Overcontrolled Hostility
        "MAC-R": 50, # MacAndrew Alcoholism Scale-Revised
        "FPTSD": 72  # Keane PTSD Scale
    }
    
    # Combine all scales
    profile_data["scales"] = {}
    profile_data["scales"].update(validity_scales)
    profile_data["scales"].update(clinical_scales)
    profile_data["scales"].update(harris_lingoes_subscales)
    profile_data["scales"].update(content_scales)
    profile_data["scales"].update(content_component_scales)
    profile_data["scales"].update(rc_scales)
    profile_data["scales"].update(psy5_scales)
    profile_data["scales"].update(supplementary_scales)
    
    # Add scale family groupings for easier processing
    profile_data["scale_families"] = {
        "validity_scales": validity_scales,
        "clinical_scales": clinical_scales,
        "harris_lingoes_subscales": harris_lingoes_subscales,
        "content_scales": content_scales,
        "content_component_scales": content_component_scales,
        "rc_scales": rc_scales,
        "psy5_scales": psy5_scales,
        "supplementary_scales": supplementary_scales
    }
    
    return profile_data

def create_traditional_profile_graph(profile_data, output_file):
    """
    Create a traditional MMPI-2 profile graph with validity and clinical scales.
    """
    # Extract validity and clinical scales
    validity_scales = profile_data["scale_families"]["validity_scales"]
    clinical_scales = profile_data["scale_families"]["clinical_scales"]
    
    # Set up the figure
    fig = plt.figure(figsize=(12, 8))
    fig.suptitle("MMPI-2 Profile: Validity and Clinical Scales", fontsize=16)
    
    # Create grid for subplots
    gs = gridspec.GridSpec(2, 1, height_ratios=[1, 2])
    
    # Validity scales subplot
    ax1 = plt.subplot(gs[0])
    validity_labels = ["VRIN", "TRIN", "F", "Fb", "Fp", "L", "K", "S"]
    validity_values = [validity_scales[scale] for scale in validity_labels]
    
    ax1.bar(validity_labels, validity_values, color='lightblue', edgecolor='black')
    ax1.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance (T=65)')
    ax1.set_ylabel('T-Score')
    ax1.set_title('Validity Scales')
    ax1.set_ylim(0, 120)
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add T-score values above bars
    for i, v in enumerate(validity_values):
        ax1.text(i, v + 3, str(v), ha='center')
    
    # Clinical scales subplot
    ax2 = plt.subplot(gs[1])
    clinical_labels = ["1 (Hs)", "2 (D)", "3 (Hy)", "4 (Pd)", "5 (Mf)", "6 (Pa)", "7 (Pt)", "8 (Sc)", "9 (Ma)", "0 (Si)"]
    clinical_values = [clinical_scales[scale] for scale in "1234567890"]
    
    # Highlight the two-point code (highest scales)
    colors = ['lightblue'] * 10
    sorted_indices = sorted(range(len(clinical_values)), key=lambda i: clinical_values[i], reverse=True)
    for i in sorted_indices[:2]:
        colors[i] = 'salmon'
    
    ax2.bar(clinical_labels, clinical_values, color=colors, edgecolor='black')
    ax2.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance (T=65)')
    ax2.set_ylabel('T-Score')
    ax2.set_title('Clinical Scales')
    ax2.set_ylim(0, 120)
    ax2.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Add T-score values above bars
    for i, v in enumerate(clinical_values):
        ax2.text(i, v + 3, str(v), ha='center')
    
    # Add legend
    ax2.legend()
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the figure
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    return output_file

def create_scale_family_graphs(profile_data, output_file):
    """
    Create separate graphs for each scale family.
    """
    # Extract scale families
    scale_families = profile_data["scale_families"]
    
    # Create a PDF with multiple pages
    with PdfPages(output_file) as pdf:
        # 1. RC Scales
        fig, ax = plt.subplots(figsize=(12, 6))
        rc_labels = ["RCd", "RC1", "RC2", "RC3", "RC4", "RC6", "RC7", "RC8", "RC9"]
        rc_values = [scale_families["rc_scales"][scale] for scale in rc_labels]
        
        ax.bar(rc_labels, rc_values, color='lightgreen', edgecolor='black')
        ax.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance (T=65)')
        ax.set_ylabel('T-Score')
        ax.set_title('Restructured Clinical (RC) Scales')
        ax.set_ylim(0, 120)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Add T-score values above bars
        for i, v in enumerate(rc_values):
            ax.text(i, v + 3, str(v), ha='center')
        
        ax.legend()
        plt.tight_layout()
        pdf.savefig()
        plt.close()
        
        # 2. Content Scales
        fig, ax = plt.subplots(figsize=(14, 6))
        content_labels = ["ANX", "FRS", "OBS", "DEP", "HEA", "BIZ", "ANG", "CYN", "ASP", "TPA", "LSE", "SOD", "FAM", "WRK", "TRT"]
        content_values = [scale_families["content_scales"][scale] for scale in content_labels]
        
        ax.bar(content_labels, content_values, color='lightsalmon', edgecolor='black')
        ax.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance (T=65)')
        ax.set_ylabel('T-Score')
        ax.set_title('Content Scales')
        ax.set_ylim(0, 120)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Add T-score values above bars
        for i, v in enumerate(content_values):
            ax.text(i, v + 3, str(v), ha='center')
        
        ax.legend()
        plt.tight_layout()
        pdf.savefig()
        plt.close()
        
        # 3. PSY-5 Scales
        fig, ax = plt.subplots(figsize=(10, 6))
        psy5_labels = ["AGGR", "PSYC", "DISC", "NEGE", "INTR"]
        psy5_values = [scale_families["psy5_scales"][scale] for scale in psy5_labels]
        
        ax.bar(psy5_labels, psy5_values, color='lightblue', edgecolor='black')
        ax.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance (T=65)')
        ax.set_ylabel('T-Score')
        ax.set_title('Personality Psychopathology Five (PSY-5) Scales')
        ax.set_ylim(0, 120)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Add T-score values above bars
        for i, v in enumerate(psy5_values):
            ax.text(i, v + 3, str(v), ha='center')
        
        ax.legend()
        plt.tight_layout()
        pdf.savefig()
        plt.close()
        
        # 4. Supplementary Scales
        fig, ax = plt.subplots(figsize=(14, 6))
        supp_labels = ["A", "R", "Es", "Do", "Re", "Mt", "GM", "GF", "PK", "PS", "MDS", "APS", "AAS", "O-H", "MAC-R", "FPTSD"]
        supp_values = [scale_families["supplementary_scales"][scale] for scale in supp_labels]
        
        ax.bar(supp_labels, supp_values, color='plum', edgecolor='black')
        ax.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance (T=65)')
        ax.set_ylabel('T-Score')
        ax.set_title('Supplementary Scales')
        ax.set_ylim(0, 120)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Add T-score values above bars
        for i, v in enumerate(supp_values):
            ax.text(i, v + 3, str(v), ha='center')
        
        ax.legend()
        plt.tight_layout()
        pdf.savefig()
        plt.close()
        
        # 5. Harris-Lingoes Subscales
        fig, ax = plt.subplots(figsize=(16, 8))
        hl_labels = ["D1", "D2", "D3", "D4", "D5", "Hy1", "Hy2", "Hy3", "Hy4", "Hy5", 
                     "Pd1", "Pd2", "Pd3", "Pd4", "Pd5", "Pa1", "Pa2", "Pa3", 
                     "Sc1", "Sc2", "Sc3", "Sc4", "Sc5", "Sc6", 
                     "Ma1", "Ma2", "Ma3", "Ma4", "Si1", "Si2", "Si3"]
        hl_values = [scale_families["harris_lingoes_subscales"][scale] for scale in hl_labels]
        
        ax.bar(hl_labels, hl_values, color='lightgrey', edgecolor='black')
        ax.axhline(y=65, color='r', linestyle='-', alpha=0.7, label='Clinical Significance (T=65)')
        ax.set_ylabel('T-Score')
        ax.set_title('Harris-Lingoes Subscales')
        ax.set_ylim(0, 120)
       
(Content truncated due to size limit. Use line ranges to read in chunks)
