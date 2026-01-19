from pathlib import Path
import json
from typing import Any

def load_json(path: str) -> Any:
    p = Path(path)
    if not p.exists():
        return []
    with p.open("r", encoding="utf-8") as f:
        try: 
            return json.load(f)
        except json.JSONDecodeError:
            return []
        
def save_json(path: str, data: Any) -> None:
    p = Path(path)
    with p.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)