from app.config.database_config import pg_config
import psycopg2

class ResourceDetailsDAO:

    def __init__(self):
        self.conn = psycopg2.connect(
            user=pg_config["user"],
            password=pg_config['passwd'],
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database']
        )

        # self.rdetails = [
        #     {
        #         'rid': 1,
        #         'rquantity': 2,
        #         'rlocation': 'Mayaguez',
        #         'ravailability': 'reserved',
        #         'supplierUid': 1,
        #         'rPrice': 1.00
        #     },
        #     {
        #         'rid': 2,
        #         'rquantity': 4,
        #         'rlocation': 'Cabo Rojo',
        #         'ravailability': 'purchased',
        #         'supplierUid': 3,
        #         'rPrice': 10.00
        #     },
        #     {
        #         'rid': 3,
        #         'rquantity': 3,
        #         'rlocation': 'Sabana Grande',
        #         'ravailability': 'available',
        #         'supplierUid': 1,
        #         'rPrice': 2.00
        #     },
        #     {
        #         'rid': 4,
        #         'rquantity': 15,
        #         'rlocation': 'Mayaguez',
        #         'ravailability': 'purchased',
        #         'supplierUid': 1,
        #         'rPrice': 1.00
        #     }
        # ]

    def getDetailsByResourceId(self, rid): #Done
        cursor = self.conn.cursor()
        query = "select * from resource_details where rid = %s;"
        cursor.execute(query,(rid,))
        result = cursor.fetchone()
        return result

    def getAvailabilityValues(self): #Done
        cursor = self.conn.cursor()
        query = "SELECT unnest(enum_range(NULL::availability))::text;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rid, rquantity, rlocation, ravailability, supplierUid, rPrice):
        cursor = self.conn.cursor()
        query = "insert into resource_details (rid, rquantity, rlocation, ravailability, supplierUid, rPrice) values (%s, %s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, rquantity, rlocation, ravailability, supplierUid, rPrice))
        self.conn.commit()
        return cursor.fetchone()[0] 

    def deleteByDetailId(self, rdid):
        pos = 0
        for rd in self.rdetails:
            if int(rd['rdid']) == int(rdid):
                del self.rdetails[pos]
                return True
            pos += 1
        return False

    def deleteByResourceId(self, rid):
        pos = 0
        for rd in self.rdetails:
            if int(rd['rid']) == int(rid):
                del self.rdetails[pos]
                return True
            pos += 1
        return False

    #Needs testing
    def updateAvailability(self, rid, status):
        try:
            cursor = self.conn.cursor()
            query = f"update resource_details set ravailability = '{status}' where rid = {rid}"
            cursor.execute(query)
            return True

        #Might be bad to use bare except
        except:
            return False

    def update(self, rid, rquantity, rlocation, ravailability, supplierUid, rPrice):
        pos = 0
        for rd in self.rdetails:
            if int(rd['rid']) == int(rid):
                newRes = self.rdetails[pos]
                newRes['rquantity'] = rquantity
                newRes['rlocation'] = rlocation
                newRes['ravailability'] = ravailability
                newRes['supplierUid'] = supplierUid
                newRes['rPrice'] = rPrice
                return True
            pos += 1
        # there will be queries that update the resource details table
        return False




