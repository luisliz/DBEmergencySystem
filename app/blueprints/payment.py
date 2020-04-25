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

@payment_bp.route('/cardByType/<string:ctype>', methods =['GET'])
def get_card_by_type(ctype):
    if request.method == 'GET':
        return PaymentHandler().getCardByType(ctype)

@payment_bp.route('/cardByProvider/<string:provider>', methods =['GET'])
def get_card_by_provider(provider):
    if request.method == 'GET':
        return PaymentHandler().getCardByProvider(provider)

@payment_bp.route('/cardByExpDate/<string:expDate>', methods =['GET'])
def get_card_by_expDate(expDate):
    if request.method == 'GET':
        return PaymentHandler().getCardByExpDate(expDate)

@payment_bp.route('/cardByUser/<int:user>', methods =['GET'])
def get_card_by_user(user):
    if request.method == 'GET':
        return PaymentHandler().getCardByUser(user)

@payment_bp.route('/count', methods=['GET'])
def count_payment():
    if request.method == 'GET':
        return PaymentHandler().countCards()

@payment_bp.route('/userByCardId/<int:cid>', methods =['GET'])
def get_user_by_card(cid):
    if request.method == 'GET':
        return PaymentHandler().getUserByCardId(cid)

"""////////////////////////////////DONT KNOW IF THESE METHODS ARE NECESSARY /////////////////////////////////////////"""
@payment_bp.route('/type/<int:tid>', methods =['GET'])
def get_card_type(tid):
    if request.method == 'GET':
        return PaymentHandler().getCardType(tid)

@payment_bp.route('/provider/<int:tid>', methods =['GET'])
def get_card_provider(tid):
    if request.method == 'GET':
        return PaymentHandler().getCardProvider(tid)

@payment_bp.route('/expdate/<int:tid>', methods =['GET'])
def get_card_exp_date(tid):
    if request.method == 'GET':
        return PaymentHandler().getCardExpDate(tid)

@payment_bp.route('/user/<int:tid>', methods =['GET'])
def get_card_user(tid):
    if request.method == 'GET':
        return PaymentHandler().getCardUser(tid)
"""////////////////////////////////DONT KNOW IF THESE METHODS ARE NECESSARY /END/////////////////////////////////////"""

"""///////////////////////////////////////////////PAST PHASE 2///////////////////////////////////////////////////////"""

@payment_bp.route('/add', methods =['POST'])
def add_card():
    if request.method == 'POST':
        return PaymentHandler().insertCard(request.form)

@payment_bp.route('/delete/<int:cID>', methods =['DELETE'])
def delete_card(cID):
    if request.method == 'DELETE':
        return PaymentHandler().deleteCard(cID)

@payment_bp.route('/update/<int:cID>', methods=['PUT'])
def settings(cID):
    if request.method == 'PUT':
        return PaymentHandler().updateCard(cID, request.form)
