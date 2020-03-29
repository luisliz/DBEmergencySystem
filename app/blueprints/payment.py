from flask import Blueprint, url_for, flash, request
from app.handlers.payment import PaymentHandler

payment_bp = Blueprint('payment', __name__)

@payment_bp.route('/', methods=['GET', 'POST'])
def payment_info():
    if request.method == 'POST':
        return PaymentHandler().insertCard(request.form)
    else:
        if not request.args:
            return PaymentHandler().getAllCards()
        else:
            return PaymentHandler().searchCard(request.args)

@payment_bp.route('/<int:cID>', methods =['GET', 'DELETE'])
def get_card_by_id(cID):
    if request.method == 'GET':
        return PaymentHandler().getCardById(cID)
    elif request.method == 'DELETE':
        return PaymentHandler().deleteCard(cID)

@payment_bp.route('/add', methods =['POST'])
def add_card():
    return "Added new Card"
    # if request.method == 'POST':
    #     return PaymentHandler().insertCard(request.form)

@payment_bp.route('/<int:cID>', methods =['DELETE'])
def delete_card(cID):
    return f"Deleted card with id: {cID}"
    # if request.method == 'DELETE':
    #     return PaymentHandler().deleteCard(cID)

@payment_bp.route('/update/<int: cID>', methods=['PUT'])
def settings(cID):
    return f"Updated transaction with id: {cID}"
    # if request.method == 'PUT':
    #     return PaymentHandler().updateCard(cID, request.form)

@payment_bp.route('/count', methods=['GET'])
def count_payment():
    if request.method == 'GET':
        return PaymentHandler().countCards()
