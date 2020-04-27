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

    def getDetailsByResourceId(self, rid): #this hasnt been tested, pero debe funcionar
        cursor = self.conn.cursor()
        query = "select * from resource_details where rid = %s;"
        cursor.execute(query,(rid,))
        result = cursor.fetchone()
        return result

    def getAvailabilityValues(self):
        cursor = self.conn.cursor()
        query = "SELECT unnest(enum_range(NULL::availability))::text;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rid, rquantity, rlocation, ravailability, supplierUid, rPrice):
        newID = len(self.rdetails) + 1
        new_resource_detail = {
            'rdid': newID,
            'rquantity': rquantity,
            'rlocation': rlocation,
            'ravailability': ravailability,
            'rid': rid,
            'supplierUid': supplierUid,
            'rPrice': rPrice
        }
        self.rdetails.append(new_resource_detail)
        # here would come a querie to insert the new resource detail into the table
        return newID

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

    def updateAvailability(self, rid, status):
        pos = 0
        for res in self.rdetails:
            if int(res['rid']) == int(rid):
                newRes = self.rdetails[pos]
                newRes['ravailability'] = status
                return True
            pos += 1
        # there will be queries that update the resource details table
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




