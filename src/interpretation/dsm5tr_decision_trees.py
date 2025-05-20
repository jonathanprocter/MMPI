"""
DSM-5-TR diagnostic decision trees for MMPI-2 profile interpretation.

This module implements diagnostic decision trees based on MMPI-2 scale patterns
to provide DSM-5-TR aligned diagnostic impressions.
"""

def get_dsm5tr_diagnostic_impressions(profile_data):
    """
    Generate DSM-5-TR aligned diagnostic impressions based on MMPI-2 profile patterns.
    
    Args:
        profile_data: Dictionary containing scale scores and demographic information
        
    Returns:
        Dictionary with diagnostic impressions sections
    """
    # Extract scale scores
    scale_scores = profile_data.get("scale_scores", {})
    
    # Create diagnostic impressions structure
    impressions = {
        "primary_diagnosis": "",
        "differential_diagnosis": "",
        "additional_considerations": ""
    }
    
    # Generate primary diagnosis based on clinical scale pattern
    clinical_scales = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    clinical_scores = {scale: scale_scores.get(scale, 0) for scale in clinical_scales}
    
    # Sort scales by T-score (descending)
    sorted_scales = sorted(clinical_scores.items(), key=lambda x: x[1], reverse=True)
    top_scales = sorted_scales[:3]
    
    # Generate primary diagnosis based on top scales
    if "7" in [s[0] for s in top_scales] and "2" in [s[0] for s in top_scales]:
        impressions["primary_diagnosis"] = """
        <p>The MMPI-2 profile suggests features consistent with <strong>Major Depressive Disorder with Anxious Distress</strong> (F32.1). The significant elevations on Scales 7 (Psychasthenia) and 2 (Depression) indicate a clinical picture dominated by anxiety, worry, and depressive symptoms including dysphoria, anhedonia, and negative self-evaluation.</p>
        
        <p>The individual likely experiences:</p>
        <ul>
            <li>Persistent worry and rumination</li>
            <li>Depressed mood and diminished interest in activities</li>
            <li>Difficulty concentrating and making decisions</li>
            <li>Fatigue and low energy</li>
            <li>Feelings of worthlessness or excessive guilt</li>
        </ul>
        """
        
        impressions["differential_diagnosis"] = """
        <p>Consider the following differential diagnoses:</p>
        <ul>
            <li><strong>Generalized Anxiety Disorder</strong> - If anxiety symptoms predominate and predate depressive symptoms</li>
            <li><strong>Persistent Depressive Disorder</strong> - If symptoms have been present for more than two years with limited symptom-free periods</li>
            <li><strong>Adjustment Disorder with Mixed Anxiety and Depressed Mood</strong> - If symptoms developed in response to an identifiable stressor</li>
        </ul>
        """
        
        impressions["additional_considerations"] = """
        <p>Additional clinical considerations:</p>
        <ul>
            <li>Assess for suicidal ideation given the significant depression</li>
            <li>Evaluate for possible somatic manifestations of anxiety and depression</li>
            <li>Consider possible cognitive distortions contributing to anxiety and depression</li>
            <li>Assess for possible trauma history that may be contributing to current symptoms</li>
        </ul>
        """
    
    elif "8" in [s[0] for s in top_scales] and "6" in [s[0] for s in top_scales]:
        impressions["primary_diagnosis"] = """
        <p>The MMPI-2 profile suggests features consistent with a <strong>Psychotic Spectrum Disorder</strong>, possibly <strong>Schizophrenia</strong> (F20.9) or <strong>Other Specified Schizophrenia Spectrum Disorder</strong> (F28). The significant elevations on Scales 8 (Schizophrenia) and 6 (Paranoia) indicate a clinical picture that may include thought disturbance, unusual perceptual experiences, and paranoid ideation.</p>
        
        <p>The individual likely experiences:</p>
        <ul>
            <li>Unusual thought processes or magical thinking</li>
            <li>Possible delusions or paranoid ideation</li>
            <li>Potential perceptual abnormalities</li>
            <li>Social withdrawal and interpersonal difficulties</li>
            <li>Cognitive disorganization</li>
        </ul>
        """
        
        impressions["differential_diagnosis"] = """
        <p>Consider the following differential diagnoses:</p>
        <ul>
            <li><strong>Schizoaffective Disorder</strong> - If significant mood symptoms are also present</li>
            <li><strong>Delusional Disorder</strong> - If paranoid features predominate without other psychotic symptoms</li>
            <li><strong>Schizotypal Personality Disorder</strong> - If traits have been stable over time without frank psychosis</li>
        </ul>
        """
        
        impressions["additional_considerations"] = """
        <p>Additional clinical considerations:</p>
        <ul>
            <li>Assess for substance use that may contribute to or exacerbate psychotic symptoms</li>
            <li>Evaluate for possible neurological conditions that may present with psychotic features</li>
            <li>Consider medication side effects as potential contributors to symptoms</li>
            <li>Assess for trauma history that may contribute to paranoid ideation</li>
        </ul>
        """
    
    elif "4" in [s[0] for s in top_scales] and "9" in [s[0] for s in top_scales]:
        impressions["primary_diagnosis"] = """
        <p>The MMPI-2 profile suggests features consistent with <strong>Antisocial Personality Disorder</strong> (F60.2) or possibly <strong>Bipolar I Disorder, Current or Recent Episode Hypomanic</strong> (F31.81). The significant elevations on Scales 4 (Psychopathic Deviate) and 9 (Hypomania) indicate a clinical picture that includes impulsivity, rule-breaking behavior, and heightened energy or irritability.</p>
        
        <p>The individual likely experiences:</p>
        <ul>
            <li>Disregard for social norms and rules</li>
            <li>Impulsivity and stimulation-seeking behavior</li>
            <li>Irritability or aggressiveness</li>
            <li>Heightened energy and decreased need for sleep</li>
            <li>Interpersonal manipulation and deceitfulness</li>
        </ul>
        """
        
        impressions["differential_diagnosis"] = """
        <p>Consider the following differential diagnoses:</p>
        <ul>
            <li><strong>Substance Use Disorder</strong> - If symptoms occur primarily in the context of substance use</li>
            <li><strong>Narcissistic Personality Disorder</strong> - If grandiosity and need for admiration are prominent</li>
            <li><strong>Attention-Deficit/Hyperactivity Disorder</strong> - If impulsivity and hyperactivity have been present since childhood</li>
        </ul>
        """
        
        impressions["additional_considerations"] = """
        <p>Additional clinical considerations:</p>
        <ul>
            <li>Assess for substance use that may contribute to or exacerbate symptoms</li>
            <li>Evaluate for history of trauma that may contribute to antisocial behavior</li>
            <li>Consider possible legal issues related to impulsive or rule-breaking behavior</li>
            <li>Assess for risk of harm to self or others given impulsivity and possible aggression</li>
        </ul>
        """
    
    elif "1" in [s[0] for s in top_scales] and "3" in [s[0] for s in top_scales]:
        impressions["primary_diagnosis"] = """
        <p>The MMPI-2 profile suggests features consistent with <strong>Somatic Symptom Disorder</strong> (F45.1). The significant elevations on Scales 1 (Hypochondriasis) and 3 (Hysteria) indicate a clinical picture dominated by somatic complaints and concerns about physical health that exceed what would be expected from any actual medical condition.</p>
        
        <p>The individual likely experiences:</p>
        <ul>
            <li>Preoccupation with physical symptoms and health concerns</li>
            <li>Excessive time and energy devoted to health concerns</li>
            <li>Resistance to psychological explanations for physical symptoms</li>
            <li>Use of physical symptoms to manage stress or interpersonal situations</li>
            <li>Tendency to present as socially conforming while experiencing significant distress</li>
        </ul>
        """
        
        impressions["differential_diagnosis"] = """
        <p>Consider the following differential diagnoses:</p>
        <ul>
            <li><strong>Illness Anxiety Disorder</strong> - If preoccupation with having a serious illness predominates with minimal somatic symptoms</li>
            <li><strong>Conversion Disorder</strong> - If symptoms include unexplained neurological symptoms</li>
            <li><strong>Major Depressive Disorder</strong> - If somatic complaints occur primarily in the context of a depressive episode</li>
        </ul>
        """
        
        impressions["additional_considerations"] = """
        <p>Additional clinical considerations:</p>
        <ul>
            <li>Ensure appropriate medical evaluation has been conducted to rule out physical causes</li>
            <li>Assess for possible secondary gain from physical symptoms</li>
            <li>Evaluate for comorbid anxiety or depression that may exacerbate somatic concerns</li>
            <li>Consider cultural factors that may influence the expression of psychological distress</li>
        </ul>
        """
    
    # Default case for other patterns
    else:
        # For the specific 7-2-1-8 pattern in our sample
        if "7" in [s[0] for s in top_scales] and "2" in [s[0] for s in top_scales] and "1" in [s[0] for s in top_scales] and "8" in [s[0] for s in top_scales]:
            impressions["primary_diagnosis"] = """
            <p>The MMPI-2 profile suggests features consistent with <strong>Major Depressive Disorder with Anxious Distress and Somatic Symptom Disorder</strong> (F32.1, F45.1). The significant elevations on Scales 7 (Psychasthenia), 2 (Depression), 1 (Hypochondriasis), and 8 (Schizophrenia) indicate a complex clinical picture dominated by anxiety, depression, somatic concerns, and possible cognitive difficulties.</p>
            
            <p>The individual likely experiences:</p>
            <ul>
                <li>Persistent worry, rumination, and anxiety</li>
                <li>Depressed mood and anhedonia</li>
                <li>Significant somatic complaints and health concerns</li>
                <li>Cognitive inefficiency and possible unusual thought processes</li>
                <li>Social withdrawal and feelings of alienation</li>
            </ul>
            """
            
            impressions["differential_diagnosis"] = """
            <p>Consider the following differential diagnoses:</p>
            <ul>
                <li><strong>Persistent Depressive Disorder</strong> - If symptoms have been present for more than two years</li>
                <li><strong>Generalized Anxiety Disorder</strong> - If anxiety symptoms predominate and predate depressive symptoms</li>
                <li><strong>Somatic Symptom Disorder</strong> - If somatic concerns are the primary focus of distress</li>
                <li><strong>Schizophrenia Spectrum Disorder</strong> - If thought disturbance is more prominent than mood symptoms</li>
            </ul>
            """
            
            impressions["additional_considerations"] = """
            <p>Additional clinical considerations:</p>
            <ul>
                <li>Assess for suicidal ideation given the significant depression</li>
                <li>Evaluate for possible trauma history that may contribute to current symptoms</li>
                <li>Consider possible cognitive distortions contributing to anxiety and depression</li>
                <li>Ensure appropriate medical evaluation has been conducted to rule out physical causes for somatic complaints</li>
                <li>Assess for possible psychotic features that may require specific intervention</li>
            </ul>
            """
        else:
            impressions["primary_diagnosis"] = """
            <p>The MMPI-2 profile suggests features consistent with a complex clinical presentation that may include elements of mood, anxiety, and personality difficulties. Further clinical assessment is needed to determine the specific diagnostic picture.</p>
            
            <p>Based on the scale elevations, the individual likely experiences:</p>
            <ul>
                <li>Significant psychological distress across multiple domains</li>
                <li>Possible mood disturbance</li>
                <li>Anxiety or worry</li>
                <li>Interpersonal difficulties</li>
                <li>Possible maladaptive personality traits</li>
            </ul>
            """
            
            impressions["differential_diagnosis"] = """
            <p>Consider the following differential diagnoses based on further clinical assessment:</p>
            <ul>
                <li><strong>Mood Disorders</strong> - Including Major Depressive Disorder or Bipolar Disorders</li>
                <li><strong>Anxiety Disorders</strong> - Including Generalized Anxiety Disorder or Panic Disorder</li>
                <li><strong>Personality Disorders</strong> - Based on interpersonal patterns and trait stability</li>
                <li><strong>Trauma-Related Disorders</strong> - If trauma history is present</li>
            </ul>
            """
            
            impressions["additional_considerations"] = """
            <p>Additional clinical considerations:</p>
            <ul>
                <li>Conduct a thorough clinical interview to clarify symptom presentation</li>
                <li>Assess for substance use that may contribute to or exacerbate symptoms</li>
                <li>Evaluate for possible trauma history</li>
                <li>Consider medical conditions that may contribute to psychological symptoms</li>
                <li>Assess for risk factors including suicidal or homicidal ideation</li>
            </ul>
            """
    
    return impressions
