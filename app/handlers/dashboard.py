from flask import Blueprint

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route('/')
def index():
    return "Welcome to dashboard"
