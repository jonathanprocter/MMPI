#!/usr/bin/env python3
"""
Script to generate a final comprehensive MMPI-2 report with all enhancements.

This script validates that all interpretation modules can be imported correctly
and generates a comprehensive report with narrative interpretations, embedded graphs,
and DSM-5-TR diagnostic impressions.
"""

import os
import sys
import json
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
from datetime import datetime

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import interpretation modules
from src.interpretation.clinical_scales import get_clinical_scale_interpretation
from src.interpretation.content_scales import get_content_scale_interpretation
from src.interpretation.content_component_scales import get_content_component_scale_interpretation
from src.interpretation.harris_lingoes_subscales import get_harris_lingoes_subscale_interpretation
from src.interpretation.rc_scales import get_rc_scale_interpretation
from src.interpretation.validity_scales import get_validity_scale_interpretation
from src.interpretation.supplementary_scales import get_supplementary_scale_interpretation
from src.interpretation.psy5_scales import get_psy5_scale_interpretation
from src.interpretation.component_scales import get_component_scale_interpretation
from src.interpretation.dsm5tr_decision_trees import get_dsm5tr_diagnostic_impressions

# Create output directory
OUTPUT_DIR = Path("final_comprehensive_output")
OUTPUT_DIR.mkdir(exist_ok=True)

