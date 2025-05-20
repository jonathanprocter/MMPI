import importlib, sys

_modules = [
    'comprehensive_report_generator',
    'profile_graph_generator',
    'report_generator',
    'embedded_graphs_report_generator',
    'final_comprehensive_report_generator',
    'gender_comparison_report_generator',
    'harmonized_report_generator',
    'revised_clinical_sample',
    'enhanced_clinical_sample',
    'dsm5tr_sample_generator',
    'create_clinical_sample'
]
for _m in _modules:
    try:
        sys.modules[f"{__name__}.{_m}"] = importlib.import_module(_m)
    except ModuleNotFoundError:
        pass
