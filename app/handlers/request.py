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
        return result

    def getRequestsFromRequester(self, requesterID):
        dao = RequestDAO()
        result = dao.getRequestsFromRequester(requesterID)
        return result

    def getRequestsFromSupplier(self, supplierid):
        dao = RequestDAO()
        result = dao.getRequestsFromSupplier(supplierid)
        return result

    def getRequestByResourceId(self, resourceid):
        dao = RequestDAO()
        result = dao.getRequestByResourceId(resourceid)
        return result

    def getRequestQuantity(self, reqid):
        dao = RequestDAO()
        result = dao.getRequestQuantity(reqid)
        return result

    def getRequestDispatchDate(self, reqid):
        dao = RequestDAO()
        result = dao.getRequestDispatchDate(reqid)
        return result

    def getRequestPostDate(self, reqid):
        dao = RequestDAO()
        result = dao.getRequestPostDate(reqid)
        return result

    def getRequestLocation(self, reqid):
        dao = RequestDAO()
        result = dao.getRequestLocation(reqid)
        return result

    def addRequest(self, form):
        dao = RequestDAO()
        result = dao.addRequest()
        return result

    def updateRequest(self, form):
        dao = RequestDAO()
        result = dao.updateRequest()
        return result

    def removeRequest(self, reqid):
        dao = RequestDAO()
        result = dao.removeRequest(reqid)
        return result

    def countRequests(self):
        dao = RequestDAO()
        result = dao.countRequests()
        return result

    def countRequestByResource(self):
        dao = RequestDAO()
        result = dao.countRequestByResource()
        return result
