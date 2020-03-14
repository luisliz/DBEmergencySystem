from flask import Blueprint

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route('/')
def index():
    return "Welcome to dashboard"

@dashboard_bp.route('/resources/add')
def add_resource():
    pass

@dashboard_bp.route('/resource/delete')
def delete_resource():
    pass

@dashboard_bp.route('/statistics')
def statistics():
    pass

@dashboard_bp.route('/statistics/<region>')
def get_stats_by_region():
    pass

@dashboard_bp.route('/statistics/<city>')
def get_stats_by_city():
    pass

@dashboard_bp.route('/users')
def get_users:
    pass


