from flask import Blueprint

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/')
def index():
    return "Welcome to payment"

@payment_bp.route('/payment/<payment_id>')
def get_payment_by_id():
    pass

@payment_bp.route('/search')
def search():
    pass

@payment_bp.route('/browse/provider')
def provider():
    pass

@payment_bp.route('/browse/cardtype')
def card_type():
    pass

@payment_bp.route('/browse/expdate')
def exp_date():
    pass



