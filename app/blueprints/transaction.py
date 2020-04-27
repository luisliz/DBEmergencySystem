from flask import Blueprint, url_for, flash, request
from app.handlers.transaction import TransactionHandler

transaction_bp = Blueprint('transaction', __name__)

@transaction_bp.route('/', methods=['GET', 'POST'])
def transaction_info():
    if request.method == 'POST':
        return TransactionHandler().insertTransaction(request.form)
    else:
        if not request.args:
            return TransactionHandler().getAllTransactions()
        else:
            return TransactionHandler().searchTransaction(request.args)

@transaction_bp.route('/getById/<int:tid>', methods =['GET', 'DELETE'])
def get_Transaction_by_id(tid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionById(tid)
    elif request.method == 'DELETE':
        return TransactionHandler().deleteTransaction(tid)

@transaction_bp.route('/getByDate/<string:date>', methods =['GET'])
def get_Transaction_by_date(date):
    if request.method == 'GET':
        return TransactionHandler().getTransactionByDate(date)

@transaction_bp.route('/getByQty/<int:quantity>', methods =['GET'])
def get_Transaction_by_quantity(quantity):
    if request.method == 'GET':
        return TransactionHandler().getTransactionByQuantity(quantity)

@transaction_bp.route('/getByReqID/<int:payer_id>', methods =['GET'])
def get_Transaction_by_payer(payer_id):
    if request.method == 'GET':
        return TransactionHandler().getTransactionByPayer(payer_id)

@transaction_bp.route('/getBySupID/<int:supplier_id>', methods =['GET'])
def get_Transaction_by_supplier(supplier_id):
    if request.method == 'GET':
        return TransactionHandler().getTransactionBySupplier(supplier_id)

@transaction_bp.route('/getByResID/<int:rid>', methods =['GET'])
def get_Transaction_by_resource(rid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionByResource(rid)

@transaction_bp.route('/getByAmount/<int:amount>', methods =['GET'])
def get_Transaction_by_amount(amount):
    if request.method == 'GET':
        return TransactionHandler().getTransactionByAmount(amount)


@transaction_bp.route('/count', methods=['GET'])
def count_Transaction():
    if request.method == 'GET':
        return TransactionHandler().countTransactions()

@transaction_bp.route('/resByTransId/<int:tid>', methods =['GET'])
def get_resource_by_transaction(tid):
    if request.method == 'GET':
        return TransactionHandler().getResourceByTransactionId(tid)

"""/////////////////////////////////////////DONT KNOW IF I NEED//////////////////////////////////////////////////////"""

@transaction_bp.route('/date/<int:tid>', methods =['GET'])
def get_Transaction_date(tid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionDate(tid)

@transaction_bp.route('/quantity/<int:tid>', methods =['GET'])
def get_Transaction_quantity(tid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionQuantity(tid)

@transaction_bp.route('/requester/<int:tid>', methods =['GET'])
def get_Transaction_requester(tid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionPayer(tid)

@transaction_bp.route('/supplier/<int:tid>', methods =['GET'])
def get_Transaction_supplier(tid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionSupplier(tid)

@transaction_bp.route('/resource/<int:tid>', methods =['GET'])
def get_Transaction_resource(tid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionResource(tid)

@transaction_bp.route('/amount/<int:tid>', methods =['GET'])
def get_Transaction_amount(tid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionAmount(tid)


"""///////////////////////////////////////////////DONT KNOW IF I NEED /END///////////////////////////////////////////"""

"""////////////////////////////////////////////////PAST PHASE 2//////////////////////////////////////////////////////"""

@transaction_bp.route('/add', methods =['POST'])
def add_transaction():
    if request.method == 'POST':
        return TransactionHandler().insertTransaction(request.form)

@transaction_bp.route('/delete/<int:tid>', methods =['DELETE'])
def delete_transaction(tid):
    if request.method == 'DELETE':
        return TransactionHandler().deleteTransaction(tid)

@transaction_bp.route('/update/<int:tid>', methods=['PUT'])
def settings(tid):
    if request.method == 'PUT':
        return TransactionHandler().updateTransaction(tid, request.form)
