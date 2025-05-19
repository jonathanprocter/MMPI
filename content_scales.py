"""
Content Scales Interpretations for MMPI-2.

This module provides detailed interpretations for MMPI-2 Content Scales
based on T-score ranges and gender.
"""

# Content Scale Interpretations Dictionary
CONTENT_SCALE_INTERPRETATIONS = {
    "Female": {
        # Add female interpretations here
    },
    "Male": {
        # Add male interpretations here
    }
}

def get_content_scale_interpretation(scale, t_score, gender):
    """
    Get the interpretation for a content scale based on T-score and gender.
    
    Args:
        scale (str): The content scale code (e.g., "ANX", "DEP", "HEA")
        t_score (int): The T-score value
        gender (str): "Male" or "Female"
        
    Returns:
        str: The appropriate interpretation text based on T-score range
    """
    if gender not in CONTENT_SCALE_INTERPRETATIONS:
        return f"Interpretation not available for gender: {gender}"
        
    gender_dict = CONTENT_SCALE_INTERPRETATIONS[gender]
    
    if scale not in gender_dict:
        return f"Interpretation not available for scale: {scale} in {gender}"
        
    scale_dict = gender_dict[scale]
    
    # Determine which interpretation to use based on T-score
    if t_score < 65:
        if "low" in scale_dict:
            return scale_dict["low"]
    elif t_score == 65:
        if "moderate" in scale_dict:
            return scale_dict["moderate"]
    else:  # t_score > 65
        if "high" in scale_dict:
            return scale_dict["high"]
            
    return f"No interpretation available for {scale} with T-score {t_score} in {gender}"
