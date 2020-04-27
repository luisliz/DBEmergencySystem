from app.config.database_config import pg_config
import psycopg2

#TODO: falta anadir errores and calls to queries to check more errors
#TODO: bregar con resource details (refactor resource dict to include rdetails too, along with changing queries so that they join in)
#TODO: see what routes can get grouped together, group them
#TODO: see what parameters can be body args, change 

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
        query = "select * from resources where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourceByName(self, rName):
        cursor = self.conn.cursor()
        query = "select * from resources where rName ilike '" + rName + "%';"
        # query = "select * from resources where rName ilike %s%%;"
        # cursor.execute(query, (rName,))
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getResourcesByCategory(self, category): #falta hacer check con query a category
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join resource_category where rcName = %s;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByAvailability(self, avail): #Done
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join resource_details where ravailability = %s;"
        cursor.execute(query, (avail,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByResourceId(self, rid): #Done
        cursor = self.conn.cursor()
        query = "select * from users inner join resource_details on supplieruid = uid where rid = %s"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

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




