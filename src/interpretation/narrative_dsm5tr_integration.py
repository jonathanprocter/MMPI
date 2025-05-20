"""
Harmonized DSM-5-TR narrative integration module for MMPI-2 reports.

This module ensures seamless integration between detailed scale interpretations
and DSM-5-TR diagnostic impressions in MMPI-2 reports.
"""

def harmonize_narrative_with_dsm5tr(scale_scores, dsm5tr_impressions):
    """
    Harmonize detailed scale interpretations with DSM-5-TR diagnostic impressions.
    
    Args:
        scale_scores: Dictionary of scale scores
        dsm5tr_impressions: Dictionary of DSM-5-TR diagnostic impressions
        
    Returns:
        Dictionary with harmonized narrative content
    """
    # Create harmonized narrative structure
    harmonized_narrative = {
        "clinical_synthesis": "",
        "diagnostic_considerations": "",
        "treatment_implications": ""
    }
    
    # Extract key clinical patterns from scale scores
    clinical_patterns = extract_clinical_patterns(scale_scores)
    
    # Generate clinical synthesis that integrates scale interpretations with diagnostic impressions
    harmonized_narrative["clinical_synthesis"] = generate_clinical_synthesis(
        clinical_patterns, 
        dsm5tr_impressions["primary_diagnosis"]
    )
    
    # Generate diagnostic considerations that integrate scale patterns with differential diagnoses
    harmonized_narrative["diagnostic_considerations"] = generate_diagnostic_considerations(
        clinical_patterns,
        dsm5tr_impressions["differential_diagnosis"]
    )
    
    # Generate treatment implications based on scale patterns and diagnostic impressions
    harmonized_narrative["treatment_implications"] = generate_treatment_implications(
        clinical_patterns,
        dsm5tr_impressions["additional_considerations"]
    )
    
    return harmonized_narrative

