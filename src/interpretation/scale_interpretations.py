# This file will contain the detailed interpretation logic for MMPI-2 scales.
# Interpretations are based on common clinical understanding, MMPI-2 literature,
# and requirements from the "MMPI-2 Reverse Engineer Prompt" document.
# Import all scale interpretation dictionaries
from src.interpretation.clinical_scales import CLINICAL_SCALES_INTERPRETATIONS
from src.interpretation.rc_scales import RC_SCALES_INTERPRETATIONS
from src.interpretation.content_scales import CONTENT_SCALES_INTERPRETATIONS
from src.interpretation.content_component_scales import CONTENT_COMPONENT_SCALES_INTERPRETATIONS
from src.interpretation.psy5_scales import PSY5_SCALES_INTERPRETATIONS
from src.interpretation.harris_lingoes_subscales import HARRIS_LINGOES_SUBSCALES_INTERPRETATIONS
from src.interpretation.supplementary_scales import SUPPLEMENTARY_SCALES_INTERPRETATIONS
from src.interpretation.validity_scales import VALIDITY_SCALES_INTERPRETATIONS

# Function to get the appropriate interpretation for a scale based on its T-score
def get_scale_interpretation(scale_name, t_score, scale_type=None, raw_score=None, gender=None):
    """
    Get the interpretation for a scale based on its T-score.
    
    Args:
        scale_name (str): The name of the scale (e.g., "Hs", "D", "Hy")
        t_score (float or str): The T-score for the scale
        scale_type (str, optional): The type of scale (e.g., "VALIDITY", "CLINICAL"). 
                                   If not provided, will attempt to determine from scale_name.
        raw_score (float or str, optional): The raw score for the scale, used for additional context in some interpretations.
        gender (str, optional): The gender of the respondent, used for gender-specific interpretations.
    
    Returns:
        str: The interpretation for the scale based on its T-score
    """
    # Handle non-numeric t_score
    try:
        t_score = float(t_score) if t_score is not None else 0
    except (ValueError, TypeError):
        # If t_score cannot be converted to float, return a message indicating invalid score
        return f"T-score for {scale_name} is not a numeric value; interpretation cannot be provided."
    
    # Determine which dictionary to use based on scale_name or scale_type
    if scale_type == "VALIDITY" or scale_name in ["?", "L", "F", "K", "Fb", "Fp", "FBS", "VRIN", "TRIN"]:
        interpretation_dict = VALIDITY_SCALES_INTERPRETATIONS
    elif scale_type == "CLINICAL" or scale_name in ["Hs", "D", "Hy", "Pd", "Mf", "Pa", "Pt", "Sc", "Ma", "Si"] or scale_name in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
        interpretation_dict = CLINICAL_SCALES_INTERPRETATIONS
        # Map numeric scale names to text names
        if scale_name == "1": scale_name = "Hs"
        elif scale_name == "2": scale_name = "D"
        elif scale_name == "3": scale_name = "Hy"
        elif scale_name == "4": scale_name = "Pd"
        elif scale_name == "5": scale_name = "Mf"
        elif scale_name == "6": scale_name = "Pa"
        elif scale_name == "7": scale_name = "Pt"
        elif scale_name == "8": scale_name = "Sc"
        elif scale_name == "9": scale_name = "Ma"
        elif scale_name == "0": scale_name = "Si"
        interpretation_dict = CLINICAL_SCALES_INTERPRETATIONS
    elif scale_type == "RC" or scale_name in ["RCd", "RC1", "RC2", "RC3", "RC4", "RC6", "RC7", "RC8", "RC9"]:
        interpretation_dict = RC_SCALES_INTERPRETATIONS
    elif scale_type == "CONTENT" or scale_name in ["ANX", "FRS", "OBS", "DEP", "HEA", "BIZ", "ANG", "CYN", "ASP", "TPA", "LSE", "SOD", "FAM", "WRK", "TRT"]:
        interpretation_dict = CONTENT_SCALES_INTERPRETATIONS
    elif scale_type == "CONTENT_COMPONENT" or scale_name in ["ANX1", "ANX2", "FRS1", "FRS2", "OBS1", "OBS2", "DEP1", "DEP2", "DEP3", "DEP4", "HEA1", "HEA2", "HEA3", "BIZ1", "BIZ2", "ANG1", "ANG2", "CYN1", "CYN2", "ASP1", "ASP2", "TPA1", "TPA2", "LSE1", "LSE2", "SOD1", "SOD2", "FAM1", "FAM2", "WRK1", "WRK2", "TRT1", "TRT2"]:
        interpretation_dict = CONTENT_COMPONENT_SCALES_INTERPRETATIONS
    elif scale_type == "PSY5" or scale_name in ["AGGR", "PSYC", "DISC", "NEGE", "INTR"]:
        interpretation_dict = PSY5_SCALES_INTERPRETATIONS
    elif scale_type == "HARRIS_LINGOES" or scale_name in ["D1", "D2", "D3", "D4", "D5", "Hy1", "Hy2", "Hy3", "Hy4", "Hy5", "Pd1", "Pd2", "Pd3", "Pd4", "Pd5", "Pa1", "Pa2", "Pa3", "Sc1", "Sc2", "Sc3", "Sc4", "Sc5", "Sc6", "Ma1", "Ma2", "Ma3", "Ma4"]:
        interpretation_dict = HARRIS_LINGOES_SUBSCALES_INTERPRETATIONS
    elif scale_type == "SUPPLEMENTARY" or scale_name in ["A", "R", "Es", "Do", "Re", "Mt", "GM", "GF", "PK", "PS", "MDS", "APS", "AAS", "MAC-R", "O-H", "Do"]:
        interpretation_dict = SUPPLEMENTARY_SCALES_INTERPRETATIONS
    else:
        # Default to VALIDITY if we can't determine the scale type
        interpretation_dict = VALIDITY_SCALES_INTERPRETATIONS
    
    # Try to get the scale from the appropriate dictionary
    if scale_name in interpretation_dict:
        scale_dict = interpretation_dict[scale_name]
        
        # Check if the scale has a "ranges" key
        if "ranges" in scale_dict:
            # Find the appropriate range for the T-score
            for range_dict in scale_dict["ranges"]:
                min_val, max_val = range_dict["range"]
                if min_val <= t_score <= max_val:
                    return range_dict["interpretation"]
            
            # If no range is found, return a default message
            return f"No interpretation found for T-score {t_score} in scale {scale_name}"
        elif "not_numeric" in scale_dict and not isinstance(t_score, (int, float)):
            # Return the not_numeric message if t_score is not numeric
            return scale_dict["not_numeric"]
        else:
            # If the scale doesn't have a "ranges" key, return the entire scale dictionary
            return scale_dict
    else:
        # If the scale is not found in the dictionary, return a default message
        return f"Interpretation not found for scale: {scale_name} in type {scale_type if scale_type else 'UNKNOWN'}"
