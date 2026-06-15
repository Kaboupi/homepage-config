from pathlib import Path

from utils.render import render_templates

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "config-raw"
OUT_DIR = BASE_DIR / "config"

if __name__ == "__main__":
    render_templates(
        raw_dir=RAW_DIR,
        out_dir=OUT_DIR,
    )

