from flask import jsonify
from app.dao.payment import PaymentDAO


class PaymentHandler:
    def build_payment_dict(self, row):
        result = {}
        if row == None:
            return {'error': 'User Not found'}
        else:
            result['pid'] = row[0]
            result['uid'] = row[1]
            result['pNumber'] = row[2]
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

    def getAllCards(self):
        dao = PaymentDAO()
        payment_list = dao.getAllCards()
        result_list = []
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Cards=result_list)

    def getCardById(self, cid):
        dao = PaymentDAO()
        row = dao.getCardById(cid)
        if not row:
            return jsonify(Error="Card Not Found"), 404
        else:
            card = self.build_payment_dict(row)
            return jsonify(Card=card)

    def getCardByType(self, ctype):
        dao = PaymentDAO()
        payment_list = dao.getCardByType(ctype)
        result_list = []
        if not payment_list:
            return jsonify(Error="Card Not Found"), 404
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Cards=result_list)


    def getCardByProvider(self, prov):
        dao = PaymentDAO()
        payment_list = dao.getCardByProvider(prov)
        result_list = []
        if not payment_list:
            return jsonify(Error="Card Not Found"), 404
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Cards=result_list)

    def getCardByExpDate(self, date):
        dao = PaymentDAO()
        payment_list = dao.getCardByExpDate(date)
        result_list = []
        if not payment_list:
            return jsonify(Error="Card Not Found"), 404
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Cards=result_list)

    def getCardByUser(self, uid):
        dao = PaymentDAO()
        payment_list = dao.getCardByUser(uid)
        result_list = []
        if not payment_list:
            return jsonify(Error="Card Not Found"), 404
        for row in payment_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Cards=result_list)

    def countCards(self):
        dao = PaymentDAO()
        cCount = dao.countCards()
        return jsonify(CardCount=cCount)

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

    """/////////////////////////////DONT KNOW IF THESE METHODS ARE NECESSARY ////////////////////////////////////////"""
    def getCardNumber(self, tid):
        return "Number: 1111 1111 1111 1111"

    def getCardType(self, tid):
        return "Type: Visa"

    def getCardProvider(self, tid):
        return "Provider: The bank"

    def getCardExpDate(self, tid):
        return "ExpDate: 02/12"

    def getCardUser(self, tid):
        return "User: Yeniel"

    def searchCard(self, args):
        type = args.get("Card_type")
        provider = args.get("Card_provider")
        expDate = args.get("Card_exp_date")
        user = args.get("Card_user")
        dao = PaymentDAO()
        card_list = []
        if (len(args) == 1) and type:
            card_list = dao.getCardByType(type)
        elif (len(args) == 1) and provider:
            card_list = dao.getCardByProvider(provider)
        elif (len(args) == 1) and expDate:
            card_list = dao.getCardByExpDate(expDate)
        elif (len(args) == 1) and user:
            card_list = dao.getCardByUser(user)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in card_list:
            result = self.build_payment_dict(row)
            result_list.append(result)
        return jsonify(Cards=result_list)
    """/////////////////////////////DONT KNOW IF THESE METHODS ARE NECESSARY /END////////////////////////////////////"""

    """/////////////////////////////////PAST PHASE 2/////////////////////////////////////////////////////////////////"""
    def insertCard(self, form):
        return "Added new Card"
        # print("form: ", form)
        # if len(form) != 5:
        #     return jsonify(Error="Malformed post request"), 400
        # else:
        #     cNumber = form['cNumber']
        #     cType = form['cType']
        #     cProvider = form['cProvider']
        #     cExpDate = form['cExpDate']
        #     cUser = form['cUser']
        #     if cNumber and cType and cProvider and cExpDate and cUser:
        #         dao = PaymentDAO()
        #         cid = dao.insert(cNumber, cType, cProvider, cExpDate, cUser)
        #         #result = self.build_payment_attributes(cid, cNumber, cType, cProvider, cExpDate, cUser)
        #         return jsonify(Card=cid)
        #     else:
        #         return jsonify(Error="Unexpected attributes in post request"), 400

    def insertCardJson(self, json):
        cNumber = json['cNumber']
        cType = json['cType']
        cProvider = json['cProvider']
        cExpDate = json['cExpDate']
        cUser = json['cUser']
        if cNumber and cType and cProvider and cExpDate and cUser:
            dao = PaymentDAO()
            cid = dao.insert(cNumber, cType, cProvider, cExpDate, cUser)
            #result = result = self.build_payment_attributes(cid, cNumber, cType, cProvider, cExpDate, cUser)
            return jsonify(Card=cid), 201
        else:
            return jsonify(Error="Unexpected attributes in post request"), 400

    def deleteCard(self, cid):
        dao = PaymentDAO()
        return f"Deleted card with id: {cid}"
        # if not dao.getCardById(cid):
        #     return jsonify(Error="Card not found."), 404
        # else:
        #     dao.delete(cid)
        #     #return jsonify(DeleteStatus="OK", deleted=cid), 200
        #     return jsonify(deleted=cid)

    def updateCard(self, cid, form):
        dao = PaymentDAO()
        return f"Updated payment with id: {cid}"
        # if not dao.getCardById(cid):
        #     return jsonify(Error="Card not found."), 404
        # else:
        #     print("form: ", form)
        #     if len(form) != 5:
        #         return jsonify(Error="Malformed post request"), 400
        #     else:
        #         cNumber = form['cNumber']
        #         cType = form['cType']
        #         cProvider = form['cProvider']
        #         cExpDate = form['cExpDate']
        #         cUser = form['cUser']
        #         if cNumber and cType and cProvider and cExpDate and cUser:
        #             dao = PaymentDAO()
        #             cid = dao.insert(cNumber, cType, cProvider, cExpDate, cUser)
        #             #result = self.build_payment_attributes(cid, cNumber, cType, cProvider, cExpDate, cUser)
        #             return jsonify(Card=cid), 201
        #         else:
        #             return jsonify(Error="Unexpected attributes in post request"), 400
