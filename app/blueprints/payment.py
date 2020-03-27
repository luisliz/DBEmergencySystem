from flask import Blueprint

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('')
def index():
    return "Welcome to payment"

@payment_bp.route('/browse', methods =['GET'])
def get_payments():
     return "ALL PAYMENTS"

@payment_bp.route('/browse/<Card_id>', methods =['GET'])
def get_payment_by_id():
    return f"ALL PAYMENTS WITH ID: <Card_id>"

@payment_bp.route('/browse/<Card_provider>', methods=['GET'])
def provider():
    return f"ALL PAYMENTS WITH provider: <Card_provider>"

@payment_bp.route('/browse/<Card_type>', methods=['GET'])
def card_type():
    return f"ALL PAYMENTS WITH type: <Card_type>"

@payment_bp.route('/browse/<Card_exp_date>', methods=['GET'])
def exp_date():
    return f"ALL PAYMENTS WITH expiration date: <Card_exp_date>"

@payment_bp.route('/add/', methods=['POST'])
def add_payment():
    return "ADD Cards"



