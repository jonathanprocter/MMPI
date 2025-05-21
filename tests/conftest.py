import sys
import types

# Create stub modules to satisfy imports in webapp
src_pkg = types.ModuleType('src')
reporting_pkg = types.ModuleType('src.reporting')
constants_pkg = types.ModuleType('src.constants')

comp_mod = types.ModuleType('src.reporting.comprehensive_report_generator')
prof_mod = types.ModuleType('src.reporting.profile_graph_generator')

class DummyReportGen:
    def __init__(self, *args, **kwargs):
        pass
    def generate_report(self, *args, **kwargs):
        return {}

class DummyGraphGen:
    def __init__(self, *args, **kwargs):
        pass
    def generate_all_graphs(self, *args, **kwargs):
        return {}

comp_mod.ComprehensiveReportGenerator = DummyReportGen
prof_mod.ProfileGraphGenerator = DummyGraphGen

scale_constants_mod = types.ModuleType('src.constants.scale_constants')
scale_constants_mod.VALIDITY_SCALES_MAP = {'L': 'Lie'}
scale_constants_mod.CLINICAL_SCALES_MAP = {'1': 'Hs'}
scale_constants_mod.HARRIS_LINGOES_SUBSCALES_MAP = {}
scale_constants_mod.CONTENT_SCALES_MAP = {}
scale_constants_mod.RC_SCALES_MAP = {}
scale_constants_mod.PSY5_SCALES_MAP = {}
scale_constants_mod.SUPPLEMENTARY_SCALES_MAP = {}

# Register modules in sys.modules
sys.modules['src'] = src_pkg
sys.modules['src.reporting'] = reporting_pkg
sys.modules['src.reporting.comprehensive_report_generator'] = comp_mod
sys.modules['src.reporting.profile_graph_generator'] = prof_mod
sys.modules['src.constants'] = constants_pkg
sys.modules['src.constants.scale_constants'] = scale_constants_mod

# Expose submodules on packages
reporting_pkg.comprehensive_report_generator = comp_mod
reporting_pkg.profile_graph_generator = prof_mod
constants_pkg.scale_constants = scale_constants_mod
