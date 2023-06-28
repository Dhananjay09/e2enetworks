import yaml
from typing import Dict, Any

def load_yaml(
    path: str,
) -> Dict[str, Any]:
    _load_from_local(path)

def _load_from_local(path: str) -> Dict[str, Any]:
    with open(path) as f:
        return yaml.safe_load(f)