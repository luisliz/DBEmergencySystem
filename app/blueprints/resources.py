from flask import Blueprint, request
from app.handlers.resources import ResourceHandler

resources_bp = Blueprint('resources', __name__)

@resources_bp.route('/')
def index():
    return "Welcome to Resources!!"

@resources_bp.route('/all/', methods=['GET']) #Done
def get_all_resources():
    if request.method == 'GET':
        return ResourceHandler().get_all_resources()

@resources_bp.route('/details/<int:rid>/', methods=['GET']) #Done
def get_resource_details(rid):
    if request.method == 'GET':
        return ResourceHandler().get_resource_details_by_rid(rid)

@resources_bp.route('/<int:rid>/', methods=['GET']) #Done
def get_resource_by_id(rid):
    if request.method == 'GET':
        return ResourceHandler().get_resource_by_id(rid)

@resources_bp.route('/search/<string:rName>/', methods=['GET']) #Done
def search_by_name(rName):
    if request.method == 'GET':
        return ResourceHandler().get_resource_by_name(rName)

@resources_bp.route('/browse/category/<string:category>/', methods=['GET']) #Done
def browse_by_category(category):
    if request.method == 'GET':
        return ResourceHandler().get_resources_by_category(category)

@resources_bp.route('/browse/availability/<string:avail>/', methods=['GET']) #Done
def browse_by_availability(avail):
    if request.method == 'GET':
        return ResourceHandler().get_resources_by_availability(avail)

@resources_bp.route('/supplier/r/<int:rid>/', methods=['GET']) #Done
def get_supplier_by_resource_id(rid):
    if request.method == 'GET':
        return ResourceHandler().get_supplier_by_resource_id(rid)

@resources_bp.route('/add/', methods=['POST']) #Done
def add_resource():
    if request.method == 'POST':
        return ResourceHandler().add_resource(request.form)

@resources_bp.route('/delete/', methods=['DELETE']) #Done
def delete_resource():
    if request.method == 'DELETE':
        return ResourceHandler().delete_resource(request.form)

@resources_bp.route('/update/', methods=['PUT']) #Done
def update_resource():
    if request.method == 'PUT':
        return ResourceHandler().update_resource(request.form)

@resources_bp.route('/browse/requested/', methods=['GET']) #Done
def browse_requested():
    if request.method == 'GET':
        return ResourceHandler().get_requested_resources()

@resources_bp.route('/browse/requested/dispatched/', methods=['GET'])
def browse_dispatched_requested():
    if request.method == 'GET':
        return ResourceHandler().get_dispatched_requested_resources()

@resources_bp.route('/browse/requested/undispatched/', methods=['GET'])
def browse_undispatched_requested():
    if request.method == 'GET':
        return ResourceHandler().get_undispatched_requested_resources()

@resources_bp.route('/browse/requested/<int:rid>/', methods=['GET']) #Done
def browse_requested_by_resource_id(rid):
    if request.method == 'GET':
        return ResourceHandler().get_requested_resource_by_id(rid)

@resources_bp.route('/reserve/<int:rid>/', methods=['PUT']) #Done
def reserve_resource(rid):
    if request.method == 'PUT':
        return ResourceHandler().reserve_resource(rid, 'reserved')

@resources_bp.route('/purchase/<int:rid>/', methods=['PUT']) #Done
def purchase_resource(rid):
    if request.method == 'PUT':
        return ResourceHandler().purchase_resource(rid, 'purchased')

