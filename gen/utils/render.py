import os
import sys
from pathlib import Path

from config.settings import Settings
from dotenv import load_dotenv
from jinja2 import BaseLoader, Environment, TemplateError
from loguru import logger

load_dotenv(override=True)


def render_templates(
    raw_dir: str | Path,
    out_dir: str | Path,
    log_level: str = Settings.LOG_LEVEL,
):
    """Recursively processes a directory of Jinja2 templates and renders them.

    Loads environment variables into the context and interpolates them into
    the discovered templates, recreating the target directory structure.

    Args:
        raw_dir (str | Path): Path to the folder containing source templates.
        out_dir (str | Path): Path to the folder where rendered files will be saved.
        log_level (str, optional): The log level for this rendering execution.
            Defaults to Settings.LOG_LEVEL.

    Raises:
        SystemExit: If the source `raw_dir` directory does not exist.
    """
    logger.remove()
    logger.add(sys.stderr, level=log_level)

    if not raw_dir.exists():
        logger.error(f"Directory `{raw_dir}` not found!")
        sys.exit(1)

    logger.info(f"Start to render configs from `{raw_dir.name}`")

    jinja_env = Environment(loader=BaseLoader())
    context = dict(os.environ)

    for raw_file_path in raw_dir.rglob("*"):
        if not raw_file_path.is_file():
            continue

        relative_path = raw_file_path.relative_to(raw_dir)
        output_file_path = out_dir / relative_path

        logger.debug(f"Render: {relative_path} -> ")

        try:
            with open(raw_file_path, encoding="utf-8") as f:
                template_content = f.read()

            template = jinja_env.from_string(template_content)
            rendered_content = template.render(context)

            output_file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(rendered_content)

        except TemplateError as e:
            logger.error(f"Jinja2 error encountered: ({e})")
        except Exception as e:
            logger.exception(f"System error encountered: ({e})")

    logger.success("Render: Complete!")
