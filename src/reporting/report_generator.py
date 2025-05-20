#!/usr/bin/env python3
"""
Report Generator for MMPI-2 test results.

This module provides functionality to generate comprehensive MMPI-2 reports
in various formats (TEXT, HTML, PDF, JSON) with detailed scale interpretations,
summaries, and diagnostic impressions.
"""

import os
import json
from datetime import datetime
from jinja2 import Template
from weasyprint import HTML

from src.interpretation.scale_interpretations import get_scale_interpretation
from src.constants.scale_constants import (
    VALIDITY_SCALES_ORDER, CLINICAL_SCALES_ORDER, CLINICAL_SCALES_DB_KEYS,
    RESTRUCTURED_CLINICAL_SCALES_ORDER, CONTENT_SCALES_ORDER,
    SUPPLEMENTARY_SCALES_ORDER, PSY5_SCALES_ORDER,
    CLINICAL_SCALES_MAP, HARRIS_LINGOES_SUBSCALES_MAP
)
from src.models.models import db, Respondent, Scale, TScore as Score

class ReportGenerator:
    """
    Generates comprehensive MMPI-2 reports in various formats.
    """
    
    def __init__(self, respondent_id):
        """
        Initialize the report generator with a respondent ID.
        
        Args:
            respondent_id: The ID of the respondent to generate a report for.
        """
        self.respondent_id = respondent_id
        self.respondent = self._get_respondent_data()
        self.scores = self._get_scores_data()
        self.graph_paths = {}  # Placeholder for graph file paths
        self.profile_summary_for_dsm = ""  # Placeholder for DSM profile summary
    
    def _get_respondent_data(self):
        """
        Retrieve respondent data from the database.
        
        Returns:
            dict: Respondent data.
        """
        respondent = Respondent.query.filter_by(id=self.respondent_id).first()
        if not respondent:
            raise ValueError(f"Respondent with ID {self.respondent_id} not found")
        
        return {
            "id": respondent.id,
            "age": respondent.age,
            "sex": respondent.sex,
            "education": respondent.education,
            "occupation": respondent.occupation,
            "marital_status": respondent.marital_status,
            "referral_source": respondent.referral_source,
            "notes": respondent.notes,
            "test_started_at": respondent.test_started_at,
            "test_completed_at": respondent.test_completed_at
        }
    
    def _get_scores_data(self):
        """
        Retrieve all scale scores for the respondent.
        
        Returns:
            dict: Scale scores indexed by scale database key.
        """
        scores_data = {}
        
        # Get all scales
        scales = Scale.query.all()
        scale_dict = {scale.id: scale.name for scale in scales}
        
        # Get all scores for the respondent
        scores = Score.query.filter_by(respondent_id=self.respondent_id).all()
        
        for score in scores:
            scale_name = scale_dict.get(score.scale_id)
            if scale_name:
                scores_data[scale_name] = {
                    "raw": score.raw_score,
                    "t_score": score.t_score
                }
        
        return scores_data
    
    def _populate_scales_list(self, scale_order, is_clinical_scales=False):
        """
        Populate a list of scales with their scores and interpretations.
        
        Args:
            scale_order: List of scale database keys in the desired order.
            is_clinical_scales: Whether these are clinical scales (for mapping).
            
        Returns:
            list: List of scale dictionaries with scores and interpretations.
        """
        scales_list = []
        
        for scale_db_key in scale_order:
            info = self.scores.get(scale_db_key)
            if info:
                # For clinical scales, use the mapping to get standard abbreviation
                if is_clinical_scales:
                    scale_code = CLINICAL_SCALES_MAP.get(scale_db_key, scale_db_key)
                else:
                    scale_code = scale_db_key
                
                # Get scale name
                scale = Scale.query.filter_by(name=scale_db_key).first()
                scale_name = scale.description if scale else scale_db_key
                
                # Get interpretation
                t_score = info.get("t_score")
                raw_score = info.get("raw")
                interpretation = get_scale_interpretation(scale_db_key, t_score, raw_score)
                
                scales_list.append({
                    "code": scale_code,
                    "name": scale_name,
                    "t_score": t_score,
                    "raw": raw_score,
                    "interpretation": interpretation
                })
        
        return scales_list
    
    def _get_harris_lingoes_subscales_data(self):
        """
        Get Harris-Lingoes subscales data for the respondent.
        
        Returns:
            list: List of Harris-Lingoes subscale dictionaries.
        """
        subscales_list = []
        
        for subscale_db_key, parent_scale in HARRIS_LINGOES_SUBSCALES_MAP.items():
            info = self.scores.get(subscale_db_key)
            if info:
                # Get scale name
                scale = Scale.query.filter_by(name=subscale_db_key).first()
                scale_name = scale.description if scale else subscale_db_key
                
                # Get interpretation
                t_score = info.get("t_score")
                raw_score = info.get("raw")
                interpretation = get_scale_interpretation(subscale_db_key, t_score, raw_score)
                
                subscales_list.append({
                    "code": subscale_db_key,
                    "name": scale_name,
                    "t_score": t_score,
                    "raw": raw_score,
                    "interpretation": interpretation,
                    "parent_scale": parent_scale
                })
        
        return subscales_list
    
    def _generate_family_summary(self, family_type, scales_list):
        """
        Generate a summary for a family of scales.
        
        Args:
            family_type: The type of scale family (e.g., "VALIDITY", "CLINICAL").
            scales_list: List of scale dictionaries.
            
        Returns:
            str: Summary text for the scale family.
        """
        elevated_scales = []
        for scale in scales_list:
            if scale.get("t_score") and float(scale.get("t_score")) >= 65:
                elevated_scales.append((scale["code"], float(scale.get("t_score"))))
        
        # Sort by T-score (highest first)
        elevated_scales.sort(key=lambda x: x[1], reverse=True)
        
        if not elevated_scales:
            return f"No clinically significant elevations were found on the {family_type} scales. All scales in this family are within normal limits, suggesting absence of significant concerns in this domain."
        
        # Generate summary based on family type
        if family_type == "VALIDITY":
            return self._generate_validity_summary(elevated_scales)
        elif family_type == "CLINICAL":
            return self._generate_clinical_summary(elevated_scales)
        elif family_type == "RC":
            return self._generate_rc_summary(elevated_scales)
        elif family_type == "CONTENT":
            return self._generate_content_summary(elevated_scales)
        elif family_type == "SUPPLEMENTARY":
            return self._generate_supplementary_summary(elevated_scales)
        elif family_type == "PSY5":
            return self._generate_psy5_summary(elevated_scales)
        else:
            return f"The following {family_type} scales show significant elevations: " + ", ".join([f"{code} (T={score})" for code, score in elevated_scales])
    
    def _generate_validity_summary(self, elevated_scales):
        """
        Generate a summary for validity scales.
        
        Args:
            elevated_scales: List of (scale_code, t_score) tuples.
            
        Returns:
            str: Summary text for validity scales.
        """
        if not elevated_scales:
            return "The validity scales indicate that the respondent approached the test in a forthright and cooperative manner. The profile appears to be a valid representation of the respondent's current psychological functioning."
        
        # Check for specific validity concerns
        f_scales = [s for s in elevated_scales if s[0] in ["F", "Fb", "Fp"]]
        vrin_trin = [s for s in elevated_scales if s[0] in ["VRIN", "TRIN"]]
        lks_scales = [s for s in elevated_scales if s[0] in ["L", "K", "S"]]
        
        concerns = []
        
        if f_scales:
            if any(score >= 80 for _, score in f_scales):
                concerns.append("significant overreporting of psychological symptoms")
            elif any(score >= 65 for _, score in f_scales):
                concerns.append("some tendency to overreport psychological symptoms")
        
        if vrin_trin:
            if any(score >= 80 for _, score in vrin_trin):
                concerns.append("inconsistent or random responding")
            elif any(score >= 65 for _, score in vrin_trin):
                concerns.append("some inconsistency in responding")
        
        if lks_scales:
            if any(score >= 80 for _, score in lks_scales):
                concerns.append("significant defensiveness or underreporting of psychological symptoms")
            elif any(score >= 65 for _, score in lks_scales):
                concerns.append("some defensiveness or reluctance to acknowledge psychological symptoms")
        
        if concerns:
            summary = "The validity scales indicate " + ", ".join(concerns) + ". "
            
            if any(score >= 80 for _, score in elevated_scales):
                summary += "Caution is warranted in interpreting this profile due to these significant validity concerns. The clinical scale elevations may not accurately reflect the respondent's true psychological functioning."
            else:
                summary += "These validity concerns should be considered when interpreting the clinical scales, although they do not necessarily invalidate the profile."
        else:
            summary = "Despite some elevated validity indicators, the profile appears to be a generally valid representation of the respondent's current psychological functioning."
        
        return summary
    
    def _generate_clinical_summary(self, elevated_scales):
        """
        Generate a summary for clinical scales.
        
        Args:
            elevated_scales: List of (scale_code, t_score) tuples.
            
        Returns:
            str: Summary text for clinical scales.
        """
        if not elevated_scales:
            return "No clinically significant elevations were found on the Clinical scales. All scales are within normal limits, suggesting absence of significant psychopathology."
        
        # Get the two highest scales for code type
        if len(elevated_scales) >= 2:
            scale1, score1 = elevated_scales[0]
            scale2, score2 = elevated_scales[1]
            code_type = "-".join(sorted([scale1, scale2]))
        else:
            scale1, score1 = elevated_scales[0]
            code_type = f"Spike {scale1}"
        
        # Generate summary based on number of elevations
        if len(elevated_scales) > 3:
            summary = f"The Clinical scales show a complex profile with multiple elevations, indicating significant psychological distress across several domains. The most prominent elevations are on scales {scale1} (T={score1}) and {scale2} (T={score2}), forming a {code_type} code type. This pattern suggests "
        elif len(elevated_scales) > 1:
            summary = f"The Clinical scales show significant elevations on scales {scale1} (T={score1}) and {scale2} (T={score2}), forming a {code_type} code type. This pattern suggests "
        else:
            summary = f"The Clinical scales show a single significant elevation on scale {scale1} (T={score1}). This spike profile suggests "
        
        # Add interpretation based on highest scales
        if "1" in [scale1, scale2] and "2" in [scale1, scale2]:
            summary += "somatic preoccupation in the context of depression, with physical symptoms likely serving as an expression of psychological distress."
        elif "1" in [scale1, scale2] and "3" in [scale1, scale2]:
            summary += "significant somatic concerns with denial of psychological problems, characteristic of a conversion V pattern."
        elif "2" in [scale1, scale2] and "7" in [scale1, scale2]:
            summary += "significant anxiety and depression, with rumination, worry, and self-criticism."
        elif "2" in [scale1, scale2] and "4" in [scale1, scale2]:
            summary += "depression complicated by characterological issues, with possible acting-out behaviors."
        elif "2" in [scale1, scale2] and "8" in [scale1, scale2]:
            summary += "severe psychological distress with features of both depression and thought disturbance."
        elif "4" in [scale1, scale2] and "9" in [scale1, scale2]:
            summary += "significant impulsivity, poor judgment, and acting-out behavior."
        elif "6" in [scale1, scale2] and "8" in [scale1, scale2]:
            summary += "significant thought disturbance with paranoid features."
        elif "7" in [scale1, scale2] and "8" in [scale1, scale2]:
            summary += "severe anxiety with possible thought disturbance and reality testing issues."
        elif "1" in [scale1]:
            summary += "preoccupation with physical health and bodily functions."
        elif "2" in [scale1]:
            summary += "significant depressive symptoms, including sadness, pessimism, and low energy."
        elif "3" in [scale1]:
            summary += "use of denial and repression to manage anxiety, with possible conversion symptoms."
        elif "4" in [scale1]:
            summary += "difficulty with authority, poor impulse control, and possible antisocial tendencies."
        elif "6" in [scale1]:
            summary += "interpersonal sensitivity, suspiciousness, and possible paranoid ideation."
        elif "7" in [scale1]:
            summary += "significant anxiety, tension, and obsessive-compulsive features."
        elif "8" in [scale1]:
            summary += "unusual thought processes, possible social alienation, and difficulty with reality testing."
        elif "9" in [scale1]:
            summary += "elevated mood, increased energy, and possible impulsivity or grandiosity."
        elif "0" in [scale1]:
            summary += "social discomfort, introversion, and possible social withdrawal."
        else:
            summary += "significant psychological distress requiring further clinical evaluation."
        
        return summary
    
    def _generate_rc_summary(self, elevated_scales):
        """
        Generate a summary for RC scales.
        
        Args:
            elevated_scales: List of (scale_code, t_score) tuples.
            
        Returns:
            str: Summary text for RC scales.
        """
        if not elevated_scales:
            return "No clinically significant elevations were found on the Restructured Clinical scales. All scales are within normal limits, suggesting absence of significant core psychopathology in these domains."
        
        # Categorize elevations
        demoralization = any(code == "RCd" for code, _ in elevated_scales)
        somatic = any(code == "RC1" for code, _ in elevated_scales)
        low_positive_emotions = any(code == "RC2" for code, _ in elevated_scales)
        cynicism = any(code == "RC3" for code, _ in elevated_scales)
        antisocial = any(code == "RC4" for code, _ in elevated_scales)
        persecution = any(code == "RC6" for code, _ in e
(Content truncated due to size limit. Use line ranges to read in chunks)
