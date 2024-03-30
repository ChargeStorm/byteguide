import os

from loguru import logger as log
from pathlib import Path

from byteguide import app
from byteguide.config import config

def main():
    created_symlink: bool = False
    docfiles_dir = Path(config.docfiles_dir)

    # Check if docfiles dir exists
    if not docfiles_dir.exists():
        raise FileNotFoundError(f"Docfiles directory does not exist: {docfiles_dir}")

    # If docfiles dir does not start with byteguide/static we need to create a symlink to the static folder for simplicity of serving files
    if not config.docfiles_dir.startswith("byteguide/static"):
        try:
            log.info(f"Creating symlink from {docfiles_dir} to byteguide/static/docfiles")
            # Create symlink if it does not already exist
            if not os.path.exists("byteguide/static/docfiles"):
                os.symlink(docfiles_dir, "byteguide/static/docfiles", target_is_directory=True)
            created_symlink = True
        except OSError as e:
            # Handle symlink creation failure
            log.error(f"Symlink creation failed: {e}")
            created_symlink = False
            raise e

    try:
        app.run(host=config.host, port=config.port, debug=config.debug)
    finally:
        # Clean up symlink if it was created
        if created_symlink:
            if os.path.exists("byteguide/static/docfiles"):
                os.unlink("byteguide/static/docfiles")

if __name__ == "__main__":
    main()