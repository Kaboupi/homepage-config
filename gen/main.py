from pathlib import Path
import sys

from loguru import logger

from config.settings import Settings
from utils import (
    parse_arguments,
    render_templates,
)

args = parse_arguments()
log_level = args.log_level

logger.remove()
logger.add(sys.stderr, level=log_level)

BASE_DIR = Path(__file__).resolve().parent.parent

if __name__ == "__main__":
    logger.info(f"Current LOG_LEVEL: {log_level}")
    logger.info(
        "Can be changed via "
        "`make run LOG_LEVEL=["
        f"{'|'.join(Settings.LOG_LEVEL_CHOICES)}]`"
    )

    for dir_to_render in Settings.DIRS_TO_RENDER:

        raw_dir = BASE_DIR / Settings.TEMPLATE_DIR / dir_to_render
        logger.debug(f"raw_dir: `{raw_dir}`")
        out_dir = BASE_DIR / Settings.RENDERED_DIR / dir_to_render
        logger.debug(f"out_dir: `{out_dir}`")

        render_templates(raw_dir=raw_dir, out_dir=out_dir, log_level=log_level)
