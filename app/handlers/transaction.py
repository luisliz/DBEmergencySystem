from flask import jsonify
from app.dao.transaction import TransactionDAO


class TransactionHandler:
    def build_transaction_dict(self, row):
        return row

    def getAllTransactions(self):
        dao = TransactionDAO()
        transaction_list = dao.getAllTransactions()
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def getTransactionById(self, tid):
        dao = TransactionDAO()
        row = dao.getTransactionById(tid)
        if not row:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            t = self.build_transaction_dict(row)
            return jsonify(Transaction=t)

    def searchTransaction(self, args):
        date = args.get("tdate")
        quantity = args.get("tquantity")
        payer = args.get("tpayer")
        supplier = args.get("tsupplier")
        resource = args.get("tresource")
        ammount = args.get("tpayAmmount")
        dao = TransactionDAO()
        transaction_list = []
        if (len(args) == 1) and date:
            transaction_list = dao.getTransactionByDate(date)
        elif (len(args) == 1) and quantity:
            transaction_list = dao.getTransactionByQuantity(quantity)
        elif (len(args) == 1) and payer:
            transaction_list = dao.getTransactionByPayer(payer)
        elif (len(args) == 1) and supplier:
            transaction_list = dao.getTransactionBySupplier(supplier)
        elif (len(args) == 1) and resource:
            transaction_list = dao.getTransactionByResource(resource)
        elif (len(args) == 1) and ammount:
            transaction_list = dao.getTransactionByAmmount(ammount)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    """
        def getPayerByTransactionId(self, tid):
            dao = TransactionDAO()
            if not dao.getTransactionById(tid):
                return jsonify(Error="Part Not Found"), 404
            users_list = dao.getPayerBytId(tid)
            result_list = []
            for row in users_list:
                result = self.build_user_dict(row)
                result_list.append(result)
            return jsonify(Users=result_list)
    """
    def insertTransaction(self, form):
        return "Added new transaction"
        # print("form: ", form)
        # if len(form) != 6:
        #     return jsonify(Error="Malformed post request"), 400
        # else:
        #     tDate = form['tdate']
        #     tQuantity = form['tquantity']
        #     tPayer = form['tpayer']
        #     tSupplier = form['tsupplier']
        #     tResource = form['tresource']
        #     tAmmount = form['tpayAmmount']
        #     if tDate and tQuantity and tPayer and tSupplier and tResource and tAmmount:
        #         dao = TransactionDAO()
        #         tid = dao.insert( tDate, tQuantity, tPayer, tSupplier. tResourc, tAmmount)
        #         #result = self.build_Transaction_attributes(tid, cNumber, cType, cProvider, cExpDate, cUser)
        #         return jsonify(Transaction=tid)
        #     else:
        #         return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteTransaction(self, tid):
        dao = TransactionDAO()
        return f"Deleted transaction with id: {tid}"
        # if not dao.getTransactionById(tid):
        #     return jsonify(Error="Card not found."), 404
        # else:
        #     dao.delete(tid)
        #     #return jsonify(DeleteStatus="OK", deleted=tid), 200
        #     return jsonify(deleted=tid)

    def countTransactions(self):
        dao = TransactionDAO()
        tCount = dao.countTransactions()
        return jsonify(TransactionCount=tCount)

    def updateTransaction(self, tid, form):
        dao = TransactionDAO()
        return f"Updated transaction with id: {tid}"
        # if not dao.getTransactionById(tid):
        #     return jsonify(Error="Transaction not found."), 404
        # else:
        #     tDate = form['tdate']
        #     tQuantity = form['tquantity']
        #     tPayer = form['tpayer']
        #     tSupplier = form['tsupplier']
        #     tResource = form['tresource']
        #     tAmmount = form['tpayAmmount']
        #     if tDate and tQuantity and tPayer and tSupplier and tResource and tAmmount:
        #         dao = TransactionDAO()
        #         tid = dao.insert(tDate, tQuantity, tPayer, tSupplier.tResourc, tAmmount)
        #         return jsonify(Transaction=tid)
        #     else:
        #         return jsonify(Error="Unexpected attributes in post request"), 400