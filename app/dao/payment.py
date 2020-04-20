from app.config.database_config import pg_config

class PaymentDAO:
    def __init__(self):
        '''
           #connection_url = "dbname=%s username=%s password=%s" % (pg_config['dbname'],
                                                                pg_config['username'],
                                                                pg_config['passwd'])
            #self.conn = psycopg2._connect(connection_url)
        '''
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
        result = self.cards
        return result

    def getCardById(self, cid):
        for card in self.cards:
            if card['pid'] == cid:
                return card
        return None

    def getCardByType(self, ctype):
        for card in self.cards:
            if card['pType'] == ctype:
                return card
        return None

    def getCardByProvider(self, provider):
        for card in self.cards:
            if card['pProvider'] == provider:
                return card
        return None

    def getCardByExpDate(self, expDate):
        for card in self.cards:
            if card['pExpDate'] == expDate:
                return card
        return None

    def getCardByUser(self, user):
        for card in self.cards:
            if card['uid'] == user:
                return card
        return None

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
        for card in self.cards:
            if card["pid"] == cid:
                return card['uid']
        return None

    def countCards(self):
        return len(self.cards)

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
