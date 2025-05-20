import importlib, sys

_modules = [
    'clinical_scales',
    'rc_scales',
    'content_scales',
    'content_component_scales',
    'psy5_scales',
    'harris_lingoes_subscales',
    'supplementary_scales',
    'validity_scales',
    'scale_interpretations',
    'narrative_dsm5tr_integration',
    'component_scales'
]
for _m in _modules:
    sys.modules[f"{__name__}.{_m}"] = importlib.import_module(_m)
