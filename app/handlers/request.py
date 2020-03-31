from flask import jsonify
from app.dao.request import RequestDAO

class RequestHandler:
    def build_request_dict(self, row):
        return row

    def getAllRequests(self):
        dao = RequestDAO()
        result = dao.getAllRequests()
        return jsonify(Requests=result)

    def getRequestById(self, reqid):
        dao = RequestDAO()
        result = dao.getRequestById(reqid)
        return jsonify(Request=result)

    def getRequestsFromRequester(self, requesterID):
        dao = RequestDAO()
        result = dao.getRequestsFromRequester(requesterID)
        return jsonify(Requests=result)

    def getRequestsFromSupplier(self, supplierid):
        dao = RequestDAO()
        result = dao.getRequestsFromSupplier(supplierid)
        return jsonify(Requests=result)

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
        dao = RequestDAO()
        result = dao.addRequest()
        return jsonify(Added=result)

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

    def countRequests(self):
        dao = RequestDAO()
        result = dao.countRequests()
        return jsonify(Count=result)

    def countRequestByResource(self, rid):
        dao = RequestDAO()
        result = dao.countRequestByResource(rid)
        return jsonify(Count=result)
