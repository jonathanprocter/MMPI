import importlib, sys

_modules = ['models']
for _m in _modules:
    sys.modules[f"{__name__}.{_m}"] = importlib.import_module(_m)
