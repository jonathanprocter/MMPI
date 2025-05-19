"""
Enhanced graphical profile generator for MMPI-2 reports using web-compatible methods.
This module creates profile graphs without using Pillow/PIL dependencies.
"""

import os
import json
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

class ProfileGraphGenerator:
    """
    Generates graphical representations of MMPI-2 profiles using web-compatible methods.
    """
    
    def __init__(self, output_dir):
        """
        Initialize the profile graph generator.
        
        Args:
            output_dir (str): Directory to save generated graphs
        """
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Set matplotlib style for clinical appearance
        plt.style.use('ggplot')
        self.fig_size = (10, 8)
        self.dpi = 100
        
    def generate_all_graphs(self, scores, client_info):
        """
        Generate all profile graphs for the MMPI-2 report.
        
        Args:
            scores (dict): Dictionary containing all scale scores
            client_info (dict): Dictionary containing client information
            
        Returns:
            dict: Dictionary of paths to generated graph files
        """
        graph_paths = {}
        
        # Generate traditional profile graph
        graph_paths['traditional'] = self.generate_traditional_profile_graph(
            scores['clinical_scales'], 
            client_info
        )
        
        # Generate RC scales graph
        graph_paths['rc_scales'] = self.generate_rc_scales_graph(
            scores['rc_scales'], 
            client_info
        )
        
        # Generate content scales graph
        graph_paths['content_scales'] = self.generate_content_scales_graph(
            scores['content_scales'], 
            client_info
        )
        
        # Generate PSY-5 scales graph
        graph_paths['psy5_scales'] = self.generate_psy5_scales_graph(
            scores['psy5_scales'], 
            client_info
        )
        
        # Generate supplementary scales graph
        graph_paths['supplementary_scales'] = self.generate_supplementary_scales_graph(
            scores['supplementary_scales'], 
            client_info
        )
        
        # Combine all graphs into a single PDF
        graph_paths['all_graphs'] = self.combine_graphs_to_pdf(graph_paths, client_info)
        
        return graph_paths
    
    def generate_traditional_profile_graph(self, clinical_scales, client_info):
        """
        Generate traditional MMPI-2 profile graph.
        
        Args:
            clinical_scales (dict): Dictionary of clinical scale scores
            client_info (dict): Dictionary containing client information
            
        Returns:
            str: Path to generated graph file
        """
        # Create figure and axis
        fig, ax = plt.subplots(figsize=self.fig_size, dpi=self.dpi)
        
        # Define scales and their order
        scale_names = ['L', 'F', 'K', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        scale_labels = ['L', 'F', 'K', 'Hs', 'D', 'Hy', 'Pd', 'Mf', 'Pa', 'Pt', 'Sc', 'Ma', 'Si']
        
        # Extract scores in correct order
        scores = []
        for scale in scale_names:
            if scale in clinical_scales:
                scores.append(clinical_scales[scale])
            else:
                scores.append(50)  # Default value if missing
        
        # Create x-axis positions
        x_pos = np.arange(len(scale_labels))
        
        # Plot scores
        ax.plot(x_pos, scores, 'b-o', linewidth=1.5, markersize=6)
        
        # Set axis limits
        ax.set_ylim(30, 120)
        ax.set_xlim(-0.5, len(scale_labels) - 0.5)
        
        # Add clinical significance lines
        ax.axhline(y=65, color='r', linestyle='-', linewidth=2)
        ax.axhline(y=50, color='r', linestyle='-', linewidth=2)
        
        # Set grid
        ax.grid(True, linestyle='-', alpha=0.7)
        ax.set_axisbelow(True)
        
        # Set ticks and labels
        ax.set_xticks(x_pos)
        ax.set_xticklabels(scale_labels)
        
        # Y-axis ticks every 10 units
        ax.yaxis.set_major_locator(MultipleLocator(10))
        
        # Add title
        name = client_info.get('name', 'Client')
        sex = client_info.get('sex', 'female')
        sex_label = 'Female' if sex == 'female' else 'Male'
        title = f"MMPI-2 Clinical Scales Profile: {name} ({sex_label})"
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        # Add labels
        ax.set_ylabel('T-Score', fontsize=12)
        
        # Add raw scores above graph
        for i, score in enumerate(scores):
            ax.text(i, 122, str(score), ha='center', va='bottom', fontsize=10)
        
        # Add "Raw Score:" label
        ax.text(-0.5, 122, "T-Score:", ha='right', va='bottom', fontsize=10)
        
        # Adjust layout
        plt.tight_layout()
        
        # Save figure
        output_path = os.path.join(self.output_dir, 'traditional_profile_graph.png')
        plt.savefig(output_path, bbox_inches='tight')
        plt.close(fig)
        
        return output_path
    
    def generate_rc_scales_graph(self, rc_scales, client_info):
        """
        Generate RC scales graph.
        
        Args:
            rc_scales (dict): Dictionary of RC scale scores
            client_info (dict): Dictionary containing client information
            
        Returns:
            str: Path to generated graph file
        """
        # Create figure and axis
        fig, ax = plt.subplots(figsize=self.fig_size, dpi=self.dpi)
        
        # Define RC scales and their full names
        rc_scale_names = ['RCd', 'RC1', 'RC2', 'RC3', 'RC4', 'RC6', 'RC7', 'RC8', 'RC9']
        rc_scale_full_names = {
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
        
        # Extract scores in correct order
        scores = []
        for scale in rc_scale_names:
            if scale in rc_scales:
                scores.append(rc_scales[scale])
            else:
                scores.append(50)  # Default value if missing
        
        # Create x-axis positions
        x_pos = np.arange(len(rc_scale_names))
        
        # Plot scores
        ax.plot(x_pos, scores, 'b-o', linewidth=1.5, markersize=6)
        
        # Set axis limits
        ax.set_ylim(30, 120)
        ax.set_xlim(-0.5, len(rc_scale_names) - 0.5)
        
        # Add clinical significance lines
        ax.axhline(y=65, color='r', linestyle='-', linewidth=2)
        ax.axhline(y=50, color='r', linestyle='-', linewidth=2)
        
        # Set grid
        ax.grid(True, linestyle='-', alpha=0.7)
        ax.set_axisbelow(True)
        
        # Set ticks and labels
        ax.set_xticks(x_pos)
        ax.set_xticklabels(rc_scale_names)
        
        # Y-axis ticks every 10 units
        ax.yaxis.set_major_locator(MultipleLocator(10))
        
        # Add title
        name = client_info.get('name', 'Client')
        sex = client_info.get('sex', 'female')
        sex_label = 'Female' if sex == 'female' else 'Male'
        title = f"MMPI-2 Restructured Clinical (RC) Scales: {name} ({sex_label})"
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        # Add labels
        ax.set_ylabel('T-Score', fontsize=12)
        
        # Add raw scores above graph
        for i, score in enumerate(scores):
            ax.text(i, 122, str(score), ha='center', va='bottom', fontsize=10)
        
        # Add "Raw Score:" label
        ax.text(-0.5, 122, "T-Score:", ha='right', va='bottom', fontsize=10)
        
        # Add RC scale full names as a table below the graph
        table_data = []
        for scale in rc_scale_names:
            table_data.append([scale, rc_scale_full_names.get(scale, '')])
        
        table = ax.table(cellText=table_data, 
                         colLabels=['Scale', 'Full Name'],
                         loc='bottom', 
                         cellLoc='center',
                         bbox=[0, -0.4, 1, 0.2])
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 1.5)
        
        # Adjust layout
        plt.subplots_adjust(bottom=0.25)
        
        # Save figure
        output_path = os.path.join(self.output_dir, 'rc_scales_graph.png')
        plt.savefig(output_path, bbox_inches='tight')
        plt.close(fig)
        
        return output_path
    
    def generate_content_scales_graph(self, content_scales, client_info):
        """
        Generate content scales graph.
        
        Args:
            content_scales (dict): Dictionary of content scale scores
            client_info (dict): Dictionary containing client information
            
        Returns:
            str: Path to generated graph file
        """
        # Create figure and axis
        fig, ax = plt.subplots(figsize=self.fig_size, dpi=self.dpi)
        
        # Define content scales
        content_scale_names = ['ANX', 'FRS', 'OBS', 'DEP', 'HEA', 'BIZ', 'ANG', 'CYN', 
                              'ASP', 'TPA', 'LSE', 'SOD', 'FAM', 'WRK', 'TRT']
        
        # Extract scores in correct order
        scores = []
        for scale in content_scale_names:
            if scale in content_scales:
                scores.append(content_scales[scale])
            else:
                scores.append(50)  # Default value if missing
        
        # Create x-axis positions
        x_pos = np.arange(len(content_scale_names))
        
        # Plot scores
        ax.plot(x_pos, scores, 'b-o', linewidth=1.5, markersize=6)
        
        # Set axis limits
        ax.set_ylim(30, 120)
        ax.set_xlim(-0.5, len(content_scale_names) - 0.5)
        
        # Add clinical significance lines
        ax.axhline(y=65, color='r', linestyle='-', linewidth=2)
        ax.axhline(y=50, color='r', linestyle='-', linewidth=2)
        
        # Set grid
        ax.grid(True, linestyle='-', alpha=0.7)
        ax.set_axisbelow(True)
        
        # Set ticks and labels
        ax.set_xticks(x_pos)
        ax.set_xticklabels(content_scale_names, rotation=45, ha='right')
        
        # Y-axis ticks every 10 units
        ax.yaxis.set_major_locator(MultipleLocator(10))
        
        # Add title
        name = client_info.get('name', 'Client')
        sex = client_info.get('sex', 'female')
        sex_label = 'Female' if sex == 'female' else 'Male'
        title = f"MMPI-2 Content Scales: {name} ({sex_label})"
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        # Add labels
        ax.set_ylabel('T-Score', fontsize=12)
        
        # Add raw scores above graph
        for i, score in enumerate(scores):
            ax.text(i, 122, str(score), ha='center', va='bottom', fontsize=10)
        
        # Add "Raw Score:" label
        ax.text(-0.5, 122, "T-Score:", ha='right', va='bottom', fontsize=10)
        
        # Adjust layout
        plt.tight_layout()
        
        # Save figure
        output_path = os.path.join(self.output_dir, 'content_scales_graph.png')
        plt.savefig(output_path, bbox_inches='tight')
        plt.close(fig)
        
        return output_path
    
    def generate_psy5_scales_graph(self, psy5_scales, client_info):
        """
        Generate PSY-5 scales graph.
        
        Args:
            psy5_scales (dict): Dictionary of PSY-5 scale scores
            client_info (dict): Dictionary containing client information
            
        Returns:
            str: Path to generated graph file
        """
        # Create figure and axis
        fig, ax = plt.subplots(figsize=self.fig_size, dpi=self.dpi)
        
        # Define PSY-5 scales
        psy5_scale_names = ['AGGR', 'PSYC', 'DISC', 'NEGE', 'INTR']
        psy5_scale_full_names = {
            'AGGR': 'Aggressiveness',
            'PSYC': 'Psychoticism',
            'DISC': 'Disconstraint',
            'NEGE': 'Negative Emotionality/Neuroticism',
            'INTR': 'Introversion/Low Positive Emotionality'
        }
        
        # Extract scores in correct order
        scores = []
        for scale in psy5_scale_names:
            if scale in psy5_scales:
                scores.append(psy5_scales[scale])
            else:
                scores.append(50)  # Default value if missing
        
        # Create x-axis positions
        x_pos = np.arange(len(psy5_scale_names))
        
        # Plot scores
        ax.plot(x_pos, scores, 'b-o', linewidth=1.5, markersize=6)
        
        # Set axis limits
        ax.set_ylim(30, 120)
        ax.set_xlim(-0.5, len(psy5_scale_names) - 0.5)
        
        # Add clinical significance lines
        ax.axhline(y=65, color='r', linestyle='-', linewidth=2)
        ax.axhline(y=50, color='r', linestyle='-', linewidth=2)
        
        # Set grid
        ax.grid(True, linestyle='-', alpha=0.7)
        ax.set_axisbelow(True)
        
        # Set ticks and labels
        ax.set_xticks(x_pos)
        ax.set_xticklabels(psy5_scale_names)
        
        # Y-axis ticks every 10 units
        ax.yaxis.set_major_locator(MultipleLocator(10))
        
        # Add title
        name = client_info.get('name', 'Client')
        sex = client_info.get('sex', 'female')
        sex_label = 'Female' if sex == 'female' else 'Male'
        title = f"MMPI-2 PSY-5 Scales: {name} ({sex_label})"
        ax.set_title(title, fontsize=14, fontweight='bold')
        
        # Add labels
        ax.set_ylabel('T-Score', fontsize=12)
        
        # Add raw scores above graph
        for i, score in enumerate(scores):
            ax.text(i, 122, str(score), ha='center', va='bottom', fontsize=10)
        
        # Add "Raw Score:" label
        ax.text(-0.5, 122, "T-Score:", ha='right', va='bottom', fontsize=10)
        
        # Add PSY-5 scale full names as a table below the graph
        table_data = []
        for scale in psy5_scale_names:
            table_data.append([scale, psy5_scale_full_names.get(scale, '')])
        
        table = ax.table(cellText=table_data, 
                         colLabels=['Scale', 'Full Name'],
                         loc='bottom', 
                         cellLoc='center',
                         bbox=[0, -0.4, 1, 0.2])
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 1.5)
        
        # Adjust layout
        plt.subplots_adjust(bottom=0.25)
        
        # Save figure
        output_path = os.path.join(self.output_dir, 'psy5_scales_graph.png')
        plt.savefig(output_path, bbox_inches='tight')
        plt.close(fig)
        
        return output_path
    
    def generate_supplementary_scales_graph(self, supplementary_scales, client_info):
        """
        Generate supplementary scales graph.
        
        Args:
            supplementary_scales (dict): Dictionary of supplementary scale scores
            client_info (dict): Dictionary containing client information
            
        Returns:
            str: Path to generated graph file
        """
        # Create figure and axis
        fig, ax = plt.subplots(figsize=self.fig_size, dpi=self.dpi)
        
        # Define supplementary scales
        supp_scale_names = ['A', 'R', 'Es', 'Do', 'Re', 'Mt', 'PK', 'MDS', 'Ho', 'O-H', 'MAC-R', 'APS', 'GM', 'GF']
        
        # Extract scores in correct order
        scores = []
        for scale in supp_scale_names:
            if
(Content truncated due to size limit. Use line ranges to read in chunks)