def extract_clinical_patterns(scale_scores):
    """
    Extract key clinical patterns from scale scores.
    
    Args:
        scale_scores: Dictionary of scale scores
        
    Returns:
        Dictionary of key clinical patterns
    """
    patterns = {
        "anxiety": False,
        "depression": False,
        "somatic_concerns": False,
        "thought_disturbance": False,
        "interpersonal_difficulties": False,
        "externalizing_behaviors": False,
        "trauma_indicators": False
    }
    
    # Check for anxiety indicators
    if "7" in scale_scores and isinstance(scale_scores["7"], int) and scale_scores["7"] >= 65:
        patterns["anxiety"] = True
    if "ANX" in scale_scores and isinstance(scale_scores["ANX"], int) and scale_scores["ANX"] >= 65:
        patterns["anxiety"] = True
    if "RC7" in scale_scores and isinstance(scale_scores["RC7"], int) and scale_scores["RC7"] >= 65:
        patterns["anxiety"] = True
        
    # Check for depression indicators
    if "2" in scale_scores and isinstance(scale_scores["2"], int) and scale_scores["2"] >= 65:
        patterns["depression"] = True
    if "DEP" in scale_scores and isinstance(scale_scores["DEP"], int) and scale_scores["DEP"] >= 65:
        patterns["depression"] = True
    if "RC2" in scale_scores and isinstance(scale_scores["RC2"], int) and scale_scores["RC2"] >= 65:
        patterns["depression"] = True
        
    # Check for somatic concern indicators
    if ("1" in scale_scores and isinstance(scale_scores["1"], int) and scale_scores["1"] >= 65) or \
       ("3" in scale_scores and isinstance(scale_scores["3"], int) and scale_scores["3"] >= 65):
        patterns["somatic_concerns"] = True
    if "HEA" in scale_scores and isinstance(scale_scores["HEA"], int) and scale_scores["HEA"] >= 65:
        patterns["somatic_concerns"] = True
    if "RC1" in scale_scores and isinstance(scale_scores["RC1"], int) and scale_scores["RC1"] >= 65:
        patterns["somatic_concerns"] = True
        
    # Check for thought disturbance indicators
    if ("6" in scale_scores and isinstance(scale_scores["6"], int) and scale_scores["6"] >= 65) or \
       ("8" in scale_scores and isinstance(scale_scores["8"], int) and scale_scores["8"] >= 65):
        patterns["thought_disturbance"] = True
    if "BIZ" in scale_scores and isinstance(scale_scores["BIZ"], int) and scale_scores["BIZ"] >= 65:
        patterns["thought_disturbance"] = True
    if ("RC6" in scale_scores and isinstance(scale_scores["RC6"], int) and scale_scores["RC6"] >= 65) or \
       ("RC8" in scale_scores and isinstance(scale_scores["RC8"], int) and scale_scores["RC8"] >= 65):
        patterns["thought_disturbance"] = True
        
    # Check for interpersonal difficulty indicators
    if "0" in scale_scores and isinstance(scale_scores["0"], int) and scale_scores["0"] >= 65:
        patterns["interpersonal_difficulties"] = True
    if "SOD" in scale_scores and isinstance(scale_scores["SOD"], int) and scale_scores["SOD"] >= 65:
        patterns["interpersonal_difficulties"] = True
        
    # Check for externalizing behavior indicators
    if ("4" in scale_scores and isinstance(scale_scores["4"], int) and scale_scores["4"] >= 65) or \
       ("9" in scale_scores and isinstance(scale_scores["9"], int) and scale_scores["9"] >= 65):
        patterns["externalizing_behaviors"] = True
    if ("ANG" in scale_scores and isinstance(scale_scores["ANG"], int) and scale_scores["ANG"] >= 65) or \
       ("ASP" in scale_scores and isinstance(scale_scores["ASP"], int) and scale_scores["ASP"] >= 65):
        patterns["externalizing_behaviors"] = True
    if ("RC4" in scale_scores and isinstance(scale_scores["RC4"], int) and scale_scores["RC4"] >= 65) or \
       ("RC9" in scale_scores and isinstance(scale_scores["RC9"], int) and scale_scores["RC9"] >= 65):
        patterns["externalizing_behaviors"] = True
        
    # Check for trauma indicators
    if ("PK" in scale_scores and isinstance(scale_scores["PK"], int) and scale_scores["PK"] >= 65) or \
       ("PS" in scale_scores and isinstance(scale_scores["PS"], int) and scale_scores["PS"] >= 65):
        patterns["trauma_indicators"] = True
    
    return patterns

def generate_clinical_synthesis(clinical_patterns, primary_diagnosis):
    """
    Generate clinical synthesis that integrates scale patterns with primary diagnosis.
    
    Args:
        clinical_patterns: Dictionary of key clinical patterns
        primary_diagnosis: Primary diagnosis from DSM-5-TR impressions
        
    Returns:
        String with harmonized clinical synthesis
    """
    synthesis = "<p>The MMPI-2 profile reveals a clinical picture characterized by "
    
    # Add pattern-specific content
    pattern_descriptions = []
    
    if clinical_patterns["anxiety"]:
        pattern_descriptions.append("significant anxiety and worry")
    
    if clinical_patterns["depression"]:
        pattern_descriptions.append("depressive symptoms including dysphoria and anhedonia")
    
    if clinical_patterns["somatic_concerns"]:
        pattern_descriptions.append("somatic concerns and preoccupation with physical health")
    
    if clinical_patterns["thought_disturbance"]:
        pattern_descriptions.append("unusual thought processes and possible perceptual abnormalities")
    
    if clinical_patterns["interpersonal_difficulties"]:
        pattern_descriptions.append("social discomfort and interpersonal difficulties")
    
    if clinical_patterns["externalizing_behaviors"]:
        pattern_descriptions.append("impulsivity and possible rule-breaking behaviors")
    
    if clinical_patterns["trauma_indicators"]:
        pattern_descriptions.append("possible trauma-related symptoms")
    
    # Combine pattern descriptions
    if pattern_descriptions:
        synthesis += ", ".join(pattern_descriptions[:-1])
        if len(pattern_descriptions) > 1:
            synthesis += ", and " + pattern_descriptions[-1]
        else:
            synthesis += pattern_descriptions[-1]
    else:
        synthesis += "a complex presentation with multiple psychological concerns"
    
    synthesis += ".</p>"
    
    # Add integration with primary diagnosis
    synthesis += "<p>These findings are consistent with the diagnostic impression of "
    synthesis += primary_diagnosis.strip().replace("<p>", "").replace("</p>", "")
    
    return synthesis

