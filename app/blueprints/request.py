from flask import Blueprint, request
from app.handlers.request import RequestHandler

request_bp = Blueprint('request', __name__)

@request_bp.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return RequestHandler().getAllRequests()
    elif request.method == 'POST':
        return RequestHandler().addRequest(request.form)


# @request_bp.route('/add/', methods=['POST']) #Done
# def add_request():
#     if request.method == 'POST':
#         return RequestHandler().addRequest(request.form)

@request_bp.route('/reqById/<int:reqid>/', methods=['GET']) #Done
def get_request_by_id(reqid):
    if request.method == 'GET':
        return RequestHandler().getRequestById(reqid)

@request_bp.route('/requester/<int:reqesterid>/', methods=['GET']) #Done
def get_requests_from_requester(reqesterid):
    if request.method == 'GET':
        return RequestHandler().getRequestsFromRequester(reqesterid)

@request_bp.route('/supplier/<int:supplierid>/', methods=['GET']) #Done
def get_requests_from_supplier(supplierid):
    if request.method == 'GET':
        return RequestHandler().getRequestsFromSupplier(supplierid)

@request_bp.route('/resources/<int:reqid>/', methods=['GET'])
def get_resources_from_requests(reqid):
    if request.method == 'GET':
        return RequestHandler().getResourcesFromRequest(reqid)

@request_bp.route('/resources/keyword/<string:rName>', methods=['GET'])
def get_requested_resources_by_keyword(rName):
    if request.method == 'GET':
        return RequestHandler().getRequestedResourcesByKeyword(rName)
"""
@request_bp.route('/resource/<int:rid>/', methods=['GET']) #Done
def get_request_by_resource_id(rid):
    if request.method == 'GET':
        return RequestHandler().getRequestByResourceId(rid)

@request_bp.route('/quantity/<int:reqid>/', methods=['GET']) #Done
def get_request_quantity(reqid):
    if request.method == 'GET':
        return RequestHandler().getRequestQuantity(reqid)

@request_bp.route('/dispatchdate/<int:reqid>/', methods=['GET']) #Done
def get_request_dispatch_date(reqid):
    if request.method == 'GET':
        return RequestHandler().getRequestDispatchDate(reqid)

@request_bp.route('/postdate/<int:reqid>/', methods=['GET']) #Done
def get_request_post_date(reqid):
    if request.method == 'GET':
        return RequestHandler().getRequestPostDate(reqid)

@request_bp.route('/location/<int:reqid>/', methods=['GET']) #Done
def get_request_location(reqid):
    if request.method == 'GET':
        return RequestHandler().getRequestLocation(reqid)

@request_bp.route('/update/', methods=['PUT']) #Done
def update_request():
    if request.method == 'PUT':
        return RequestHandler().updateRequest(request.form)

@request_bp.route('/delete/<int:reqid>/', methods=['DELETE']) #Done
def delete_request(reqid):
    if request.method == 'DELETE':
        return RequestHandler().removeRequest(reqid)
"""
@request_bp.route('/count/', methods=['GET']) #Done
def count_requests():
    if request.method == 'GET':
        return RequestHandler().countRequests()

@request_bp.route('/count/<int:rid>/', methods=['GET']) #Done
def count_requests_by_resource_id(rid):
    if request.method == 'GET':
        return RequestHandler().countRequestByResource(rid)