def create_sample_profile():
    """
    Create a sample profile with clinically significant elevations across multiple scales.
    
    Returns:
        dict: A dictionary containing the sample profile data
    """
    return {
        "respondent_id": "final_comprehensive",
        "name": "Sample Respondent",
        "age": 35,
        "gender": "Female",
        "date_tested": datetime.now().strftime("%Y-%m-%d"),
        "scale_scores": {
            # Validity Scales
            "VRIN": 55,
            "TRIN": 57,
            "F": 75,
            "Fb": 72,
            "Fp": 65,
            "L": 45,
            "K": 40,
            "S": 38,
            
            # Clinical Scales
            "1": 78,  # Hs (Hypochondriasis)
            "2": 82,  # D (Depression)
            "3": 65,  # Hy (Hysteria)
            "4": 70,  # Pd (Psychopathic Deviate)
            "5": 55,  # Mf (Masculinity-Femininity)
            "6": 68,  # Pa (Paranoia)
            "7": 80,  # Pt (Psychasthenia)
            "8": 74,  # Sc (Schizophrenia)
            "9": 60,  # Ma (Hypomania)
            "0": 72,  # Si (Social Introversion)
            
            # Harris-Lingoes Subscales
            "D1": 75,  # Subjective Depression
            "D2": 70,  # Psychomotor Retardation
            "D3": 65,  # Physical Malfunctioning
            "D4": 72,  # Mental Dullness
            "D5": 68,  # Brooding
            "Hy1": 60,  # Denial of Social Anxiety
            "Hy2": 65,  # Need for Affection
            "Hy3": 75,  # Lassitude-Malaise
            "Hy4": 70,  # Somatic Complaints
            "Hy5": 65,  # Inhibition of Aggression
            "Pd1": 72,  # Familial Discord
            "Pd2": 68,  # Authority Problems
            "Pd3": 65,  # Social Imperturbability
            "Pd4": 70,  # Social Alienation
            "Pd5": 75,  # Self-Alienation
            "Pa1": 72,  # Persecutory Ideas
            "Pa2": 68,  # Poignancy
            "Pa3": 65,  # Naivete
            "Sc1": 75,  # Social Alienation
            "Sc2": 70,  # Emotional Alienation
            "Sc3": 80,  # Lack of Ego Mastery, Cognitive
            "Sc4": 75,  # Lack of Ego Mastery, Conative
            "Sc5": 70,  # Lack of Ego Mastery, Defective Inhibition
            "Sc6": 74,  # Bizarre Sensory Experiences
            "Ma1": 65,  # Amorality
            "Ma2": 60,  # Psychomotor Acceleration
            "Ma3": 55,  # Imperturbability
            "Ma4": 62,  # Ego Inflation
            "Si1": 75,  # Shyness/Self-Consciousness
            "Si2": 70,  # Social Avoidance
            "Si3": 65,  # Self/Other Alienation
            
            # Content Scales
            "ANX": 78,  # Anxiety
            "FRS": 65,  # Fears
            "OBS": 72,  # Obsessiveness
            "DEP": 80,  # Depression
            "HEA": 75,  # Health Concerns
            "BIZ": 68,  # Bizarre Mentation
            "ANG": 70,  # Anger
            "CYN": 65,  # Cynicism
            "ASP": 60,  # Antisocial Practices
            "TPA": 72,  # Type A
            "LSE": 75,  # Low Self-Esteem
            "SOD": 78,  # Social Discomfort
            "FAM": 70,  # Family Problems
            "WRK": 75,  # Work Interference
            "TRT": 72,  # Negative Treatment Indicators
            
            # Content Component Scales
            "ANX1": 75,  # Generalized Anxiety
            "ANX2": 70,  # Phobic Anxiety
            "ANX3": 78,  # Worry/Rumination
            "FRS1": 65,  # Generalized Fearfulness
            "FRS2": 60,  # Multiple Fears
            "OBS1": 72,  # Obsessiveness
            "OBS2": 70,  # Indecisiveness
            "DEP1": 80,  # Lack of Drive
            "DEP2": 75,  # Dysphoria
            "DEP3": 78,  # Self-Depreciation
            "DEP4": 72,  # Suicidal Ideation
            "HEA1": 75,  # Gastrointestinal Symptoms
            "HEA2": 70,  # Neurological Symptoms
            "HEA3": 68,  # General Health Concerns
            "BIZ1": 65,  # Psychotic Symptomatology
            "BIZ2": 62,  # Schizotypal Characteristics
            "ANG1": 70,  # Explosive Behavior
            "ANG2": 68,  # Irritability
            "CYN1": 65,  # Misanthropic Beliefs
            "CYN2": 62,  # Interpersonal Suspiciousness
            "ASP1": 60,  # Antisocial Attitudes
            "ASP2": 58,  # Antisocial Behavior
            "TPA1": 72,  # Impatience
            "TPA2": 70,  # Competitive Drive
            "LSE1": 75,  # Self-Doubt
            "LSE2": 72,  # Submissiveness
            "SOD1": 78,  # Introversion
            "SOD2": 75,  # Shyness
            "FAM1": 70,  # Family Discord
            "FAM2": 68,  # Family Alienation
            "WRK1": 75,  # Work Inefficiency
            "WRK2": 72,  # Lack of Work Motivation
            "TRT1": 70,  # Low Motivation for Treatment
            "TRT2": 68,  # Inability to Disclose
            
            # RC Scales
            "RCd": 80,  # Demoralization
            "RC1": 75,  # Somatic Complaints
            "RC2": 78,  # Low Positive Emotions
            "RC3": 65,  # Cynicism
            "RC4": 70,  # Antisocial Behavior
            "RC6": 68,  # Ideas of Persecution
            "RC7": 80,  # Dysfunctional Negative Emotions
            "RC8": 72,  # Aberrant Experiences
            "RC9": 60,  # Hypomanic Activation
            
            # PSY-5 Scales
            "AGGR": 65,  # Aggressiveness
            "PSYC": 70,  # Psychoticism
            "DISC": 60,  # Disconstraint
            "NEGE": 78,  # Negative Emotionality/Neuroticism
            "INTR": 75,  # Introversion/Low Positive Emotionality
            
            # Supplementary Scales
            "A": 72,  # Anxiety
            "R": 70,  # Repression
            "Es": 45,  # Ego Strength
            "Do": 48,  # Dominance
            "Re": 50,  # Social Responsibility
            "Mt": 75,  # College Maladjustment
            "GM": 55,  # Gender Role - Masculine
            "GF": 60,  # Gender Role - Feminine
            "PK": 72,  # PTSD - Keane
            "PS": 70,  # PTSD - Schlenger
            "MDS": 68,  # Marital Distress
            "AAS": 55,  # Addiction Acknowledgment
            "APS": 52,  # Addiction Potential
            "MAC-R": 58,  # MacAndrew Alcoholism-Revised
            "O-H": 45,  # Overcontrolled Hostility
            "FBS": 65,  # Symptom Validity
        }
    }

