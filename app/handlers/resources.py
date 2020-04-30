from flask import jsonify
from app.dao.resources import ResourcesDAO
from app.dao.resource_details import ResourceDetailsDAO


class ResourceHandler:
    # def build_resource_dict(self, row):
    #     result = {}
    #     result['rid'] = row[0]
    #     result['rName'] = row[1]
    #     result['rcid'] = row[2]
    #     return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['rcid'] = row[2]
        result['rdid'] = row[3]
        result['rquantity'] = row[4]
        result['rlocation'] = row[5]
        result['ravailability'] = row[6]
        result['supplieruid'] = row[7]
        result['rprice'] = row[8]

        return result

    def build_supplier_dict(self, row):
        result = {}
        result['supplierID'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        return result

    def get_all_resources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources() #this too, is a 'table', list of lists (rows)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def get_resource_details(self, rid):
        dao = ResourceDetailsDAO()
        resource = dao.getDetailsByResourceId(rid)
        result = self.build_resource_dict(resource)
        return jsonify(Resource=result)

    def get_resource_by_id(self, rid):
        dao = ResourcesDAO()
        row = dao.getResourceById(rid)  # in this case, this is just a tuple
        result = self.build_resource_dict(row)
        return jsonify(Resources=result)

    def get_resource_by_name(self, rName):
        dao = ResourcesDAO()
        row = dao.getResourceByName(rName)  # in this case, this is just a tuple
        if not (row):
            return jsonify(Error="No resources found with that name"), 404
        result = self.build_resource_dict(row)
        return jsonify(Resources=result)

    def get_resources_by_category(self, category):
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByCategory(category) #list of tuples, a 'table'
        if not (resources_list):
            return jsonify(Error="No resources found for that category"), 404
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row) #el dict asocia cada valor del tuplo con su column name
            result_list.append(result)
        return jsonify(Resources=result_list)

    def get_resources_by_availability(self, avail):
        if not (self.findEnumMatch(avail)):
            return jsonify(Error = "Incorrect availability."), 400
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByAvailability(avail)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def findEnumMatch(self, enum):
        daoRD = ResourceDetailsDAO()
        values = daoRD.getAvailabilityValues() #this is a list of tuples with the enum values
        for val in values:
            if (val[0] == enum):
                return True
        return False

    def get_supplier_by_resource_id(self, rid):
        dao = ResourcesDAO()
        if not (dao.getResourceById(rid)):
            return jsonify(Error = "Resource not found"), 404
        row = dao.getSupplierByResourceId(rid)
        if not (row):
            return jsonify(Error = "No supplier found."), 404
        result = self.build_supplier_dict(row)
        return jsonify(Supplier=result)

    def add_resource(self, form):
        rName = form['rName']
        rcid = form['rcid'] #this will probably be replaced by category name, followed by a lookup of rcid with respect to its name
        #the attributes below are for the insertion into the resoruce details table
        rdQuantity = form['rdQuantity']
        rdLocation = form['rdLocation']
        rdAvailability = form['rdAvailability']
        supplierID = form['supplierID']
        price_per_unit = form['price_per_unit']

        daoR = ResourcesDAO()
        daoRD = ResourceDetailsDAO()
        rid = daoR.insert(rName, rcid)
        daoRD.insert(rid, rdQuantity, rdLocation, rdAvailability, supplierID, price_per_unit)
        return jsonify(rid=rid)

    def delete_resource(self, form):
        dao = ResourcesDAO()
        rid = form['rid']
        resource = dao.delete(rid)
        return jsonify(deleted=resource)

    def update_resource(self, form):
        rid = form['rid']
        rName = form['rName']
        rcid = form['rcid']  # this will probably be replaced by category name, followed by a lookup of rcid with respect to its name
        # the attributes below are for the insertion into the resoruce details table
        rdQuantity = form['rdQuantity']
        rdLocation = form['rdLocation']
        rdAvailability = form['rdAvailability']
        supplierID = form['supplierID']
        price_per_unit = form['price_per_unit']

        daoR = ResourcesDAO()
        daoRD = ResourceDetailsDAO()
        rid = daoR.update(rid, rName, rcid)
        daoRD.update(rid, rdQuantity, rdLocation, rdAvailability, supplierID, price_per_unit)
        return jsonify(rid=rid)

    def get_requested_resources(self):
        dao = ResourcesDAO()
        resources_list = dao.getRequestedResources()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def get_requested_resource_by_id(self, rid):
        dao = ResourcesDAO()
        resource = dao.getRequestedResourceById(rid)
        if not (resource):
            return jsonify(Error="Resource not found"), 404
        result = self.build_resource_dict(resource)
        return jsonify(Resource=result)

    def reserve_resource(self, rid, status):
        dao = ResourceDetailsDAO()
        result = dao.updateAvailability(rid, status)
        return jsonify(Reserved=result)

    def purchase_resource(self, rid, status):
        dao = ResourceDetailsDAO()
        result = dao.updateAvailability(rid, status)
        return jsonify(Reserved=result)

