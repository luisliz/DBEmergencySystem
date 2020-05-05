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
        """
        else:
            return TransactionHandler().searchTransaction(request.args)
        """

@transaction_bp.route('/getById/<int:tid>', methods =['GET', 'DELETE'])
def get_Transaction_by_id(tid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionById(tid)
    elif request.method == 'DELETE':
        return TransactionHandler().deleteTransaction(tid)

@transaction_bp.route('/reservations', methods =['GET'])
def get_all_reservations():
    if request.method == 'GET':
        return TransactionHandler().getAllReservations()

@transaction_bp.route('/reservations/<int:tid>', methods =['GET'])
def get_reservation_by_id(tid):
    if request.method == 'GET':
        return TransactionHandler().getReservationById(tid)

@transaction_bp.route('/purchases/<int:tid>', methods =['GET'])
def get_purchase_by_id(tid):
    if request.method == 'GET':
        return TransactionHandler().getPurchaseById(tid)

@transaction_bp.route('/purchases', methods =['GET'])
def get_all_purchases():
    if request.method == 'GET':
        return TransactionHandler().getAllPurchases()



@transaction_bp.route('/getByDate/<string:date>', methods =['GET'])
def get_Transaction_by_date(date):
    if request.method == 'GET':
        return TransactionHandler().getTransactionByDate(date)

@transaction_bp.route('/getByQty/<int:quantity>', methods =['GET'])
def get_Transaction_by_quantity(quantity):
    if request.method == 'GET':
        return TransactionHandler().getTransactionByQuantity(quantity)

#Needs testing
@transaction_bp.route('/getByPayerPaymentID/<int:payer_pid>', methods =['GET'])
def get_Transaction_by_payer_payment(payer_pid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionByPayerPaymentINfo(payer_pid)

#Needs testing
@transaction_bp.route('/getBySupPaymentID/<int:supplier_pid>', methods =['GET'])
def get_Transaction_by_supplier_payment(supplier_pid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionBySupplierPaymentInfo(supplier_pid)

#Needs testing
@transaction_bp.route('/getByReqID/<int:payer_id>', methods =['GET'])
def get_Transaction_by_payer(payer_id):
    if request.method == 'GET':
        return TransactionHandler().getTransactionByPayer(payer_id)

#Needs testing
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

#Needs testing
@transaction_bp.route('/payerPaymentByTransId/<int:tid>', methods =['GET'])
def get_payer_payment_by_transaction(tid):
    if request.method == 'GET':
        return TransactionHandler().getPayerPaymentInfoByTransactionId(tid)

#Needs testing
@transaction_bp.route('/supplierPaymentByTransId/<int:tid>', methods =['GET'])
def get_supplier_payment_by_transaction(tid):
    if request.method == 'GET':
        return TransactionHandler().getSupplierPaymentInfoByTransactionId(tid)

#Needs testing
@transaction_bp.route('/payerByTransId/<int:tid>', methods =['GET'])
def get_payer_by_transaction(tid):
    if request.method == 'GET':
        return TransactionHandler().getPayerByTransactionId(tid)

#Needs testing
@transaction_bp.route('/supplierByTransId/<int:tid>', methods =['GET'])
def get_supplier_by_transaction(tid):
    if request.method == 'GET':
        return TransactionHandler().getSupplierByTransactionId(tid)

@transaction_bp.route('/resByTransId/<int:tid>', methods =['GET'])
def get_resource_by_transaction(tid):
    if request.method == 'GET':
        return TransactionHandler().getResourceByTransactionId(tid)

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
