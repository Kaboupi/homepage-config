import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from jinja2 import Environment, BaseLoader, TemplateError

load_dotenv(override=True)


def render_templates(
    raw_dir: str | Path,
    out_dir: str | Path,
):
    if not raw_dir.exists():
        print(f"[Ошибка] Папка {raw_dir} не найдена!")
        sys.exit(1)

    print(f"=== Начало генерации конфигов из {raw_dir.name} ===")

    jinja_env = Environment(loader=BaseLoader())

    context = dict(os.environ)

    for raw_file_path in raw_dir.rglob("*"):
        if not raw_file_path.is_file():
            continue

        relative_path = raw_file_path.relative_to(raw_dir)
        output_file_path = out_dir / relative_path

        print(f"Обработка: {relative_path} -> ", end="")

        try:
            with open(raw_file_path, "r", encoding="utf-8") as f:
                template_content = f.read()

            template = jinja_env.from_string(template_content)
            rendered_content = template.render(context)

            output_file_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(rendered_content)

            print("Успешно")

        except TemplateError as e:
            print(f"ОШИБКА JINJA2 ({e})")
        except Exception as e:
            print(f"СИСТЕМНАЯ ОШИБКА ({e})")

    print("=== Генерация успешно завершена ===")

