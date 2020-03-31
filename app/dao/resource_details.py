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
                'rdid': 1,
                'rid': 1,
                'rdQuantity': 2,
                'rdLocation': 'Mayaguez',
                'rdAvailability': 'reserved',
                'supplierID': 1,
                'price_per_unit': 1.00
            },
            {
                'rdid': 2,
                'rid': 2,
                'rdQuantity': 4,
                'rdLocation': 'Cabo Rojo',
                'rdAvailability': 'purchased',
                'supplierID': 3,
                'price_per_unit': 10.00
            },
            {
                'rdid': 3,
                'rid': 3,
                'rdQuantity': 3,
                'rdLocation': 'Sabana Grande',
                'rdAvailability': 'available',
                'supplierID': 1,
                'price_per_unit': 2.00
            },
            {
                'rdid': 4,
                'rid': 4,
                'rdQuantity': 15,
                'rdLocation': 'Mayaguez',
                'rdAvailability': 'purchased',
                'supplierID': 1,
                'price_per_unit': 1.00
            }
        ]

    def getDetailsById(self, rdid):
        for rd in self.rdetails:
            if rd['rdid'] == rdid:
                return rd
        return None

    def getDetailsByResourceId(self, rid):
        for rd in self.rdetails:
            if rd['rid'] == rid:
                return rd
        return None

    def insert(self, rid, rdQuantity, rdLocation, rdAvailability, supplierID, price_per_unit):
        newID = len(self.rdetails) + 1
        new_resource_detail = {
            'rdid': newID,
            'rdQuantity': rdQuantity,
            'rdLocation': rdLocation,
            'rdAvailability': rdAvailability,
            'rid': rid,
            'supplierID': supplierID,
            'price_per_unit': price_per_unit
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
                newRes['rdAvailability'] = status
                return True
            pos += 1
        # there will be queries that update the resource details table
        return False

    def update(self, rid, rdQuantity, rdLocation, rdAvailability, supplierID, price_per_unit):
        pos = 0
        for rd in self.rdetails:
            if int(rd['rid']) == int(rid):
                newRes = self.rdetails[pos]
                newRes['rdQuantity'] = rdQuantity
                newRes['rdLocation'] = rdLocation
                newRes['rdAvailability'] = rdAvailability
                newRes['supplierID'] = supplierID
                newRes['price_per_unit'] = price_per_unit
                return True
            pos += 1
        # there will be queries that update the resource details table
        return False




