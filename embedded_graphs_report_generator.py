#!/usr/bin/env python3
"""
Script to generate a comprehensive MMPI-2 report with embedded graphs within the narrative.
This enhanced version addresses formatting issues and embeds graphs at appropriate locations
within the report narrative.
"""

import os
import sys
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_pdf import PdfPages
from datetime import datetime
import base64
from weasyprint import HTML, CSS
from jinja2 import Template

# Add the project root to the Python path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import interpretation modules
from src.interpretation.scale_interpretations import get_scale_interpretation
from src.interpretation.dsm5tr_decision_trees import get_dsm5tr_diagnostic_impressions

# Output directory
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "embedded_graphs_report_output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Define a sample profile with clinically significant elevations
def create_clinical_profile():
    """Create a sample profile with clinically significant elevations across multiple scales."""
    profile_data = {
        "id": "EMBEDDED-GRAPHS-001",
        "name": "Sample Respondent",
        "age": 35,
        "gender": "Female",
        "date_tested": datetime.now().strftime("%Y-%m-%d"),
        "education": "College Graduate",
        "referral_source": "Self-referred",
        "presenting_concerns": "Anxiety, depression, difficulty concentrating",
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
            "1": 72,  # Hs
            "2": 80,  # D
            "3": 68,  # Hy
            "4": 65,  # Pd
            "5": 55,  # Mf
            "6": 62,  # Pa
            "7": 85,  # Pt
            "8": 70,  # Sc
            "9": 60,  # Ma
            "0": 68,  # Si
            
            # Harris-Lingoes Subscales
            "D1": 75,
            "D2": 78,
            "D3": 70,
            "D4": 65,
            "D5": 72,
            "Hy1": 60,
            "Hy2": 65,
            "Hy3": 70,
            "Hy4": 68,
            "Hy5": 55,
            "Pd1": 65,
            "Pd2": 70,
            "Pd3": 60,
            "Pd4": 65,
            "Pd5": 62,
            "Pa1": 65,
            "Pa2": 70,
            "Pa3": 60,
            "Sc1": 65,
            "Sc2": 70,
            "Sc3": 80,
            "Sc4": 65,
            "Sc5": 70,
            "Sc6": 74,
            "Ma1": 60,
            "Ma2": 65,
            "Ma3": 55,
            "Ma4": 60,
            
            # Content Scales
            "ANX": 78,
            "FRS": 65,
            "OBS": 72,
            "DEP": 80,
            "HEA": 70,
            "BIZ": 65,
            "ANG": 60,
            "CYN": 55,
            "ASP": 50,
            "TPA": 65,
            "LSE": 75,
            "SOD": 70,
            "FAM": 65,
            "WRK": 75,
            "TRT": 70,
            
            # RC Scales
            "RCd": 75,
            "RC1": 70,
            "RC2": 75,
            "RC3": 60,
            "RC4": 65,
            "RC6": 60,
            "RC7": 80,
            "RC8": 65,
            "RC9": 55,
            
            # PSY-5 Scales
            "AGGR": 55,
            "PSYC": 65,
            "DISC": 50,
            "NEGE": 80,
            "INTR": 70,
            
            # Supplementary Scales
            "A": 75,
            "R": 65,
            "Es": 40,
            "Do": 45,
            "Re": 50,
            "Mt": 70,
            "GM": 50,
            "GF": 55,
            "PK": 75,
            "PS": 70,
            "MDS": 65,
            "APS": 55,
            "AAS": 50,
            "MAC-R": 60,
            "O-H": 45
        }
    }
    return profile_data

