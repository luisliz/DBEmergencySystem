#unnecessary comment
from flask import Blueprint, request
from app.handlers.request import RequestHandler

request_bp = Blueprint('request', __name__)

@request_bp.route('/')
def index():
    return "Welcome to the requests page??"

@request_bp.route('/all/', methods=['GET']) #Done
def get_all_requests():
    if request.method == 'GET':
        return RequestHandler().getAllRequests()

@request_bp.route('/add/', methods=['POST'])
def add_request():
    if request.method == 'POST':
        return RequestHandler().addRequest(request.form)