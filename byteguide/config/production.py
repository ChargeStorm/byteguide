"""Default configuration for byteguide."""
from pathlib import Path


def get():
    """
    Get the default configuration.

    Returns:
        The default configuration.
    """
    return {
        "docfiles_dir": Path("/home/azureuser/byteguide_docs"),
        "docfiles_link_root": "/static/docfiles",
        "copyright": "All rights reserved © CTEK Sweden AB 2016-2024",
        "title": "CTEK Docshost",
        # "welcome": "Hello there!, \n - From byte/guide!",
        "intro_line1": "Welcome to CTEKs internal code documentation hosting site!",
        "intro_line2": "Follow the buttons in the upper right corner to browse available projects or learn how to upload your own project.",
        # "footer": "All rights reserved © CTEK Sweden AB 2016-2024",
        "host": "0.0.0.0",
        "port": 29000,
        "debug": True,
        "readonly": True,
        "disable_delete": False,
        "max_content_mb": 10,
        # "enable_email_notification": False,
        # "smpt_server": "",
        # "smpt_port": 587,
        # "smpt_username": "",
        # "smtp_password": "",
    }
