import argparse

from config.settings import Settings


def parse_arguments():
    parser = argparse.ArgumentParser(description="Configurable log levels.")

    parser.add_argument(
        "--log-level",
        type=str,
        default=Settings.LOG_LEVEL,
        choices=Settings.LOG_LEVEL_CHOICES,
        help="Set the logging level (default: INFO)",
    )

    return parser.parse_args()
