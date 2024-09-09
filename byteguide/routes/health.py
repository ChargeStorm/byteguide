"""Health routes for the byteguide."""

from flask import Blueprint, jsonify

health_routes = Blueprint("health", __name__, template_folder="templates")


@health_routes.route("/health", methods=["get"])
def health():
    """
    Health check endpoint provides a simple way to check the health status of the service.
    This can be useful for monitoring and ensuring the service is running correctly.

    Returns:
        - status: ok
        - HTTP status code: 200
    """
    return jsonify({"status": "ok"})
