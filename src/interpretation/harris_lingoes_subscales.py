"""
Harris-Lingoes Subscales Interpretations for MMPI-2.

This module provides detailed interpretations for MMPI-2 Harris-Lingoes Subscales
based on T-score ranges and gender.
"""

# Harris-Lingoes Subscale Interpretations Dictionary
HARRIS_LINGOES_SUBSCALE_INTERPRETATIONS = {
    "Female": {
        # Add female interpretations here
    },
    "Male": {
        # Add male interpretations here
    }
}

def get_harris_lingoes_subscale_interpretation(scale, t_score, gender):
    """
    Get the interpretation for a Harris-Lingoes subscale based on T-score and gender.
    
    Args:
        scale (str): The Harris-Lingoes subscale code (e.g., "D1", "D2", "Hy1")
        t_score (int): The T-score value
        gender (str): "Male" or "Female"
        
    Returns:
        str: The appropriate interpretation text based on T-score range
    """
    if gender not in HARRIS_LINGOES_SUBSCALE_INTERPRETATIONS:
        return f"Interpretation not available for gender: {gender}"
        
    gender_dict = HARRIS_LINGOES_SUBSCALE_INTERPRETATIONS[gender]
    
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
