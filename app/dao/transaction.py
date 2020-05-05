from app.config.database_config import pg_config
import psycopg2

class TransactionDAO:
    def __init__(self):
        self.conn = psycopg2.connect(
            user=pg_config["user"],
            password=pg_config['passwd'],
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database']
        )

    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "select * from transactions;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionById(self, tid):
        cursor = self.conn.cursor()
        query = f"select * from transactions where tid = {tid};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllReservations(self):
        cursor = self.conn.cursor()
        query = "select * from transactions where tamount = 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReservationById(self, tid):
        cursor = self.conn.cursor()
        query = f"select * from transactions where tamount = 0 and tid = {tid};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllPurchases(self):
        cursor = self.conn.cursor()
        query = "select * from transactions where tamount > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getPurchaseById(self, tid):
        cursor = self.conn.cursor()
        query = f"select * from transactions where tamount > 0 and tid = {tid};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByDate(self, tdate):
        cursor = self.conn.cursor()
        query = f"select * from transactions where tdate = '{tdate}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByQuantity(self, quan):
        cursor = self.conn.cursor()
        query = f"select * from transactions where tquantity = {quan};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Needs testing
    def getTransactionByPayerPaymentInfo(self, ppid):
        cursor = self.conn.cursor()
        query = f"select * from transactions where tpayerpid = {ppid};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Needs testing
    def getTransactionBySupplierPaymentInfo(self, spid):
        cursor = self.conn.cursor()
        query = f"select * from transactions where tsupplierpid = {spid};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Need testing
    def getTransactionByPayer(self, uidp):
        cursor = self.conn.cursor()
        query = f"select tid, tdate, tquantity, tpayerpid, tsupplierpid, trid, tamount from transactions as T inner join payments as P inner join users as U on T.tpayerpid = P.pid where U.uid = {uidp};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Need testing
    def getTransactionBySupplier(self, uids):
        cursor = self.conn.cursor()
        query = f"select tid, tdate, tquantity, tpayerpid, tsupplierpid, trid, tamount from transactions as T inner join payments as P inner join users as U on T.tsupplierpid = P.pid where U.uid = {uids};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByResource(self, rid):
        cursor = self.conn.cursor()
        query = f"select * from transactions where  rid = {rid};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionByAmmount(self, amnt):
        cursor = self.conn.cursor()
        query = f"select * from transactions where tamount = {amnt};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # Need testing
    def getPayerPaymentInfoByTransactionId(self, tid):
        cursor = self.conn.cursor()
        query = f"select pid, pType, pProvider, pExpDate from transactions as T inner join payments as P on T.tpayerpid = P.pid where tid = '{tid}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Need testing
    def getSupplierPaymentInfoByTransactionId(self, tid):
        cursor = self.conn.cursor()
        query = f"select pid, pType, pProvider, pExpDate from transactions as T inner join payments as P on T.tsupplierpid = P.pid where tid = '{tid}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Need testing
    def getPayerByTransactionId(self, tid):
        cursor = self.conn.cursor()
        query = f"select U.uid, ucid, ufirstname, ulastname, udob, uemail from transactions as T inner join payments as P inner join users as U on T.tpayerpid = P.pid where tid = '{tid}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Need tsting
    def getSupplierByTransactionId(self, tid):
        cursor = self.conn.cursor()
        query = f"select U.uid, ucid, ufirstname, ulastname, udob, uemail from transactions as T inner join payments as P inner join users as U on T.tsupplierpid = P.pid where tid = '{tid}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceByTransactionId(self, tid):
        cursor = self.conn.cursor()
        query = f"select rid, rName, rcid from transactions natural inner join resources where tid = '{tid}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def countTransactions(self):
        cursor = self.conn.cursor()
        query = f"select count(*) from transactions;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    """///////////////////////////////////////PAST PHASE 2///////////////////////////////////////////////////////////"""

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
