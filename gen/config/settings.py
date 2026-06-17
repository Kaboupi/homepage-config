class Settings:
    """Application-wide settings and constants used for configuration rendering.

    Attributes:
        TEMPLATE_DIR (str): The directory containing unrendered template files.
        RENDERED_DIR (str): The destination directory for rendered outputs.
        DIRS_TO_RENDER (tuple): Target subdirectories inside TEMPLATE_DIR to process.
        LOG_LEVEL (str): The default system logging level.
        LOG_LEVEL_CHOICES (tuple): Allowed values for the application log level.
    """

    TEMPLATE_DIR: str = "templates"
    RENDERED_DIR: str = "rendered"

    DIRS_TO_RENDER: tuple = (
        "config",
        "monitoring",
    )

    LOG_LEVEL: str = "INFO"
    LOG_LEVEL_CHOICES: tuple = (
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
    )