def generate_traditional_profile_graph(profile_data, output_path):
    """Generate a traditional MMPI-2 profile graph with validity and clinical scales."""
    # Extract scores
    validity_scales = ["L", "F", "K"]
    clinical_scales = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    
    validity_scores = [profile_data["scale_scores"][scale] for scale in validity_scales]
    clinical_scores = [profile_data["scale_scores"][scale] for scale in clinical_scales]
    
    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # X-axis positions
    x_validity = np.arange(len(validity_scales))
    x_clinical = np.arange(len(clinical_scales)) + len(validity_scales) + 1
    
    # Plot bars
    validity_bars = ax.bar(x_validity, validity_scores, color='lightblue', width=0.7)
    clinical_bars = ax.bar(x_clinical, clinical_scores, color='lightgreen', width=0.7)
    
    # Highlight clinically significant elevations (T >= 65)
    for i, score in enumerate(validity_scores):
        if score >= 65:
            validity_bars[i].set_color('salmon')
    
    for i, score in enumerate(clinical_scores):
        if score >= 65:
            clinical_bars[i].set_color('salmon')
    
    # Add T-score reference lines
    ax.axhline(y=50, color='black', linestyle='-', alpha=0.3)
    ax.axhline(y=65, color='red', linestyle='--', alpha=0.5)
    ax.axhline(y=80, color='red', linestyle='-', alpha=0.5)
    
    # Set axis labels and title
    ax.set_ylabel('T-Score')
    ax.set_title('MMPI-2 Profile: Validity and Clinical Scales')
    
    # Set x-tick labels
    all_labels = validity_scales + [""] + clinical_scales
    all_positions = list(x_validity) + [len(validity_scales)] + list(x_clinical)
    ax.set_xticks(all_positions)
    ax.set_xticklabels(all_labels)
    
    # Add T-score values above bars
    for i, score in enumerate(validity_scores):
        ax.text(x_validity[i], score + 1, str(score), ha='center')
    
    for i, score in enumerate(clinical_scores):
        ax.text(x_clinical[i], score + 1, str(score), ha='center')
    
    # Set y-axis limits
    ax.set_ylim(0, max(max(validity_scores), max(clinical_scores)) + 10)
    
    # Add legend
    ax.legend([validity_bars[0], clinical_bars[0]], ['Validity Scales', 'Clinical Scales'])
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    
    return output_path

def generate_scale_family_graph(profile_data, scale_family, output_path):
    """Generate a graph for a specific scale family."""
    scale_family_mapping = {
        "validity": {
            "scales": ["?", "VRIN", "TRIN", "F", "Fb", "Fp", "FBS", "L", "K"],
            "title": "Validity Scales",
            "color": "lightblue"
        },
        "clinical": {
            "scales": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            "title": "Clinical Scales",
            "color": "lightgreen"
        },
        "harris_lingoes": {
            "scales": ["D1", "D2", "D3", "D4", "D5", "Hy1", "Hy2", "Hy3", "Hy4", "Hy5", 
                      "Pd1", "Pd2", "Pd3", "Pd4", "Pd5", "Pa1", "Pa2", "Pa3", 
                      "Sc1", "Sc2", "Sc3", "Sc4", "Sc5", "Sc6", "Ma1", "Ma2", "Ma3", "Ma4"],
            "title": "Harris-Lingoes Subscales",
            "color": "lightyellow"
        },
        "content": {
            "scales": ["ANX", "FRS", "OBS", "DEP", "HEA", "BIZ", "ANG", "CYN", "ASP", "TPA", "LSE", "SOD", "FAM", "WRK", "TRT"],
            "title": "Content Scales",
            "color": "lightcoral"
        },
        "rc": {
            "scales": ["RCd", "RC1", "RC2", "RC3", "RC4", "RC6", "RC7", "RC8", "RC9"],
            "title": "Restructured Clinical (RC) Scales",
            "color": "lightgreen"
        },
        "psy5": {
            "scales": ["AGGR", "PSYC", "DISC", "NEGE", "INTR"],
            "title": "PSY-5 Scales",
            "color": "lightpink"
        },
        "supplementary": {
            "scales": ["A", "R", "Es", "Do", "Re", "Mt", "GM", "GF", "PK", "PS", "MDS", "APS", "AAS", "MAC-R", "O-H"],
            "title": "Supplementary Scales",
            "color": "lightgrey"
        }
    }
    
    if scale_family not in scale_family_mapping:
        raise ValueError(f"Unknown scale family: {scale_family}")
    
    scales = scale_family_mapping[scale_family]["scales"]
    title = scale_family_mapping[scale_family]["title"]
    color = scale_family_mapping[scale_family]["color"]
    
    # Extract scores
    scores = []
    for scale in scales:
        if scale in profile_data["scale_scores"]:
            scores.append(profile_data["scale_scores"][scale])
        else:
            scores.append(0)  # Default if scale not found
    
    # Create figure
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # X-axis positions
    x_pos = np.arange(len(scales))
    
    # Plot bars
    bars = ax.bar(x_pos, scores, color=color, width=0.7)
    
    # Highlight clinically significant elevations (T >= 65)
    for i, score in enumerate(scores):
        if score >= 65:
            bars[i].set_color('salmon')
    
    # Add T-score reference lines
    ax.axhline(y=50, color='black', linestyle='-', alpha=0.3)
    ax.axhline(y=65, color='red', linestyle='--', alpha=0.5)
    ax.axhline(y=80, color='red', linestyle='-', alpha=0.5)
    
    # Set axis labels and title
    ax.set_ylabel('T-Score')
    ax.set_title(f'MMPI-2 {title}')
    
    # Set x-tick labels
    ax.set_xticks(x_pos)
    ax.set_xticklabels(scales, rotation=45 if len(scales) > 10 else 0)
    
    # Add T-score values above bars
    for i, score in enumerate(scores):
        ax.text(x_pos[i], score + 1, str(score), ha='center')
    
    # Set y-axis limits
    ax.set_ylim(0, max(scores) + 10)
    
    # Adjust layout and save
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    
    return output_path

