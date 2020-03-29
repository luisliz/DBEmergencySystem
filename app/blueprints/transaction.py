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

@transaction_bp.route('/<int:tid>', methods =['GET', 'DELETE'])
def get_Transaction_by_id(tid):
    if request.method == 'GET':
        return TransactionHandler().getTransactionById(tid)
    elif request.method == 'DELETE':
        return TransactionHandler().deleteTransaction(tid)

@transaction_bp.route('/add', methods =['POST'])
def add_transaction():
    return "Added new transaction"
    # if request.method == 'POST':
    #     return TransactionHandler().insertTransaction(request.form)

@transaction_bp.route('/<int:tid>', methods =['DELETE'])
def delete_transaction(tid):
    return f"Deleted transaction with id: {tid}"
    # if request.method == 'PUT':
    #     return TransactionHandler().deleteTransaction(tid)

@transaction_bp.route('/update/<int:tid>', methods=['PUT'])
def settings(tid):
    return f"Updated transaction with id: {tid}"
    # if request.method == 'PUT':
    #     return TransactionHandler().updateTransaction(tid, request.form)

@transaction_bp.route('/count', methods=['GET'])
def count_Transaction():
    if request.method == 'GET':
        return TransactionHandler().countTransactions()
