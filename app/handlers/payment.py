from flask import jsonify
from app.dao.payment import PaymentDAO


class PaymentHandler:
    def build_payment_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['cNumber'] = row[1]
        result['cType'] = row[2]
        result['cProvider'] = row[3]
        result['cExpDate'] = row[4]
        result['uID'] = row[5]
        return result

    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['ufname'] = row[1]
        result['ulname'] = row[2]
        result['udateOfBirth'] = row[3]
        result['uemail'] = row[4]
        result['upassword'] = row[5]
        return result

    def build_payment_attributes(self, cid, cNumber, cType, cProvider, cExpDate, uID):
        result = {}
        result['cid'] = cid
        result['cNumber'] = cNumber
        result['cType'] = cType
        result['cProvider'] = cProvider
        result['cExpDate'] = cExpDate
        result['uID'] = uID
        return result

    def getAllPayments(self):
        dao = PaymentDAO()
        payment_list = dao.getAllCards()
        result_list = []
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Cards=result_list)

    def getPaymentById(self, cid):
        dao = PaymentDAO()
        row = dao.getCardById(cid)
        if not row:
            return jsonify(Error="Card Not Found"), 404
        else:
            card = self.build_payment_dict(row)
            return jsonify(Card=card)

    def searchParts(self, args):
        type = args.get("cType")
        provider = args.get("cProvider")
        dao = PaymentDAO()
        card_list = []
        if (len(args) == 2) and type and provider:
            card_list = dao.getCardByTypeAndProvider(type, provider)
        elif (len(args) == 1) and type:
            card_list = dao.getCardByType(type)
        elif (len(args) == 1) and provider:
            card_list = dao.getPartsByProvider(provider)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in card_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Cards=result_list)

    def getUserByCardId(self, cid):
        dao = PaymentDAO()
        if not dao.getCardById(cid):
            return jsonify(Error="Part Not Found"), 404
        users_list = dao.getUserByCardId(cid)
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def insertCard(self, form):
        print("form: ", form)
        if len(form) != 4:
            return jsonify(Error="Malformed post request"), 400
        else:
            cNumber = form['cNumber']
            cType = form['cType']
            cProvider = form['cProvider']
            cExpDate = form['cExpDate']
            cUser = form['cUser']
            if cNumber and cType and cProvider and cExpDate and cUser:
                dao = PaymentDAO()
                cid = dao.insert(cNumber, cType, cProvider, cExpDate, cUser)
                result = self.build_payment_attributes(cid, cNumber, cType, cProvider, cExpDate, cUser)
                return jsonify(Card=result), 201
            else:
                return jsonify(Error="Unexpected attributes in post request"), 400

    def insertCardJson(self, json):
        cNumber = json['cNumber']
        cType = json['cType']
        cProvider = json['cProvider']
        cExpDate = json['cExpDate']
        cUser = json['cUser']
        if cNumber and cType and cProvider and cExpDate and cUser:
            dao = PaymentDAO()
            cid = dao.insert(cNumber, cType, cProvider, cExpDate, cUser)
            result = result = self.build_payment_attributes(cid, cNumber, cType, cProvider, cExpDate, cUser)
            return jsonify(Card=result), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deletePart(self, cid):
        dao = PaymentDAO()
        if not dao.getCardById(cid):
            return jsonify(Error="Card not found."), 404
        else:
            dao.delete(cid)
            return jsonify(DeleteStatus="OK"), 200

    def updatePart(self, cid, form):
        dao = PaymentDAO()
        if not dao.getCardById(cid):
            return jsonify(Error="Card not found."), 404
        else:
            print("form: ", form)
            if len(form) != 4:
                return jsonify(Error="Malformed post request"), 400
            else:
                cNumber = form['cNumber']
                cType = form['cType']
                cProvider = form['cProvider']
                cExpDate = form['cExpDate']
                cUser = form['cUser']
                if cNumber and cType and cProvider and cExpDate and cUser:
                    dao = PaymentDAO()
                    cid = dao.insert(cNumber, cType, cProvider, cExpDate, cUser)
                    result = self.build_payment_attributes(cid, cNumber, cType, cProvider, cExpDate, cUser)
                    return jsonify(Card=result), 201
                else:
                    return jsonify(Error="Unexpected attributes in post request"), 400

    def build_payment_counts(self, payment_counts):
        result = []
        # print(payment_counts)
        for P in payment_counts:
            D = {}
            D['type'] = P[0]
            D['provider'] = P[1]
            D['count'] = P[2]
            result.append(D)
        return result