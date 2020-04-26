from flask import jsonify
from app.dao.transaction import TransactionDAO


class TransactionHandler:
    def build_transaction_dict(self, row):
        result = {}
        if row == None:
            return {'error': 'User Not found'}
        else:
            result['tid'] = row[0]
            result['tdate'] = row[1]
            result['tquantity'] = row[2]
            result['uid'] = row[3]
            result['supplieruid'] = row[4]
            result['rid'] = row[5]
            result['tamount'] = row[6]
            return row

    def build_user_dict(self, row):
        result = {}
        if row == None:
            return {'error': 'User Not found'}
        else:
            result['uid'] = row[0]
            result['ucid'] = row[1]
            result['ufirstName'] = row[2]
            result['ulastName'] = row[3]
            result['udob'] = row[4]
            result['uemail'] = row[5]
            return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rName'] = row[1]
        result['rcid'] = row[2]
        return result

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

    def getTransactionByDate(self, date):
        dao = TransactionDAO()
        transaction_list = dao.getTransactionByDate(date)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def getTransactionByQuantity(self, qty):
        dao = TransactionDAO()
        transaction_list = dao.getTransactionByQuantity(qty)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def getTransactionByPayer(self, uidp):
        dao = TransactionDAO()
        transaction_list = dao.getTransactionByPayer(uidp)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def getTransactionBySupplier(self, uids):
        dao = TransactionDAO()
        transaction_list = dao.getTransactionBySupplier(uids)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def getTransactionByResource(self, rid):
        dao = TransactionDAO()
        transaction_list = dao.getTransactionByResource(rid)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def getTransactionByAmount(self, amount):
        dao = TransactionDAO()
        transaction_list = dao.getTransactionByAmmount(amount)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def countTransactions(self):
        dao = TransactionDAO()
        tCount = dao.countTransactions()
        return jsonify(TransactionCount=tCount)

    def getResourceByTransactionId(self, tid):
        dao = TransactionDAO()
        if not dao.getTransactionById(tid):
            return jsonify(Error="Transaction Not Found"), 404
        users_list = dao.gerResourceByTransaction(tid)
        result_list = []
        for row in users_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    """/////////////////////////////////////////////DONT KNOW IF I NEED//////////////////////////////////////////////"""

    def getTransactionDate(self, tid):
        return "Date: 02/02/2020"

    def getTransactionQuantity(self, tid):
        return "Quantity: 10"

    def getTransactionPayer(self, tid):
        return "Requester: Yeniel"

    def getTransactionSupplier(self, tid):
        return "Supplier: Jorge"

    def getTransactionResource(self, tid):
        return "Resource: Water"

    def getTransactionAmount(self, tid):
        return "Amount: 50.0"

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

    """//////////////////////////////////////////DONT KNOW IF I NEED /END////////////////////////////////////////////"""

    """////////////////////////////////////////PAST PHASE 2//////////////////////////////////////////////////////////"""
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