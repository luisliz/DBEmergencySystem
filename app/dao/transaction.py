from app.config.database_config import pg_config

class TransactionDAO:
    def __init__(self):
        '''
           #connection_url = "dbname=%s t=%s password=%s" % (pg_config['dbname'],
                                                                pg_config['t'],
                                                                pg_config['passwd'])
            #self.conn = psycopg2._connect(connection_url)
        '''
        self.transactions = [
            {
                'tid': 1,
                'tdate': '02/02/2020',
                'tQuantity': '10',
                'tpayer': 'Yeniel',
                'tsupplier': "Jorge",
                'tresource': 'Water',
                'tpayAmount': 50.0
            }
        ]

    def getAllTransactions(self):
        result = self.transactions
        return result

    def getTransactionById(self, tid):
        for t in self.transactions:
            if t['tid'] == tid:
                return t
        return None

    def getTransactionByDate(self, tdate):
        for t in self.transactions:
            if t['tdate'] == tdate:
                return t
        return None

    def getTransactionByQuantity(self, quan):
        for t in self.transactions:
            if t['tquantity'] == quan:
                return t
        return None

    def getTransactionByPayer(self, p):
        for t in self.transactions:
            if t['tpayer'] == p:
                return t
        return None

    def getTransactionBySupplier(self, s):
        for t in self.transactions:
            if t['tsupplier'] == s:
                return t
        return None

    def getTransactionBySupplier(self, s):
        for t in self.transactions:
            if t['tsupplier'] == s:
                return t
        return None

    def getTransactionByResource(self, r):
        for t in self.transactions:
            if t['tresource'] == r:
                return t
        return None

    def getTransactionByAmmount(self, a):
        for t in self.transactions:
            if t['tpayAmmount'] == a:
                return t
        return None

    def getPayerBytId(self, tid):
        for t in self.transactions:
            if t["tid"] == tid:
                return t['tpayer']
        return None

    def getSupplierBytId(self, tid):
        for t in self.transactions:
            if t["tid"] == tid:
                return t['tsupplier']
        return None

    def getResourceBytId(self, tid):
        for t in self.transactions:
            if t["tid"] == tid:
                return t['tresource']
        return None

    def countTransactions(self):
        return len(self.transactions)

    def insert(self, tDate, tQuantity, tPayer, tSupplier, tResource, tAmmount):
        newTId = len(self.transactions) + 1
        newTransaction = {
            'tid': len(self.transactions) + 1,
            'tdate': tDate,
            'tquantity': tQuantity,
            'tpayer': tPayer,
            'tsupplier': tSupplier,
            'tresource': tResource,
            'tpayAmmount': tAmmount
        }
        self.transactions.append(newTransaction)
        return newTId

    def delete(self, tid):
        pos = 0
        for t in self.transactions:
            if int(t['tid']) == int(tid):
                del self.transactions[pos]
                return True
            pos += 1

        return False

    def update(self, tid, tDate, tQuantity, tPayer, tSupplier, tResource, tAmmount):
        for t in self.transactions:
            if t['tid'] == tid:
                t = {
                    'tid': tid,
                    'tdate': tDate,
                    'tquantity': tQuantity,
                    'tpayer': tPayer,
                    'tsupplier': tSupplier,
                    'tresource': tResource,
                    'tpayAmmount': tAmmount
                }
                return True
        return False
