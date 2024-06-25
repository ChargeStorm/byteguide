"""Default configuration for byteguide."""
from pathlib import Path


def get():
    """
    Get the default configuration.

    Returns:
        The default configuration.
    """
    return {
        "docfiles_dir": "/mnt/docshost-volume", #! This path is a mounted file share from Azure Blob Storage
        "copyright": "All rights reserved © CTEK Sweden AB 2016-2024",
        "title": "CTEK Docshost",
        # "welcome": "Hello there!, \n - From byte/guide!",
        "intro_line1": "Welcome to CTEKs internal documentation hosting site!",
        "intro_line2": (
            "<br>Follow the buttons in the upper right corner to browse available projects or learn how to upload your own project.<br><br>"
            "Remember that this site is purely for hosting <b>internal</b> documentation."
        ),
        # "footer": "All rights reserved © CTEK Sweden AB 2016-2024",
        "host": "0.0.0.0",
        "port": 8000,
        "debug": True,
        "readonly": False,
        "disable_delete": False,
        "max_content_mb": 100,
        # "enable_email_notification": False,
        # "smpt_server": "",
        # "smpt_port": 587,
        # "smpt_username": "",
        # "smtp_password": "",
    }
