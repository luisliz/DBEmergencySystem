import psycopg2

from app.config.database_config import pg_config

class PaymentDAO:
    def __init__(self):
        self.conn = psycopg2.connect(host="localhost",database="disasterAid", user="appusr", password="class")

        self.cards = [
            {
                'pid': 1,
                'uid': 1,
                'pNumber': '1111111111111111',
                'pType': 'Visa',
                'pProvider': "The bank",
                'pExpDate': "02/12",
            }
        ]

    def getAllCards(self):
        cursor = self.conn.cursor()
        query = "select * from payments;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
        #result = self.cards

    def getCardById(self, cid):
        """
            for card in self.cards:
                if card['pid'] == cid:
                    return card
            return None
        """
        cursor = self.conn.cursor()
        query = f'select * from payments where pid = {cid};'
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getCardByType(self, ctype):
        """
        for card in self.cards:
            if card['pType'] == ctype:
                return card
        return None
        """
        cursor = self.conn.cursor()
        query = f"select * from payments where ptype = '{ctype}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByProvider(self, provider):
        """
        for card in self.cards:
            if card['pProvider'] == provider:
                return card
        return None
        """
        cursor = self.conn.cursor()
        query = f"select * from payments where pprovider = '{provider}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByExpDate(self, expDate):
        #IF IT STAYS AS A TIMESTAMP ITS GONNA BE A PAIN IN THE ASS TO TEST
        """
        for card in self.cards:
            if card['pExpDate'] == expDate:
                return card
        return None
        """
        cursor = self.conn.cursor()
        query = f"select * from payments where pexpdate = '{expDate}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByUser(self, uid):
        """
        for card in self.cards:
            if card['uid'] == user:
                return card
        return None
        """
        cursor = self.conn.cursor()
        query = f"select * from payments where uid = '{uid}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Are these necessary?
    def getCardByTypeAndProvider(self, ctype, provider):
        for card in self.cards:
            if card['pType'] == ctype and card['pProvider'] == provider:
                return card
        return None

    def getCardByTypeAndExpDate(self, ctype, expDate):
        for card in self.cards:
            if card['pType'] == ctype and card['pExpDate'] == expDate:
                return card
        return None

    def getCardByTypeAndExpDate(self, ctype, user):
        for card in self.cards:
            if card['pType'] == ctype and card['uid'] == user:
                return card
        return None

    def getCardByProviderAndExpDate(self, provider, expDate):
        for card in self.cards:
            if card['pProvider'] == provider and\
                    card['pExpDate'] == expDate:
                return card
        return None

    def getCardByProviderAndUser(self, provider, user):
        for card in self.cards:
            if card['pProvider'] == provider and\
                    card['uid'] == user:
                return card
        return None

    def getCardByExpDateAndUser(self, expDate, user):
        for card in self.cards:
            if card['pExpDate'] == expDate and\
                    card['uid'] == user:
                return card
        return None

    def getUserByCardId(self, cid):
        """
        for card in self.cards:
            if card["pid"] == cid:
                return card['uid']
        return None
        """
        cursor = self.conn.cursor()
        query = f"select uid, ucid, ufirstname, ulastname, udob, uemail, upassword from payments natural inner join users where pid = '{cid}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def countCards(self):
        """return len(self.cards)"""
        cursor = self.conn.cursor()
        query = f"select count(*) from payments;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    """//////////////////////////////////////FOR FUTURE PHASE///////////////////////////////////////////////////////"""
    def insert(self, cid, cNumber, cType, cProvider, cExpDate, cUser):
        newCID = len(self.cards) + 1
        newCard = {
            'pid': len(self.cards) + 1,
            'Card_number': cNumber,
            'pType': cType,
            'pProvider': cProvider,
            'pExpDate': cExpDate,
            'uid': cUser
        }
        self.cards.append(newCard)
        return newCID

    def delete(self, cid):
        pos = 0
        for card in self.cards:
            if int(card['pid']) == int(cid):
                del self.cards[pos]
                return True
            pos += 1

        return False

    def update(self, cid, cNumber, cType, cProvider, cExpDate, cUser):
        for card in self.cards:
            if card['pid'] == cid:
                card = {
                    'pid': cid,
                    'Card_number': cNumber,
                    'pType': cType,
                    'pProvider': cProvider,
                    'pExpDate': cExpDate,
                    'uid': cUser
                }
                return True
        return False
