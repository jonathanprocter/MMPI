"""
Scale constants for the MMPI-2 platform.

This module defines constants related to scale ordering, display names,
and other scale-specific information used throughout the platform.
"""

# Validity Scales
VALIDITY_SCALES_ORDER = ["?", "VRIN", "TRIN", "F", "FB", "FP", "L", "K", "S"]
VALIDITY_SCALES_DISPLAY_NAMES = {
    "?": "Cannot Say",
    "VRIN": "Variable Response Inconsistency",
    "TRIN": "True Response Inconsistency",
    "F": "Infrequency",
    "FB": "Back F",
    "FP": "Infrequency-Psychopathology",
    "L": "Lie",
    "K": "Correction",
    "S": "Superlative Self-Presentation"
}

# Clinical Scales
CLINICAL_SCALES_ORDER = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
CLINICAL_SCALES_DB_KEYS = {
    "1": "Hs", "2": "D", "3": "Hy", "4": "Pd", "5": "Mf", 
    "6": "Pa", "7": "Pt", "8": "Sc", "9": "Ma", "0": "Si"
}
CLINICAL_SCALES_DISPLAY_NAMES = {
    "1": "Hypochondriasis",
    "2": "Depression",
    "3": "Hysteria",
    "4": "Psychopathic Deviate",
    "5": "Masculinity-Femininity",
    "6": "Paranoia",
    "7": "Psychasthenia",
    "8": "Schizophrenia",
    "9": "Hypomania",
    "0": "Social Introversion"
}
CLINICAL_SCALES_MAP = {
    "1": {"name": "Hypochondriasis", "db_key": "Hs"},
    "2": {"name": "Depression", "db_key": "D"},
    "3": {"name": "Hysteria", "db_key": "Hy"},
    "4": {"name": "Psychopathic Deviate", "db_key": "Pd"},
    "5": {"name": "Masculinity-Femininity", "db_key": "Mf"},
    "6": {"name": "Paranoia", "db_key": "Pa"},
    "7": {"name": "Psychasthenia", "db_key": "Pt"},
    "8": {"name": "Schizophrenia", "db_key": "Sc"},
    "9": {"name": "Hypomania", "db_key": "Ma"},
    "0": {"name": "Social Introversion", "db_key": "Si"}
}

