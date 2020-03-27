from app.config.database_config import pg_config

class PaymentDAO:
    def __init__(self):
        '''
           #connection_url = "dbname=%s card=%s password=%s" % (pg_config['dbname'],
                                                                pg_config['card'],
                                                                pg_config['passwd'])
            #self.conn = psycopg2._connect(connection_url)
        '''
        self.cards = [
            {
                'Card_id': 1,
                'Card_number': '1111111111111111',
                'Card_type': 'Visa',
                'Card_provider': "The bank",
                'Card_exp_date': '02/12',
                'Card_user': 'Yeniel'
            }
        ]

    def getAllCards(self):
        result = self.cards
        return result

    def getCardById(self, cid):
        for card in self.cards:
            if card['Card_id'] == cid:
                return card
        return None

    def getCardByType(self, ctype):
        for card in self.cards:
            if card['Card_type'] == ctype:
                return card
        return None

    def getCardByProvider(self, provider):
        for card in self.cards:
            if card['Card_provider'] == provider:
                return card
        return None

    def getCardByExpDate(self, expDate):
        for card in self.cards:
            if card['Card_exp_date'] == expDate:
                return card
        return None

    def getCardByUser(self, user):
        for card in self.cards:
            if card['Card_user'] == user:
                return card
        return None

    def getCardByTypeAndProvider(self, ctype, provider):
        for card in self.cards:
            if card['Card_type'] == ctype and card['Card_provider'] == provider:
                return card
        return None

    def getCardByTypeAndExpDate(self, ctype, expDate):
        for card in self.cards:
            if card['Card_type'] == ctype and card['Card_exp_date'] == expDate:
                return card
        return None

    def getCardByTypeAndExpDate(self, ctype, user):
        for card in self.cards:
            if card['Card_type'] == ctype and card['Card_user'] == user:
                return card
        return None

    def getCardByProviderAndExpDate(self, provider, expDate):
        for card in self.cards:
            if card['Card_provider'] == provider and\
                    card['Card_exp_date'] == expDate:
                return card
        return None

    def getCardByProviderAndUser(self, provider, user):
        for card in self.cards:
            if card['Card_provider'] == provider and\
                    card['Card_user'] == user:
                return card
        return None

    def getCardByExpDateAndUser(self, expDate, user):
        for card in self.cards:
            if card['Card_exp_date'] == expDate and\
                    card['Card_user'] == user:
                return card
        return None

    def getUserByCardId(self, cid):
        for card in self.cards:
            if card["Card_id"] == cid:
                return card['Card_user']
        return None

    def countCards(self):
        return len(self.cards)

    def insert(self, cid, cNumber, cType, cProvider, cExpDate, cUser):
        newCID = len(self.cards) + 1
        newCard = {
            'Card_id': len(self.cards) + 1,
            'Card_number': cNumber,
            'Card_type': cType,
            'Card_provider': cProvider,
            'Card_exp_date': cExpDate,
            'Card_user': cUser
        }
        self.cards.append(newCard)
        return newCID

    def delete(self, cid):
        pos = 0
        for card in self.cards:
            if int(card['Card_id']) == int(cid):
                del self.cards[pos]
                return True
            pos += 1

        return False

    def update(self, cid, cNumber, cType, cProvider, cExpDate, cUser):
        for card in self.cards:
            if card['Card_id'] == cid:
                card = {
                    'Card_id': cid,
                    'Card_number': cNumber,
                    'Card_type': cType,
                    'Card_provider': cProvider,
                    'Card_exp_date': cExpDate,
                    'Card_user': cUser
                }
                return True
        return False
