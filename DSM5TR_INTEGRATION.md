# DSM-5-TR Integration for MMPI-2 Platform

## Overview
This document describes the integration of DSM-5-TR diagnostic decision trees into the MMPI-2 interpretation platform. The implementation provides algorithmically-derived diagnostic impressions based on MMPI-2 profile patterns, following established clinical decision trees.

## Files Added
1. **src/interpretation/dsm5tr_decision_trees.py**
   - Core implementation of DSM-5-TR diagnostic algorithms
   - Hierarchical decision tree approach for diagnostic impressions
   - Dimensional assessment of psychopathology
   - Treatment recommendation generation

2. **dsm5tr_sample_generator.py**
   - Sample script demonstrating the integration of DSM-5-TR algorithms
   - Creates clinically significant MMPI-2 profile
   - Generates comprehensive report with DSM-5-TR diagnostic impressions
   - Produces graphical representations of scale elevations

## Key Features

### Diagnostic Decision Trees
- **Hierarchical Approach**: Evaluates psychotic spectrum disorders first, followed by mood/anxiety disorders, then externalizing disorders
- **Code Type Analysis**: Incorporates traditional MMPI-2 code type interpretation
- **Dimensional Assessment**: Provides severity ratings across four key dimensions:
  - Thought Dysfunction
  - Emotional/Internalizing
  - Behavioral/Externalizing
  - Somatic Concerns

### Treatment Recommendations
- Algorithmically generates treatment recommendations based on diagnostic impressions
- Provides primary and adjunctive interventions
- Identifies special considerations for treatment planning
- Includes rationale for each recommendation

### Report Enhancements
- DSM-5-TR aligned diagnostic impressions section
- Treatment recommendations section
- Enhanced graphical representations
- Integrative summary incorporating diagnostic findings

## Usage
To generate a sample report with DSM-5-TR diagnostic impressions:
```
python3 dsm5tr_sample_generator.py
```

Output files will be created in the `dsm5tr_sample_output` directory:
- dsm5tr_sample_report.txt
- dsm5tr_sample_report.html
- dsm5tr_sample_report.pdf
- dsm5tr_sample_report.json
- traditional_profile_graph.pdf

## Implementation Details

### Diagnostic Algorithm
The diagnostic algorithm follows these steps:
1. Validate profile for response bias
2. Apply hierarchical decision tree for primary diagnostic considerations
3. Check for personality disorders
4. Apply dimensional approach for severity assessment
5. Generate treatment recommendations
6. Create narrative summaries

### Integration with Existing Platform
The DSM-5-TR module can be integrated with the existing report generation workflow by:
1. Importing the `get_diagnostic_impressions` and `get_treatment_recommendations` functions
2. Passing the profile data to these functions
3. Including the returned diagnostic impressions and treatment recommendations in the report

## Future Enhancements
Potential future enhancements include:
- Expanded decision trees for specialized populations
- Integration with external clinical databases
- Machine learning refinement of diagnostic algorithms
- Interactive decision support for clinicians
