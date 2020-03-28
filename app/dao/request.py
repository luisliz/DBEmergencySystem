from app.config.database_config import pg_config
class RequestDAO:
    self.requests = [
        {
            'reqid': 1,
            'req_quantitiy': 4,
            'req_post_date': 408109458,
            'req_dispatch_date': 5908230598,
            'req_location': 'Guayama',
            'requesterID': 1,
            'supplierID': 2,
            'rid': 3,
        }
    ]
    def __init__(self):
        '''
           #connection_url = "dbname=%s t=%s password=%s" % (pg_config['dbname'],
                                                                pg_config['t'],
                                                                pg_config['passwd'])
            #self.conn = psycopg2._connect(connection_url)
        '''

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
        for r in self.requests:
            if r['reqid'] == reqid:
                return r
        return

    def updateRequest(self):
        for r in self.requests:
            if r['reqid'] == reqid:
                return r
        return

    def removeRequest(self):
        for r in self.requests:
            if r['reqid'] == reqid:
                return r
        return

    def countRequests(self): #done
        return len(self.requests)

    def countRequestByResource(self):
        for r in self.requests:
            if r['reqid'] == reqid:
                return r
        return

