from flask import Blueprint

resources_bp = Blueprint('resources', __name__)

@resources_bp.route('/')
def index():
    return "Welcome to resources"
