from flask import Blueprint, url_for, flash, request
from app.handlers.resource_category import ResourceCategoryHandler

resource_category_bp = Blueprint('resource_category', __name__)

@resource_category_bp.route('/', methods=['GET', 'POST'])
def resource_category():
    if request.method == 'POST':
        return ResourceCategoryHandler().add_category(request.form)
    else:
        return ResourceCategoryHandler().get_all_categories()

@resource_category_bp.route('/<int:rcid>/', methods=['GET'])
def get_category_by_id(rcid):
    if request.method == 'GET':
        return ResourceCategoryHandler().get_category_by_id(rcid)

@resource_category_bp.route('/delete', methods=['DELETE']) #need to verify that this works
def delete_category():
    if request.method == 'DELETE':
        return ResourceCategoryHandler().delete_category(request.form)

@resource_category_bp.route('/update/{rcid}', methods=['PUT']) #need to verify
def update_category(rcid):
    if request.method == 'PUT':
        return ResourceCategoryHandler().update_category(rcid, request.form)
