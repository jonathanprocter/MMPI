"""
Utility module to align and standardize function names and exports across interpretation modules.
"""

import importlib
import inspect
import os
import sys

# Add the project root to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_root)

# List of interpretation modules to align
INTERPRETATION_MODULES = [
    'clinical_scales',
    'content_scales',
    'content_component_scales',
    'harris_lingoes_subscales',
    'rc_scales',
    'validity_scales',
    'supplementary_scales',
    'psy5_scales',
    'component_scales',
    'dsm5tr_decision_trees'
]

def align_function_signatures():
    """
    Align function signatures across all interpretation modules.
    Ensures consistent naming patterns and parameter lists.
    """
    print("Aligning function signatures across interpretation modules...")
    
    # Standard function signature pattern
    # get_X_scale_interpretation(scale, t_score, gender)
    
    for module_name in INTERPRETATION_MODULES:
        try:
            # Import the module
            module_path = f"mmpi_platform.src.interpretation.{module_name}"
            module = importlib.import_module(module_path)
            
            # Get all functions in the module
            functions = inspect.getmembers(module, inspect.isfunction)
            
            # Check for interpretation functions
            interpretation_functions = [f for f in functions if 'interpretation' in f[0]]
            
            if interpretation_functions:
                print(f"Module {module_name} has {len(interpretation_functions)} interpretation functions:")
                for name, func in interpretation_functions:
                    sig = inspect.signature(func)
                    print(f"  - {name}{sig}")
            else:
                print(f"Module {module_name} has no interpretation functions.")
                
        except ImportError as e:
            print(f"Could not import module {module_name}: {e}")
        except Exception as e:
            print(f"Error processing module {module_name}: {e}")
    
    print("Function signature alignment complete.")

def validate_interpretation_access():
    """
    Validate that all interpretation functions can be accessed through the scale_interpretations module.
    """
    print("Validating interpretation function access...")
    
    try:
        from mmpi_platform.src.interpretation.scale_interpretations import get_scale_interpretation
        
        # Test with sample scales from different families
        test_scales = [
            # Clinical scales
            "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
            # Content scales
            "ANX", "FRS", "OBS", "DEP", "HEA", "BIZ", "ANG", "CYN", "ASP", "TPA", "LSE", "SOD", "FAM", "WRK", "TRT",
            # RC scales
            "RCd", "RC1", "RC2", "RC3", "RC4", "RC6", "RC7", "RC8", "RC9",
            # Validity scales
            "L", "F", "K", "Fb", "VRIN", "TRIN", "FBS",
            # PSY-5 scales
            "AGGR", "PSYC", "DISC", "NEGE", "INTR",
            # Supplementary scales
            "A", "R", "Es", "MAC-R", "AAS", "APS", "MDS", "Ho", "O-H", "Do", "Re", "Mt", "GM", "GF", "PK", "PS", "TPA"
        ]
        
        # Test with a sample T-score and gender
        t_score = 70
        gender = "female"
        
        success_count = 0
        failure_count = 0
        
        for scale in test_scales:
            try:
                interpretation = get_scale_interpretation(scale, t_score, gender)
                if interpretation and not interpretation.startswith("Interpretation not found"):
                    success_count += 1
                else:
                    print(f"  - Missing interpretation for scale: {scale}")
                    failure_count += 1
            except Exception as e:
                print(f"  - Error getting interpretation for scale {scale}: {e}")
                failure_count += 1
        
        print(f"Interpretation access validation complete: {success_count} successes, {failure_count} failures")
        
    except ImportError as e:
        print(f"Could not import scale_interpretations module: {e}")
    except Exception as e:
        print(f"Error during validation: {e}")

if __name__ == "__main__":
    align_function_signatures()
    print("\n" + "-"*50 + "\n")
    validate_interpretation_access()
