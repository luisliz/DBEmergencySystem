from app.config.database_config import pg_config
class RequestDAO:

    def __init__(self):
        '''
           #connection_url = "dbname=%s t=%s password=%s" % (pg_config['dbname'],
                                                                pg_config['t'],
                                                                pg_config['passwd'])
            #self.conn = psycopg2._connect(connection_url)
        '''
        self.requests = [
            {
                'reqId': 1,
                'reqQuantity': 4,
                'reqPostDate': 408109458,
                'reqDispatchDate': 5908230598,
                'reqLocation': 'Guayama',
                'requestUid': 1,
                'supplierUid': 2,
                'rid': 3,
            }
        ]

    def getAllRequests(self): #Done
        result = self.requests
        return result

    def getRequestById(self, reqId): #Done
        for r in self.requests:
            if r['reqId'] == reqId:
                return r
        return None

    def getRequestsFromRequester(self, requestUid): #Done
        result = []
        for r in self.requests:
            if r['requestUid'] == requestUid:
                result.append(r)
        return result

    def getRequestsFromSupplier(self, supplierUid): #done
        result = []
        for r in self.requests:
            if r['supplierUid'] == supplierUid:
                result.append(r)
        return result

    def getRequestByResourceId(self, resourceid): #Done
        result = []
        for r in self.requests:
            if r['rid'] == resourceid:
                result.append(r)
        return result

    def getRequestQuantity(self, reqId): #Done
        for r in self.requests:
            if r['reqId'] == reqId:
                return r['reqQuantity']
        return None

    def getRequestDispatchDate(self, reqId): #Done
        for r in self.requests:
            if r['reqId'] == reqId:
                return r['reqDispatchDate']
        return None

    def getRequestPostDate(self, reqId): #Done
        for r in self.requests:
            if r['reqId'] == reqId:
                return r['reqPostDate']
        return None

    def getRequestLocation(self, reqId): #Done
        for r in self.requests:
            if r['reqId'] == reqId:
                return r['reqLocation']
        return None

    def addRequest(self, req_quantitiy, reqPostDate, reqDispatchDate, reqLocation, requestUid, supplierUid, rid):
        newID = len(self.requests)+1
        return newID

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

    def countRequests(self): #done
        return len(self.requests)

    def countRequestByResource(self, rid):
        count = 0
        for r in self.requests:
            if r['rid'] == rid:
                count = count + 1
        return count

