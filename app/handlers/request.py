from flask import jsonify
from app.dao.request import RequestDAO

class RequestHandler:
    def build_request_dict(self, row):
        result = {}
        if row == None:
            return {'error': 'Request Not found'}
        else:
            result['reqid'] = row[0]
            result['reqpostdate'] = row[1]
            result['reqdispatchdate'] = row[2]
            result['reqlocation'] = row[3]
            result['requestuid'] = row[4]
            result['supplieruid'] = row[5]
            return result

    def build_requested_resource_dict(self, row):
        result = {}
        if row == None:
            return {'error': 'Request Not found'}
        else:
            result['rid'] = row[0]
            result['rprid'] = row[1]
            result['reqid'] = row[2]
            result['rname'] = row[3]
            result['rquantity'] = row[4]
            result['rlocation'] = row[5]
            result['ravailability'] = row[6]
            return result

    def getAllRequests(self):
        dao = RequestDAO()
        result = dao.getAllRequests()
        result_list = []
        for row in result:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    def getRequestById(self, reqid):
        dao = RequestDAO()
        result = dao.getRequestById(reqid)
        return jsonify(Request=self.build_request_dict(result))

    def getRequestsFromRequester(self, requesterID):
        dao = RequestDAO()
        requests_list = dao.getRequestsFromRequester(requesterID)
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestsFromSupplier(self, supplierid):
        dao = RequestDAO()
        result = dao.getRequestsFromSupplier(supplierid)
        return jsonify(Requests=result)

    def getResourcesFromRequest(self, reqID):
        dao = RequestDAO()
        requests_list = dao.getResourcesFromRequest(reqID)
        result_list = []
        for row in requests_list:
            result = self.build_requested_resource_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getRequestedResourcesByKeyword(self, rName):
        dao = RequestDAO()
        requests_list = dao.getRequestedResourcesByKeyword(rName)
        result_list = []
        for row in requests_list:
            result = self.build_requested_resource_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)
    """
    def getRequestByResourceId(self, resourceid):
        dao = RequestDAO()
        result = dao.getRequestByResourceId(resourceid)
        return jsonify(Request=result)
    
    
    def getRequestQuantity(self, reqid):
        dao = RequestDAO()
        result = dao.getRequestQuantity(reqid)
        return jsonify(Quantity=result)

    def getRequestDispatchDate(self, reqid):
        dao = RequestDAO()
        result = dao.getRequestDispatchDate(reqid)
        return jsonify(DispatchDate=result)

    def getRequestPostDate(self, reqid):
        dao = RequestDAO()
        result = dao.getRequestPostDate(reqid)
        return jsonify(PostDate=result)

    def getRequestLocation(self, reqid):
        dao = RequestDAO()
        result = dao.getRequestLocation(reqid)
        return jsonify(Location=result)

    def addRequest(self, form):
        req_quantity = form['req_quantity']
        req_post_date = form['req_post_date']
        req_dispatch_date = form['req_dispatch_date']
        req_location = form['req_location']
        requesterID = form['requesterID']
        supplierID = form['supplierID']
        rid = form['rid']

        dao = RequestDAO()
        result = dao.addRequest(req_quantity, req_post_date, req_dispatch_date, req_location, requesterID,
                                   supplierID, rid)
        return jsonify(Reqid=result)

    def updateRequest(self, form):
        reqid = form['reqid']
        req_quantity = form['req_quantity']
        req_post_date = form['req_post_date']
        req_dispatch_date = form['req_dispatch_date']
        req_location = form['req_location']
        requesterID = form['requesterID']
        supplierID = form['supplierID']
        rid = form['rid']

        dao = RequestDAO()
        result = dao.updateRequest(reqid, req_quantity, req_post_date, req_dispatch_date, req_location, requesterID, supplierID, rid)
        return jsonify(Updated=result)

    def removeRequest(self, reqid):
        dao = RequestDAO()
        result = dao.removeRequest(reqid)
        return jsonify(Removed=result)

    """
    def countRequests(self):
        dao = RequestDAO()
        result = dao.countRequests()
        return jsonify(Count=result)