def generate_diagnostic_considerations(clinical_patterns, differential_diagnosis):
    """
    Generate diagnostic considerations that integrate scale patterns with differential diagnoses.
    
    Args:
        clinical_patterns: Dictionary of key clinical patterns
        differential_diagnosis: Differential diagnoses from DSM-5-TR impressions
        
    Returns:
        String with harmonized diagnostic considerations
    """
    considerations = "<p>Based on the MMPI-2 profile pattern, the following diagnostic considerations are warranted:</p>"
    
    # Add differential diagnosis content
    considerations += differential_diagnosis.strip()
    
    # Add pattern-specific diagnostic considerations
    additional_considerations = []
    
    if clinical_patterns["trauma_indicators"] and "trauma" not in differential_diagnosis.lower():
        additional_considerations.append("<li><strong>Posttraumatic Stress Disorder</strong> - Given elevations on trauma-related scales</li>")
    
    if clinical_patterns["somatic_concerns"] and "somatic" not in differential_diagnosis.lower():
        additional_considerations.append("<li><strong>Somatic Symptom Disorder</strong> - Given the significant somatic concerns</li>")
    
    if clinical_patterns["interpersonal_difficulties"] and "personality" not in differential_diagnosis.lower():
        additional_considerations.append("<li><strong>Personality Factors</strong> - Consider how personality traits may influence presentation and treatment response</li>")
    
    # Add additional considerations if any
    if additional_considerations:
        considerations += "<p>Additional considerations based on scale elevations:</p><ul>"
        considerations += "".join(additional_considerations)
        considerations += "</ul>"
    
    return considerations

def generate_treatment_implications(clinical_patterns, additional_considerations):
    """
    Generate treatment implications based on scale patterns and additional considerations.
    
    Args:
        clinical_patterns: Dictionary of key clinical patterns
        additional_considerations: Additional considerations from DSM-5-TR impressions
        
    Returns:
        String with harmonized treatment implications
    """
    implications = "<p>The MMPI-2 profile suggests the following treatment implications:</p><ul>"
    
    # Add pattern-specific treatment implications
    if clinical_patterns["anxiety"]:
        implications += "<li>Anxiety management strategies including relaxation training, cognitive restructuring, and possibly medication</li>"
    
    if clinical_patterns["depression"]:
        implications += "<li>Depression-focused interventions including behavioral activation, cognitive therapy, and consideration of antidepressant medication</li>"
    
    if clinical_patterns["somatic_concerns"]:
        implications += "<li>Collaborative approach with medical providers to address somatic concerns while introducing psychological perspectives</li>"
    
    if clinical_patterns["thought_disturbance"]:
        implications += "<li>Reality testing interventions and possible referral for medication evaluation if thought disturbance is significant</li>"
    
    if clinical_patterns["interpersonal_difficulties"]:
        implications += "<li>Social skills training and interpersonal therapy to address social discomfort and isolation</li>"
    
    if clinical_patterns["externalizing_behaviors"]:
        implications += "<li>Impulse control strategies and structured behavioral interventions</li>"
    
    if clinical_patterns["trauma_indicators"]:
        implications += "<li>Trauma-focused therapy approaches if further assessment confirms trauma history</li>"
    
    implications += "</ul>"
    
    # Add integration with additional considerations
    implications += additional_considerations.strip()
    
    return implications