def generate_scale_family_graphs(profile_data, output_dir):
    """
    Generate graphs for all scale families.
    
    Args:
        profile_data (dict): The profile data dictionary
        output_dir (Path): Directory to save the graphs
        
    Returns:
        list: Paths to the generated graph files
    """
    scale_scores = profile_data["scale_scores"]
    graph_files = []
    
    # Define scale families
    scale_families = {
        "validity": ["VRIN", "TRIN", "F", "Fb", "Fp", "L", "K", "S"],
        "clinical": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
        "rc": ["RCd", "RC1", "RC2", "RC3", "RC4", "RC6", "RC7", "RC8", "RC9"],
        "content": ["ANX", "FRS", "OBS", "DEP", "HEA", "BIZ", "ANG", "CYN", "ASP", "TPA", "LSE", "SOD", "FAM", "WRK", "TRT"],
        "psy5": ["AGGR", "PSYC", "DISC", "NEGE", "INTR"],
        "supplementary": ["A", "R", "Es", "Do", "Re", "Mt", "PK", "PS", "MDS", "AAS", "APS", "MAC-R", "O-H", "FBS"]
    }
    
    # Generate traditional profile graph (Validity + Clinical)
    plt.figure(figsize=(12, 8))
    
    # Combine validity and clinical scales
    traditional_scales = scale_families["validity"] + scale_families["clinical"]
    traditional_scores = [scale_scores.get(scale, 0) for scale in traditional_scales]
    
    # Create x-axis labels
    x = np.arange(len(traditional_scales))
    
    # Plot bars
    bars = plt.bar(x, traditional_scores, width=0.6)
    
    # Color code by clinical significance
    for i, bar in enumerate(bars):
        if traditional_scores[i] >= 65:
            bar.set_color('red')
        elif traditional_scores[i] >= 55:
            bar.set_color('orange')
        else:
            bar.set_color('blue')
    
    # Add horizontal lines at T-scores 50, 65, and 80
    plt.axhline(y=50, color='black', linestyle='-', alpha=0.3)
    plt.axhline(y=65, color='red', linestyle='--', alpha=0.5)
    plt.axhline(y=80, color='red', linestyle='-', alpha=0.5)
    
    # Set axis labels and title
    plt.xlabel('Scales')
    plt.ylabel('T-Score')
    plt.title('MMPI-2 Traditional Profile (Validity and Clinical Scales)')
    
    # Set y-axis limits
    plt.ylim(30, 100)
    
    # Set x-axis ticks and labels
    plt.xticks(x, traditional_scales, rotation=45)
    
    # Add T-score values above bars
    for i, v in enumerate(traditional_scores):
        plt.text(i, v + 2, str(v), ha='center')
    
    # Adjust layout and save
    plt.tight_layout()
    traditional_graph_path = output_dir / "traditional_profile_graph.png"
    plt.savefig(traditional_graph_path)
    plt.close()
    graph_files.append(traditional_graph_path)
    
    # Generate individual graphs for each scale family
    for family_name, scales in scale_families.items():
        plt.figure(figsize=(12, 6))
        
        scores = [scale_scores.get(scale, 0) for scale in scales]
        x = np.arange(len(scales))
        
        # Plot bars
        bars = plt.bar(x, scores, width=0.6)
        
        # Color code by clinical significance
        for i, bar in enumerate(bars):
            if scores[i] >= 65:
                bar.set_color('red')
            elif scores[i] >= 55:
                bar.set_color('orange')
            else:
                bar.set_color('blue')
        
        # Add horizontal lines at T-scores 50, 65, and 80
        plt.axhline(y=50, color='black', linestyle='-', alpha=0.3)
        plt.axhline(y=65, color='red', linestyle='--', alpha=0.5)
        plt.axhline(y=80, color='red', linestyle='-', alpha=0.5)
        
        # Set axis labels and title
        plt.xlabel('Scales')
        plt.ylabel('T-Score')
        plt.title(f'MMPI-2 {family_name.title()} Scales')
        
        # Set y-axis limits
        plt.ylim(30, 100)
        
        # Set x-axis ticks and labels
        plt.xticks(x, scales, rotation=45)
        
        # Add T-score values above bars
        for i, v in enumerate(scores):
            plt.text(i, v + 2, str(v), ha='center')
        
        # Adjust layout and save
        plt.tight_layout()
        family_graph_path = output_dir / f"{family_name}_scales_graph.png"
        plt.savefig(family_graph_path)
        plt.close()
        graph_files.append(family_graph_path)
    
    # Combine all graphs into a single PDF
    combined_graph_path = output_dir / "scale_family_graphs.pdf"
    
    # Create a combined PDF with all graphs using matplotlib's PdfPages
    import matplotlib.backends.backend_pdf
    pdf = matplotlib.backends.backend_pdf.PdfPages(combined_graph_path)
    
    # Add each graph to the PDF directly
    # Traditional profile graph
    fig = plt.figure(figsize=(12, 8))
    plt.figure(figsize=(12, 8))
    
    # Combine validity and clinical scales again for the PDF
    traditional_scales = scale_families["validity"] + scale_families["clinical"]
    traditional_scores = [scale_scores.get(scale, 0) for scale in traditional_scales]
    
    # Create x-axis labels
    x = np.arange(len(traditional_scales))
    
    # Plot bars
    bars = plt.bar(x, traditional_scores, width=0.6)
    
    # Color code by clinical significance
    for i, bar in enumerate(bars):
        if traditional_scores[i] >= 65:
            bar.set_color('red')
        elif traditional_scores[i] >= 55:
            bar.set_color('orange')
        else:
            bar.set_color('blue')
    
    # Add horizontal lines at T-scores 50, 65, and 80
    plt.axhline(y=50, color='black', linestyle='-', alpha=0.3)
    plt.axhline(y=65, color='red', linestyle='--', alpha=0.5)
    plt.axhline(y=80, color='red', linestyle='-', alpha=0.5)
    
    # Set axis labels and title
    plt.xlabel('Scales')
    plt.ylabel('T-Score')
    plt.title('MMPI-2 Traditional Profile (Validity and Clinical Scales)')
    
    # Set y-axis limits
    plt.ylim(30, 100)
    
    # Set x-axis ticks and labels
    plt.xticks(x, traditional_scales, rotation=45)
    
    # Add T-score values above bars
    for i, v in enumerate(traditional_scores):
        plt.text(i, v + 2, str(v), ha='center')
    
    # Adjust layout and save to PDF
    plt.tight_layout()
    pdf.savefig()
    plt.close()
    
    # Add individual scale family graphs to the PDF
    for family_name, scales in scale_families.items():
        plt.figure(figsize=(12, 6))
        
        scores = [scale_scores.get(scale, 0) for scale in scales]
        x = np.arange(len(scales))
        
        # Plot bars
        bars = plt.bar(x, scores, width=0.6)
        
        # Color code by clinical significance
        for i, bar in enumerate(bars):
            if scores[i] >= 65:
                bar.set_color('red')
            elif scores[i] >= 55:
                bar.set_color('orange')
            else:
                bar.set_color('blue')
        
        # Add horizontal lines at T-scores 50, 65, and 80
        plt.axhline(y=50, color='black', linestyle='-', alpha=0.3)
        plt.axhline(y=65, color='red', linestyle='--', alpha=0.5)
        plt.axhline(y=80, color='red', linestyle='-', alpha=0.5)
        
        # Set axis labels and title
        plt.xlabel('Scales')
        plt.ylabel('T-Score')
        plt.title(f'MMPI-2 {family_name.title()} Scales')
        
        # Set y-axis limits
        plt.ylim(30, 100)
        
        # Set x-axis ticks and labels
        plt.xticks(x, scales, rotation=45)
        
        # Add T-score values above bars
        for i, v in enumerate(scores):
            plt.text(i, v + 2, str(v), ha='center')
        
        # Adjust layout and save to PDF
        plt.tight_layout()
        pdf.savefig()
        plt.close()
    
    pdf.close()
    graph_files.append(combined_graph_path)
    
    return graph_files


def generate_comprehensive_report(profile_data, output_dir):
    """Placeholder implementation for generating a comprehensive report."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "final_report.txt")
    with open(path, "w") as f:
        f.write("Report generation not fully implemented.")
    return {"text": path}

