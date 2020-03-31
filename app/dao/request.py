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
                'reqid': 1,
                'req_quantity': 4,
                'req_post_date': 408109458,
                'req_dispatch_date': 5908230598,
                'req_location': 'Guayama',
                'requesterID': 1,
                'supplierID': 2,
                'rid': 3,
            }
        ]

    def getAllRequests(self): #Done
        result = self.requests
        return result

    def getRequestById(self, reqid): #Done
        for r in self.requests:
            if r['reqid'] == reqid:
                return r
        return None

    def getRequestsFromRequester(self, requesterID): #Done
        result = []
        for r in self.requests:
            if r['requesterID'] == requesterID:
                result.append(r)
        return result

    def getRequestsFromSupplier(self, supplierid): #done
        result = []
        for r in self.requests:
            if r['supplierID'] == supplierid:
                result.append(r)
        return result

    def getRequestByResourceId(self, resourceid): #Done
        result = []
        for r in self.requests:
            if r['rid'] == resourceid:
                result.append(r)
        return result

    def getRequestQuantity(self, reqid): #Done
        for r in self.requests:
            if r['reqid'] == reqid:
                return r['req_quantity']
        return None

    def getRequestDispatchDate(self, reqid): #Done
        for r in self.requests:
            if r['reqid'] == reqid:
                return r['req_dispatch_date']
        return None

    def getRequestPostDate(self, reqid): #Done
        for r in self.requests:
            if r['reqid'] == reqid:
                return r['req_post_date']
        return None

    def getRequestLocation(self, reqid): #Done
        for r in self.requests:
            if r['reqid'] == reqid:
                return r['req_location']
        return None

    def addRequest(self, req_quantitiy, req_post_date, req_dispatch_date, req_location, requesterID, supplierID, rid):
        newID = len(self.requests)+1
        return newID

    def updateRequest(self, reqid, req_quantity, req_post_date, req_dispatch_date, req_location, requesterID, supplierID, rid):
        pos = 0
        for req in self.requests:
            if int(req['reqid']) == int(reqid):
                newReq = self.requests[pos]
                newReq['req_quantity'] = req_quantity
                newReq['req_post_date'] = req_post_date
                newReq['req_dispatch_date'] = req_dispatch_date
                newReq['req_location'] = req_location
                newReq['requesterID'] = requesterID
                newReq['supplierID'] = supplierID
                newReq['rid'] = rid
                return True
            pos += 1
        return False

    def removeRequest(self, reqid):
        pos = 0
        for req in self.requests:
            if int(req['reqid']) == int(reqid):
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

