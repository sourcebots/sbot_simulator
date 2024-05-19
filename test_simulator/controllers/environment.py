import sys
from pathlib import Path

SIM_ROOT = Path(__file__).absolute().parents[2] / 'simulator'
ZONE_ROOT = SIM_ROOT.parent
MODULES_ROOT = SIM_ROOT / 'modules'


def setup_environment():
    sys.path.insert(0, str(MODULES_ROOT))
    this_dir = str(Path(__file__).parent)
    if this_dir in sys.path:
        sys.path.remove(this_dir)