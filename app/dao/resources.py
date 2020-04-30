from app.config.database_config import pg_config
import psycopg2

#TODO: add handler and routes for requested dispatched and non dispatched
#TODO: add resource/<rid>/details route para pedir details solo y usar su dao
#TODO: falta anadir errores and calls to queries to check more errors
#TODO: see what routes can get grouped together, group them
#TODO: see what parameters can be body args, change
#TODO: check for error manegement con rd and rc
#TODO: aggregate queries de P2
#TODO: revisa that u meet all spec reqs

class ResourcesDAO:

    def __init__(self):
        self.conn = psycopg2.connect(
            user=pg_config["user"],
            password=pg_config['passwd'],
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database']
        )

        self.allrplusrd = "select distinct r.rid, r.rname, r.rcid, rd.rdid, rd.rquantity, rd.rlocation, rd.ravailability, rd.supplieruid, rd.rprice from resources as r inner join resource_details as rd on r.rid = rd.rid "

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
        query = self.allrplusrd
        cursor.execute(query)
        result = []                 #this is a 'table', a list of lists: result[0][0] --> first row, value in first col
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResources(self):
        cursor = self.conn.cursor()
        # query = "select distinct r.rid, r.rname, r.rcid, rd.rdid, rd.rquantity, rd.rlocation, rd.ravailability, rd.supplieruid, rd.rprice from resources as r inner join resource_details as rd on r.rid = rd.rid inner join requests as req on r.rid = req.rid;"
        query = self.allrplusrd + "inner join requests as req on r.rid = req.rid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResourcesUndispatched(self):
        cursor = self.conn.cursor()
        query = self.allrplusrd + "inner join requests as req on r.rid = req.rid where req.reqdispatchdate is null;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResourcesDispatched(self):
        cursor = self.conn.cursor()
        query = self.allrplusrd + "inner join requests as req on r.rid = req.rid where req.reqdispatchdate is not null;" #might be problematix
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResourceById(self, rid):
        cursor = self.conn.cursor()
        query = self.allrplusrd + "inner join requests as req on r.rid = req.rid where r.rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        query = self.allrplusrd + "where r.rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourceByName(self, rName): #Done
        cursor = self.conn.cursor()
        query = self.allrplusrd + "where rName ilike '" + rName + "%';"
        # query = "select * from resources where rName ilike %s%%;"
        # cursor.execute(query, (rName,))
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getResourcesByCategory(self, category): #Done
        cursor = self.conn.cursor()
        query = self.allrplusrd + "natural inner join resource_category where rcName = %s;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByAvailability(self, avail): #Done
        cursor = self.conn.cursor()
        query = self.allrplusrd + "where rd.ravailability = %s;"
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




