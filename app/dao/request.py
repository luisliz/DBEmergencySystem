from app.config.database_config import pg_config
import psycopg2


class RequestDAO:

    def __init__(self):
        self.conn = psycopg2.connect(
            user=pg_config["user"],
            password=pg_config['passwd'],
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database']
        )

        self.requests = [
            {
                'reqId': 1,
                'reqQuantity': 4,  # eliminate
                'reqPostDate': 408109458,
                'reqDispatchDate': 5908230598,
                'reqLocation': 'Guayama',
                'requestUid': 1,
                'supplierUid': 2,
                'rid': 3,
            }
        ]

    def getAllRequests(self):  # Done
        cursor = self.conn.cursor()
        query = "select * from requests;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestById(self, reqId):  # Done
        cursor = self.conn.cursor()
        query = f"select * from requests where reqid = {reqId};"
        cursor.execute(query)
        return cursor.fetchone()

    def getRequestsFromRequester(self, requestUid):  # Done
        cursor = self.conn.cursor()
        query = f"select * from requests where requestuid = {requestUid};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsFromSupplier(self, supplierUid):  # done
        cursor = self.conn.cursor()
        query = f"select * from requests where supplieruid = {supplierUid};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesFromRequest(self, reqID):  # Done
        cursor = self.conn.cursor()
        query = f"select RPR.rid, rprid, reqid, rname, rquantity, rlocation, ravailability from resources_per_request as RPR natural inner join resources natural inner join resource_details where reqid = {reqID};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResourcesByKeyword(self, rName):  # Done
        cursor = self.conn.cursor()
        query = f"select RPR.rid, rprid, reqid, rname, rquantity, rlocation, ravailability from resources_per_request as RPR natural inner join resources natural inner join resource_details natural inner join requests where reqdispatchdate is null and rname = '{rName}';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def addRequest(self, reqpostdate, reqlocation, requesterID, supplierID, resources):
        cursor = self.conn.cursor()
        query = "INSERT INTO requests(reqpostdate, reqlocation, requestuid, supplieruid) VALUES (%s, %s, %s, %s) returning reqid"
        cursor.execute(query, (reqpostdate, reqlocation, requesterID, supplierID))
        reqid = cursor.fetchone()[0]
        for res in resources:
            query = "INSERT INTO resources_per_request (reqid, rid, reqquantity) VALUES (%s, %s, %s);"
            cursor.execute(query, (reqid, res['rid'], res['reqquantity'],))
        self.conn.commit()
        return reqid

    """
    def getRequestByResourceId(self, resourceid): #Done
        cursor = self.conn.cursor()
        query = "select * from requests where rid = {resourceid};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestQuantity(self, reqId): #Done #HANDLER
        cursor = self.conn.cursor()
        query = "select reqquantity from requests where reqid = {reqId};"
        cursor.execute(query)
        return cursor.fetchone()

    def getRequestDispatchDate(self, reqId): #Done
        cursor = self.conn.cursor()
        query = "select reqdispatchdate from requests where reqid = {reqId};"
        cursor.execute(query)
        return cursor.fetchone()

    def getRequestPostDate(self, reqId): #Done
        cursor = self.conn.cursor()
        query = "select reqpostdate from request where reqid = {reqId};"
        cursor.execute(query)
        return cursor.fetchone()

    def getRequestLocation(self, reqId): #Done
        cursor = self.conn.cursor()
        query = "select reqlocation from requests where reqid = {reqId};"
        cursor.execute(query)
        return cursor.fetchone()

    def countRequests(self): #done
        cursor = self.conn.cursor()
        query = "select  count(*) from requests;"
        cursor.execute(query)
        return cursor.fetchone()

    def countRequestByResource(self, rid):
        cursor = self.conn.cursor()
        query = "select  count(*) from requests where rid = {rid};"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    

    def updateRequest(self, reqId, reqQuantity, reqPostDate, reqDispatchDate, reqLocation, requestUid, supplierUid, rid):
        pos = 0
        for req in self.requests:
            if int(req['reqId']) == int(reqId):
                newReq = self.requests[pos]
                newReq['reqQuantity'] = reqQuantity
                newReq['reqPostDate'] = reqPostDate
                newReq['reqDispatchDate'] = reqDispatchDate
                newReq['reqLocation'] = reqLocation
                newReq['requestUid'] = requestUid
                newReq['supplierUid'] = supplierUid
                newReq['rid'] = rid
                return True
            pos += 1
        return False

    def removeRequest(self, reqId):
        pos = 0
        for req in self.requests:
            if int(req['reqId']) == int(reqId):
                del self.requests[pos]
                return True
            pos += 1

        return False
    """
