"""ByteGuide Flask app initialization."""
import os
from flask import Flask

from byteguide.config import config
from byteguide.libs.jinja_fltrs import register_filters
from byteguide.routes.common import common_routes
from byteguide.routes.display import display_routes
from byteguide.routes.manage import manage_routes
from pathlib import Path
from loguru import logger as log

def create_app():
    app = Flask(__name__)

    app.config.from_object(config)
    app.config["MAX_CONTENT_LENGTH"] = config.max_content_mb * 1024 * 1024

    register_blueprints(app)
    register_filters()

    create_symlink()

    return app

def register_blueprints(app):
    app.register_blueprint(common_routes)
    app.register_blueprint(display_routes)
    app.register_blueprint(manage_routes)

def create_symlink():
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
        except OSError as e:
            # Handle symlink creation failure
            log.error(f"Symlink creation failed: {e}")
            raise e

app = create_app()