# Harris-Lingoes Subscales
HARRIS_LINGOES_SUBSCALES_ORDER = [
    "D1", "D2", "D3", "D4", "D5",
    "Hy1", "Hy2", "Hy3", "Hy4", "Hy5",
    "Pd1", "Pd2", "Pd3", "Pd4", "Pd5",
    "Pa1", "Pa2", "Pa3",
    "Sc1", "Sc2", "Sc3", "Sc4", "Sc5", "Sc6",
    "Ma1", "Ma2", "Ma3", "Ma4"
]
HARRIS_LINGOES_SUBSCALES_DISPLAY_NAMES = {
    "D1": "Subjective Depression",
    "D2": "Psychomotor Retardation",
    "D3": "Physical Malfunctioning",
    "D4": "Mental Dullness",
    "D5": "Brooding",
    "Hy1": "Denial of Social Anxiety",
    "Hy2": "Need for Affection",
    "Hy3": "Lassitude-Malaise",
    "Hy4": "Somatic Complaints",
    "Hy5": "Inhibition of Aggression",
    "Pd1": "Familial Discord",
    "Pd2": "Authority Problems",
    "Pd3": "Social Imperturbability",
    "Pd4": "Social Alienation",
    "Pd5": "Self-Alienation",
    "Pa1": "Persecutory Ideas",
    "Pa2": "Poignancy",
    "Pa3": "Naiveté",
    "Sc1": "Social Alienation",
    "Sc2": "Emotional Alienation",
    "Sc3": "Lack of Ego Mastery, Cognitive",
    "Sc4": "Lack of Ego Mastery, Conative",
    "Sc5": "Lack of Ego Mastery, Defective Inhibition",
    "Sc6": "Bizarre Sensory Experiences",
    "Ma1": "Amorality",
    "Ma2": "Psychomotor Acceleration",
    "Ma3": "Imperturbability",
    "Ma4": "Ego Inflation"
}
HARRIS_LINGOES_SUBSCALES_MAP = {
    "D1": {"name": "Subjective Depression", "parent": "2"},
    "D2": {"name": "Psychomotor Retardation", "parent": "2"},
    "D3": {"name": "Physical Malfunctioning", "parent": "2"},
    "D4": {"name": "Mental Dullness", "parent": "2"},
    "D5": {"name": "Brooding", "parent": "2"},
    "Hy1": {"name": "Denial of Social Anxiety", "parent": "3"},
    "Hy2": {"name": "Need for Affection", "parent": "3"},
    "Hy3": {"name": "Lassitude-Malaise", "parent": "3"},
    "Hy4": {"name": "Somatic Complaints", "parent": "3"},
    "Hy5": {"name": "Inhibition of Aggression", "parent": "3"},
    "Pd1": {"name": "Familial Discord", "parent": "4"},
    "Pd2": {"name": "Authority Problems", "parent": "4"},
    "Pd3": {"name": "Social Imperturbability", "parent": "4"},
    "Pd4": {"name": "Social Alienation", "parent": "4"},
    "Pd5": {"name": "Self-Alienation", "parent": "4"},
    "Pa1": {"name": "Persecutory Ideas", "parent": "6"},
    "Pa2": {"name": "Poignancy", "parent": "6"},
    "Pa3": {"name": "Naiveté", "parent": "6"},
    "Sc1": {"name": "Social Alienation", "parent": "8"},
    "Sc2": {"name": "Emotional Alienation", "parent": "8"},
    "Sc3": {"name": "Lack of Ego Mastery, Cognitive", "parent": "8"},
    "Sc4": {"name": "Lack of Ego Mastery, Conative", "parent": "8"},
    "Sc5": {"name": "Lack of Ego Mastery, Defective Inhibition", "parent": "8"},
    "Sc6": {"name": "Bizarre Sensory Experiences", "parent": "8"},
    "Ma1": {"name": "Amorality", "parent": "9"},
    "Ma2": {"name": "Psychomotor Acceleration", "parent": "9"},
    "Ma3": {"name": "Imperturbability", "parent": "9"},
    "Ma4": {"name": "Ego Inflation", "parent": "9"}
}

# Restructured Clinical Scales
RESTRUCTURED_CLINICAL_SCALES_ORDER = [
    "RCd", "RC1", "RC2", "RC3", "RC4", "RC6", "RC7", "RC8", "RC9"
]
RESTRUCTURED_CLINICAL_SCALES_DISPLAY_NAMES = {
    "RCd": "Demoralization",
    "RC1": "Somatic Complaints",
    "RC2": "Low Positive Emotions",
    "RC3": "Cynicism",
    "RC4": "Antisocial Behavior",
    "RC6": "Ideas of Persecution",
    "RC7": "Dysfunctional Negative Emotions",
    "RC8": "Aberrant Experiences",
    "RC9": "Hypomanic Activation"
}

# Content Scales
CONTENT_SCALES_ORDER = [
    "ANX", "FRS", "OBS", "DEP", "HEA", "BIZ", "ANG", "CYN",
    "ASP", "TPA", "LSE", "SOD", "FAM", "WRK", "TRT"
]
CONTENT_SCALES_DISPLAY_NAMES = {
    "ANX": "Anxiety",
    "FRS": "Fears",
    "OBS": "Obsessiveness",
    "DEP": "Depression",
    "HEA": "Health Concerns",
    "BIZ": "Bizarre Mentation",
    "ANG": "Anger",
    "CYN": "Cynicism",
    "ASP": "Antisocial Practices",
    "TPA": "Type A",
    "LSE": "Low Self-Esteem",
    "SOD": "Social Discomfort",
    "FAM": "Family Problems",
    "WRK": "Work Interference",
    "TRT": "Negative Treatment Indicators"
}

