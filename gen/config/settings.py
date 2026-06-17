class Settings:
    TEMPLATE_DIR: str = "templates"
    RENDERED_DIR: str = "rendered"

    DIRS_TO_RENDER: tuple = (
        "config",
        "monitoring",
    )

    LOG_LEVEL: str = "INFO"
    LOG_LEVEL_CHOICES: list = (
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
    )
