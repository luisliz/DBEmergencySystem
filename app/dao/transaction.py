from app.config.database_config import pg_config

class TransactionDAO:
    def __init__(self):
        '''
           #connection_url = "dbname=%s t=%s password=%s" % (pg_config['dbname'],
                                                                pg_config['username'],
                                                                pg_config['passwd'])
            #self.conn = psycopg2._connect(connection_url)
        '''
        self.transactions = [
            {
                'tid': 1,
                'tdate': '02/02/2020',
                'tquantity': '10',
                'uid': 1,
                'supplierUid': 2,
                'rid': 1,
                'tamount': 50.0
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
            if t['uid'] == p:
                return t
        return None

    def getTransactionBySupplier(self, s):
        for t in self.transactions:
            if t['supplierUid'] == s:
                return t
        return None

    def getTransactionByResource(self, r):
        for t in self.transactions:
            if t['rid'] == r:
                return t
        return None

    def getTransactionByAmmount(self, a):
        for t in self.transactions:
            if t['tpayAmmount'] == a:
                return t
        return None

    def geuidBytId(self, tid):
        for t in self.transactions:
            if t["tid"] == tid:
                return t['uid']
        return None

    def gesupplierUidBytId(self, tid):
        for t in self.transactions:
            if t["tid"] == tid:
                return t['supplierUid']
        return None

    def geridBytId(self, tid):
        for t in self.transactions:
            if t["tid"] == tid:
                return t['rid']
        return None

    def countTransactions(self):
        return len(self.transactions)

    def insert(self, tDate, tquantity, uid, supplierUid, rid, tAmmount):
        newTId = len(self.transactions) + 1
        newTransaction = {
            'tid': len(self.transactions) + 1,
            'tdate': tDate,
            'tquantity': tquantity,
            'uid': uid,
            'supplierUid': supplierUid,
            'rid': rid,
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

    def update(self, tid, tDate, tquantity, uid, supplierUid, rid, tAmmount):
        for t in self.transactions:
            if t['tid'] == tid:
                t = {
                    'tid': tid,
                    'tdate': tDate,
                    'tquantity': tquantity,
                    'uid': uid,
                    'supplierUid': supplierUid,
                    'rid': rid,
                    'tpayAmmount': tAmmount
                }
                return True
        return False
