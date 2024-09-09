from flask import Blueprint, jsonify

health_routes = Blueprint("health", __name__, template_folder="templates")


@health_routes.route("/health", methods=["get"])
def health():
    """Health check endpoint for the byteguide service"""
    return jsonify({"status": "ok"})
