from flask import jsonify

from app.dao.payment import PaymentDAO
from app.dao.resources import ResourcesDAO
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
            result['tpayerpid'] = row[3]
            result['tsupplierpid'] = row[4]
            result['rid'] = row[5]
            result['tamount'] = row[6]
            return row

    def build_payment_dict(self, row):
        result = {}
        if row == None:
            return {'error': 'User Not found'}
        else:
            result['pid'] = row[0]
            result['pType'] = row[3]
            result['pProvider'] = row[4]
            result['pExpDate'] = row[5]
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
        transaction_list = dao.getTransactionById(tid)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    def getAllReservations(self):
        dao = TransactionDAO()
        transaction_list = dao.getAllReservations()
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Reservations=result_list)

    def getReservationById(self, tid):
        dao = TransactionDAO()
        transaction_list = dao.getReservationById(tid)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)

    def getAllPurchases(self):
        dao = TransactionDAO()
        transaction_list = dao.getAllPurchases()
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Purchases=result_list)

    def getPurchaseById(self, tid):
        dao = TransactionDAO()
        transaction_list = dao.getPurchaseById(tid)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Purchase=result_list)

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

    #Need testing
    def getTransactionByPayerPaymentInfo(self, ppid):
        dao = TransactionDAO()
        transaction_list = dao.getTransactionByPayerPaymentInfo(ppid)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    #Need testing
    def getTransactionByPayer(self, spid):
        dao = TransactionDAO()
        transaction_list = dao.getTransactionBySupplierPaymentInfo(spid)
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    #Need testing
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

    #Need testing
    def getPayerByTransactionId(self, tid):
        dao = TransactionDAO()
        if not dao.getTransactionById(tid):
            return jsonify(Error="Transaction Not Found"), 404
        users_list = dao.getPayerByTransactionId(tid)
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    #Need testing
    def getSupplierById(self, tid):
        dao = TransactionDAO()
        if not dao.getTransactionById(tid):
            return jsonify(Error="Transaction Not Found"), 404
        users_list = dao.getSupplierByTransactionId(tid)
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    #Need testing
    def getPayerPaymentInfoById(self, tid):
        dao = TransactionDAO()
        if not dao.getTransactionById(tid):
            return jsonify(Error="Transaction Not Found"), 404
        payments_list = dao.getPayerPaymentInfoByTransactionId(tid)
        result_list = []
        for row in payments_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    #Need testing
    def getSupplierPaymentInfoByTransactionId(self, tid):
        dao = TransactionDAO()
        if not dao.getTransactionById(tid):
            return jsonify(Error="Transaction Not Found"), 404
        payments_list = dao.getSupplierPaymentInfoByTransactionId(tid)
        result_list = []
        for row in payments_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getResourceByTransactionId(self, tid):
        dao = TransactionDAO()
        if not dao.getTransactionById(tid):
            return jsonify(Error="Transaction Not Found"), 404
        resource_list = dao.getResourceByTransactionId(tid)
        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    """////////////////////////////////////////PHASE 3//////////////////////////////////////////////////////////"""
    def insertTransaction(self, form, rid):
        tdate = form['tdate']
        tquantity = form['tquantity']
        tpayerpid = form['tpayerpid']
        tsupplierpid = form['tsupplierpid']
        #rid = form['rid'] MADE A CHANGE SO THAT WE TAKE RID FROM THE PURCHASE RESOURCE ROUTE
        tamount = form['tamount']

        """
        resourceDao = ResourcesDAO()
        if 'rid' in form:
            try:
                if resourceDao.getResourceById(int(rid)) is None:
                    return jsonify(error='rid does not exist')
            except ValueError:
                return jsonify(error='rid must be an int')
        """

        dao = TransactionDAO()
        #THIS IS MY ATTEMPT TO MAKE RESERVATIONS NOT NEED ANY PAYMENT INFO
        #BUT WE WOULD NEED TO CHANGE THE SCHEMA
        """
        if tamount == 0:
            result = dao.insertReservation(tdate, tquantity, rid, tamount)
        """

        paymentDao = PaymentDAO()

        if 'tpayerpid' in form:
            try:
                if paymentDao.getCardById(tpayerpid) is None:
                    return jsonify(error='tpayerpid ' + tpayerpid + ' does not exist')
            except:
                return jsonify(error='tpayerid must be an int')
        if 'tsupplierpid' in form:
            try:

                if not paymentDao.checkPaymentIsFromSupplier(int(tsupplierpid)):
                    return jsonify(error='tsupplierpid ' + tsupplierpid + ' does not exist or is not a supplier')
            except ValueError:
                return jsonify(error='supplierid must be an int')

        result = dao.insertPurchase(tdate, tquantity, tpayerpid, tsupplierpid, rid, tamount)
        return jsonify(Reqid=result)
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