def generate_all_graphs(profile_data):
    """Generate all graphs for the report."""
    graph_paths = {}
    
    # Traditional profile graph
    traditional_graph_path = os.path.join(OUTPUT_DIR, "traditional_profile_graph.png")
    graph_paths["traditional"] = generate_traditional_profile_graph(profile_data, traditional_graph_path)
    
    # Scale family graphs
    scale_families = ["validity", "clinical", "harris_lingoes", "content", "rc", "psy5", "supplementary"]
    for family in scale_families:
        output_path = os.path.join(OUTPUT_DIR, f"{family}_scales_graph.png")
        graph_paths[family] = generate_scale_family_graph(profile_data, family, output_path)
    
    return graph_paths

def get_two_point_code(profile_data):
    """Determine the two-point code from clinical scales."""
    clinical_scales = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    clinical_scores = [(scale, profile_data["scale_scores"][scale]) for scale in clinical_scales]
    
    # Sort by T-score (descending)
    sorted_scores = sorted(clinical_scores, key=lambda x: x[1], reverse=True)
    
    # Get top two scales
    top_two = sorted_scores[:2]
    
    # Format as X-Y code
    code = f"{top_two[0][0]}-{top_two[1][0]}"
    
    return code, top_two[0][1], top_two[1][1]

def generate_html_report(profile_data, graph_paths):
    """Generate an HTML report with embedded graphs."""
    # Get interpretations for all scale families
    interpretations = {}
    scale_scores = profile_data["scale_scores"]
    gender = profile_data["gender"]
    
    # Get validity scale interpretations
    validity_scales = ["?", "VRIN", "TRIN", "F", "Fb", "Fp", "FBS", "L", "K"]
    interpretations["validity"] = {scale: get_scale_interpretation(scale, scale_scores[scale], "VALIDITY", gender=gender) for scale in validity_scales}
    
    # Get clinical scale interpretations
    clinical_scales = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    interpretations["clinical"] = {scale: get_scale_interpretation(scale, scale_scores[scale], "CLINICAL", gender=gender) for scale in clinical_scales}
    
    # Get Harris-Lingoes subscale interpretations
    harris_lingoes_scales = ["D1", "D2", "D3", "D4", "D5", "Hy1", "Hy2", "Hy3", "Hy4", "Hy5", 
                           "Pd1", "Pd2", "Pd3", "Pd4", "Pd5", "Pa1", "Pa2", "Pa3", 
                           "Sc1", "Sc2", "Sc3", "Sc4", "Sc5", "Sc6", "Ma1", "Ma2", "Ma3", "Ma4"]
    interpretations["harris_lingoes"] = {scale: get_scale_interpretation(scale, scale_scores[scale], "HARRIS_LINGOES", gender=gender) for scale in harris_lingoes_scales}
    
    # Get Content scale interpretations
    content_scales = ["ANX", "FRS", "OBS", "DEP", "HEA", "BIZ", "ANG", "CYN", "ASP", "TPA", "LSE", "SOD", "FAM", "WRK", "TRT"]
    interpretations["content"] = {scale: get_scale_interpretation(scale, scale_scores[scale], "CONTENT", gender=gender) for scale in content_scales}
    
    # Get RC scale interpretations
    rc_scales = ["RCd", "RC1", "RC2", "RC3", "RC4", "RC6", "RC7", "RC8", "RC9"]
    interpretations["rc"] = {scale: get_scale_interpretation(scale, scale_scores[scale], "RC", gender=gender) for scale in rc_scales}
    
    # Get PSY-5 scale interpretations
    psy5_scales = ["AGGR", "PSYC", "DISC", "NEGE", "INTR"]
    interpretations["psy5"] = {scale: get_scale_interpretation(scale, scale_scores[scale], "PSY5", gender=gender) for scale in psy5_scales}
    
    # Get Supplementary scale interpretations
    supplementary_scales = ["A", "R", "Es", "Do", "Re", "Mt", "GM", "GF", "PK", "PS", "MDS", "APS", "AAS", "MAC-R", "O-H"]
    interpretations["supplementary"] = {scale: get_scale_interpretation(scale, scale_scores[scale], "SUPPLEMENTARY", gender=gender) for scale in supplementary_scales}
    
    # Get two-point code
    two_point_code, code_score1, code_score2 = get_two_point_code(profile_data)
    
    # Get DSM-5-TR diagnostic impressions
    dsm5tr_impressions = get_dsm5tr_diagnostic_impressions(profile_data)
    
    # Create summaries for each scale family
    summaries = {
        "validity": "The validity scales suggest a valid profile with possible slight exaggeration of symptoms. The elevated F scale (T=68) indicates acknowledgment of significant psychological distress, while the low K scale (T=40) suggests limited psychological resources and poor self-concept. The profile is likely an accurate representation of the respondent's current psychological functioning.",
        
        "clinical": f"The clinical scales show significant elevations on Scale 7 (Psychasthenia, T=85), Scale 2 (Depression, T=80), Scale 1 (Hypochondriasis, T=72), and Scale 8 (Schizophrenia, T=70). This {two_point_code} profile suggests a person experiencing significant anxiety and depression with somatic concerns and possible cognitive difficulties. The individual likely feels overwhelmed, worried, and may have trouble concentrating.",
        
        "harris_lingoes": "The Harris-Lingoes subscales provide additional detail about the clinical scale elevations. The D1 (Subjective Depression) and D2 (Psychomotor Retardation) elevations confirm significant depressive symptoms. The Sc3 (Lack of Ego Mastery, Cognitive) and Sc6 (Bizarre Sensory Experiences) elevations suggest cognitive difficulties and possible unusual perceptual experiences under stress.",
        
        "content": "The Content scales show significant elevations on ANX (Anxiety, T=78), DEP (Depression, T=80), and LSE (Low Self-Esteem, T=75). These elevations are consistent with the clinical scale findings and suggest significant anxiety, depression, and negative self-evaluation. The WRK (Work Interference, T=75) elevation indicates that these symptoms are likely affecting occupational functioning.",
        
        "rc": "The RC scales show significant elevations on RCd (Demoralization, T=75), RC2 (Low Positive Emotions, T=75), and RC7 (Dysfunctional Negative Emotions, T=80). These elevations are consistent with the clinical scale findings and suggest significant demoralization, anhedonia, and negative emotionality.",
        
        "psy5": "The PS
(Content truncated due to size limit. Use line ranges to read in chunks)
