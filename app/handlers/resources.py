from flask import Blueprint

resources_bp = Blueprint('resources', __name__)

@resources_bp.route('/')
def index():
    return "Welcome to resources"

@resources_bp.route('/resource/<resource_id>')
def get_resource_by_id: 
    pass 

@resources_bp.route('/search')
def search():
    pass

@resources_bp.route('/browse/type')
def type(): 
    pass

@resources_bp.route('/browse/need')
def browse_need():
    pass

@resources_bp.route('/browse/available')
def browse_available():
    pass

@resources_bp.route('/request/<string:category>/')
def request_type(category):
    pass

@resources_bp.route('/request/other')
def request_other():
    pass

@resources_bp.route('/reserve/')
def reserve_resource(): 
    pass

@resources_bp.route('/purchase/')
def purchase_resource(): 
    pass

