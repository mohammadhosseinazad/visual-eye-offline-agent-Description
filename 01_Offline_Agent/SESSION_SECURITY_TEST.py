#!/usr/bin/env python3
"""Regression tests for persisted session path and schema validation."""
import json
import tempfile
from pathlib import Path
from engine.state import Session

def rejected(root: Path, sid: str, payload: dict) -> bool:
    target = root / "data" / "sessions" / f"{sid}.json"
    target.write_text(json.dumps(payload), encoding="utf-8")
    try:
        Session.load(root, sid)
    except (ValueError, TypeError, KeyError):
        return True
    return False

def main():
    with tempfile.TemporaryDirectory() as td:
        root = Path(td)
        (root / "data" / "sessions").mkdir(parents=True)
        (root / "data" / "uploads").mkdir(parents=True)
        sid = "a" * 32
        assert rejected(root, sid, {"id": sid, "image_path": "/etc/passwd", "user_order": []})
        assert rejected(root, sid, {"id": sid, "image_path": "", "user_order": "not-a-list"})
        assert rejected(root, sid, {"id": sid, "image_path": "", "user_order": ["x"] * 33})
        good = Session.new()
        good.save(root)
        assert Session.load(root, good.id).id == good.id
    print("PASS session security: upload path confinement and persisted schema validation")

if __name__ == "__main__":
    main()
