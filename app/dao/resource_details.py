from app.config.database_config import pg_config
# import psycopg2

class ResourceDetailsDAO:

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        # self.conn = psycopg2._connect(connection_url)

        self.rdetails = [
            {
                'rid': 1,
                'rquantity': 2,
                'rlocation': 'Mayaguez',
                'ravailability': 'reserved',
                'supplierUid': 1,
                'rPrice': 1.00
            },
            {
                'rid': 2,
                'rquantity': 4,
                'rlocation': 'Cabo Rojo',
                'ravailability': 'purchased',
                'supplierUid': 3,
                'rPrice': 10.00
            },
            {
                'rid': 3,
                'rquantity': 3,
                'rlocation': 'Sabana Grande',
                'ravailability': 'available',
                'supplierUid': 1,
                'rPrice': 2.00
            },
            {
                'rid': 4,
                'rquantity': 15,
                'rlocation': 'Mayaguez',
                'ravailability': 'purchased',
                'supplierUid': 1,
                'rPrice': 1.00
            }
        ]

    def getDetailsByResourceId(self, rid):
        for rd in self.rdetails:
            if rd['rid'] == rid:
                return rd
        return None

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




