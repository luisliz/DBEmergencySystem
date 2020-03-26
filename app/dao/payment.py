from app.config.database_config import pg_config

class PaymentDAO:
    def __init__(self):
        '''
           #connection_url = "dbname=%s card=%s password=%s" % (pg_config['dbname'],
                                                                pg_config['card'],
                                                                pg_config['passwd'])
            #self.conn = psycopg2._connect(connection_url)
        '''
        self.cards = {
            1: {
                'Card_id': 1,
                'Card_number': '1111111111111111',
                'Card_type': 'Visa',
                'Card_provider': "The bank",
                'Card_exp_date': '02/12',
                'Card_user': 'Yeniel'
            }
        }

    def getAllCards(self):
        result = self.cards
        return result

    def getCardById(self, cid):
        for i, card in self.cards:
            if i == cid:
                return card
        return None

    def getCardByType(self, type):
        for i, card in self.cards:
            if card['Card_type'] == type:
                return card
        return None

    def getCardByProvider(self, provider):
        for i, card in self.cards:
            if card['Card_provider'] == provider:
                return card
        return None

    def getCardByEXPDate(self, expDate):
        for i, card in self.cards:
            if card['Card_exp_date'] == expDate:
                return card
        return None

    def getCardByTypeAndProvider(self, type, provider):
        for i, card in self.cards:
            if card['Card_type'] == type and card['Card_provider'] == provider:
                return card
        return None

    def getUserByCardID(self, cid):
        return cid

    def insert(self, cid, cNumber, cType, cProvider, cExpDate, cUser):
        return cid

    def delete(self, cid):
        return cid

    def update(self, cid, cNumber, cType, cProvider, cExpDate, cUser):
        return cid