# Content Component Scales
CONTENT_COMPONENT_SCALES_ORDER = [
    "ANX1", "ANX2", "FRS1", "FRS2", "OBS1", "OBS2", "DEP1", "DEP2", "DEP3", "DEP4",
    "HEA1", "HEA2", "HEA3", "BIZ1", "BIZ2", "ANG1", "ANG2", "CYN1", "CYN2", "ASP1",
    "ASP2", "TPA1", "TPA2", "LSE1", "LSE2", "SOD1", "SOD2", "FAM1", "FAM2", "WRK1",
    "WRK2", "TRT1", "TRT2"
]
CONTENT_COMPONENT_SCALES_DISPLAY_NAMES = {
    "ANX1": "Anxious Thoughts",
    "ANX2": "Anxious Feelings",
    "FRS1": "Generalized Fears",
    "FRS2": "Multiple Fears",
    "OBS1": "Obsessive Thoughts",
    "OBS2": "Compulsive Behaviors",
    "DEP1": "Lack of Drive",
    "DEP2": "Dysphoria",
    "DEP3": "Self-Deprecation",
    "DEP4": "Suicidal Ideation",
    "HEA1": "Gastrointestinal Symptoms",
    "HEA2": "Neurological Symptoms",
    "HEA3": "General Health Concerns",
    "BIZ1": "Psychotic Symptomatology",
    "BIZ2": "Schizotypal Characteristics",
    "ANG1": "Explosive Behavior",
    "ANG2": "Irritability",
    "CYN1": "Misanthropic Beliefs",
    "CYN2": "Interpersonal Suspiciousness",
    "ASP1": "Antisocial Attitudes",
    "ASP2": "Antisocial Behavior",
    "TPA1": "Impatience",
    "TPA2": "Competitive Drive",
    "LSE1": "Self-Doubt",
    "LSE2": "Submissiveness",
    "SOD1": "Introversion",
    "SOD2": "Shyness",
    "FAM1": "Family Discord",
    "FAM2": "Familial Alienation",
    "WRK1": "Work Aversion",
    "WRK2": "Work Performance Difficulties",
    "TRT1": "Low Motivation",
    "TRT2": "Inability to Disclose"
}

# Supplementary Scales
SUPPLEMENTARY_SCALES_ORDER = [
    "A", "R", "Es", "MAC-R", "AAS", "APS", "MDS", "Ho", "O-H",
    "Do", "Re", "Mt", "GM", "GF", "PK", "PS"
]
SUPPLEMENTARY_SCALES_DISPLAY_NAMES = {
    "A": "Anxiety",
    "R": "Repression",
    "Es": "Ego Strength",
    "MAC-R": "MacAndrew Alcoholism Scale-Revised",
    "AAS": "Addiction Acknowledgment Scale",
    "APS": "Addiction Potential Scale",
    "MDS": "Marital Distress",
    "Ho": "Hostility",
    "O-H": "Overcontrolled Hostility",
    "Do": "Dominance",
    "Re": "Social Responsibility",
    "Mt": "College Maladjustment",
    "GM": "Gender Role - Masculine",
    "GF": "Gender Role - Feminine",
    "PK": "Post-Traumatic Stress Disorder",
    "PS": "Post-Traumatic Stress Disorder Supplementary"
}

# PSY-5 Scales
PSY5_SCALES_ORDER = ["AGGR", "PSYC", "DISC", "NEGE", "INTR"]
PSY5_SCALES_DISPLAY_NAMES = {
    "AGGR": "Aggressiveness",
    "PSYC": "Psychoticism",
    "DISC": "Disconstraint",
    "NEGE": "Negative Emotionality/Neuroticism",
    "INTR": "Introversion/Low Positive Emotionality"
}

# Two-Point Code Types
TWO_POINT_CODE_TYPES = [
    "1-2", "1-3", "1-4", "1-5", "1-6", "1-7", "1-8", "1-9", "1-0",
    "2-3", "2-4", "2-5", "2-6", "2-7", "2-8", "2-9", "2-0",
    "3-4", "3-5", "3-6", "3-7", "3-8", "3-9", "3-0",
    "4-5", "4-6", "4-7", "4-8", "4-9", "4-0",
    "5-6", "5-7", "5-8", "5-9", "5-0",
    "6-7", "6-8", "6-9", "6-0",
    "7-8", "7-9", "7-0",
    "8-9", "8-0",
    "9-0"
]
