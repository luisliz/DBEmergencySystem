from app.config.database_config import pg_config
import psycopg2

class ResourcesDAO:

    def __init__(self):
        self.conn = psycopg2.connect(
            user=pg_config["user"],
            password=pg_config['passwd'],
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database']
        )

        # self.resources = [
        #     {
        #         'rid': 1,
        #         'rName': 'Water',
        #         'rcId': 1
        #     },
        #     {
        #         'rid': 2,
        #         'rName': 'Cannabis',
        #         'rcId': 2
        #     },
        #     {
        #         'rid': 3,
        #         'rName': 'Chef Boyardee',
        #         'rcId': 3
        #     },
        #     {
        #         'rid': 4,
        #         'rName': 'Tylenol',
        #         'rcId': 2
        #     }
        # ]

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resources;"
        cursor.execute(query)
        result = []                 #this is a 'table', a list of lists: result[0][0] --> first row, value in first col
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResources(self):
        # cursor = self.conn.cursor()
        # query = "<query that gets all resources that have a record in the request table and havent been dispatched yet>"
        # cursor.execute(query)
        # result = []
        # for row in self.resources:#cursor:
        #     result.append(row)
        result = self.resources
        return result

    def getRequestedResourceById(self, rid):
        # cursor = self.conn.cursor()
        # query = "<query that gets all resources that have a record in the request table and havent been dispatched yet
        # and filters it with the given id>"
        # cursor.execute(query)
        # result = []
        # for row in self.resources:#cursor:
        #     result.append(row)
        for res in self.resources:
            if res['rid'] == rid:
                return res
        return None

    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid = " + str(rid) + ";"
        cursor.execute(query)
        result = []  # this is a 'table', a list of lists: result[0][0] --> first row, value in first col
        for row in cursor:
            result.append(row)
        return result

    def getResourceByName(self, rName):
        for res in self.resources:
            if res['rName'] == rName:
                return res
        return None

    def getResourcesByCategory(self, category):
        # cursor = self.conn.cursor()
        # query = "select rid, rName from resources inner join resource_category on resources.rcId = resource_category.rcId
        # where resource_category.rcName = category;"
        # cursor.execute(query)
        # result = []
        # for row in self.resources:#cursor:
        #     result.append(row)
        if (category == 'Water'):
            result = [self.resources[0]]
        elif (category == 'Medication'):
            result = [self.resources[1], self.resources[3]]
        elif (category == 'Canned Food'):
            result = [self.resources[2]]
        else:
            result = []
        return result

    def getResourcesByAvailability(self, avail):
        # cursor = self.conn.cursor()
        # query = "select rid, rName from resources inner join resource_category on resources.rcId = resource_category.rcId
        # where resource_category.rcAvailability = avail;"
        # cursor.execute(query)
        # result = []
        # for row in self.resources:#cursor:
        #     result.append(row)
        if (avail == 'purchased'):
            result = [self.resources[1], self.resources[3]]
        elif (avail == 'reserved'):
            result = [self.resources[0]]
        elif (avail == 'available'):
            result = [self.resources[2]]
        else:
            result = []
        return result

    def getSupplierByResourceId(self, rid):
        # cursor = self.conn.cursor()
        # query = "" #query that gets supplierID from resource details and joins it with the user table to get firstname and lastname too
        # cursor.execute(query)
        # result = []
        # for row in self.resources:#cursor:
        #     result.append(row)
        return [1, 'John', 'Mendez']

    def insert(self, rName, rcId):
        newRID = len(self.resources)+1
        new_resource = {
            'rid': newRID,
            'rName': rName,
            'rcId': rcId
        }
        self.resources.append(new_resource)
        #here would come a query to insert the new resource into the table
        return newRID

    def delete(self, rid):
        pos = 0
        for res in self.resources:
            if int(res['rid']) == int(rid):
                del self.resources[pos]
                return True
            pos += 1

        return False

    def update(self, rid, rName, rcId):
        pos = 0
        for res in self.resources:
            if int(res['rid']) == int(rid):
                newRes = self.resources[pos]
                newRes['rName'] = rName
                newRes['rcId'] = rcId
                return True
            pos += 1
        return False




