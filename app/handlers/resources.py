from flask import jsonify
from app.dao.resources import ResourcesDAO
from app.dao.resource_details import ResourceDetailsDAO


class ResourceHandler:

    def __init__(self):
        dao = ResourcesDAO()
        self.getcol = {
            'baby_foods': dao.getResourceColumns('baby_foods'),
            'ices': dao.getResourceColumns('ices'),
            'fuels': dao.getResourceColumns('fuels'),
            'heavy_equipments': dao.getResourceColumns('heavy_equipments'),
            'tools': dao.getResourceColumns('tools'),
            'medications': dao.getResourceColumns('medications'),
            'power_generators': dao.getResourceColumns('power_generators'),
            'waters': dao.getResourceColumns('waters'),
            'medical_devices': dao.getResourceColumns('medical_devices'),
            'batteries': dao.getResourceColumns('batteries'),
            'canned_foods': dao.getResourceColumns('canned_foods'),
            'dry_foods': dao.getResourceColumns('dry_foods'),
            'clothings': dao.getResourceColumns('clothings')
        }

    # def build_resource_dict(self, row):
    #     result = {}
    #     result['rid'] = row[0]
    #     result['rName'] = row[1]
    #     result['rcid'] = row[2]
    #     return result

    def build_resource_dict(self, columns, row):
        col = columns.copy()
        for c in range(len(col)):
            col[c] = col[c][0]

        col += ['rid', 'rname', 'rquantity', 'rlocation', 'ravailability', 'supplieruid', 'rprice']
        result = {}
        for i in range(len(col)):
            result[col[i]] = row[i]
        return result

    def build_details_dict(self, row):
        result = {}
        result['rdid'] = row[0]
        result['rquantity'] = row[1]
        result['rlocation'] = row[2]
        result['ravailability'] = row[3]
        result['supplieruid'] = row[4]
        result['rprice'] = row[5]

        return result

    def build_catcols_dict(self, catcols):
        result = {}
        result['medications'] = catcols[0]
        result['canned_foods'] = catcols[1]
        result['baby_foods'] = catcols[2]
        result['dry_foods'] = catcols[3]
        result['fuels'] = catcols[4]
        result['heavy_equipments'] = catcols[5]
        result['clothings'] = catcols[6]
        result['power_generators'] = catcols[7]
        result['medical_devices'] = catcols[8]
        result['batteries'] = catcols[9]
        result['tools'] = catcols[10]
        result['ices'] = catcols[11]
        result['waters'] = catcols[12]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['supplierID'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        return result

    def get_all_resources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()  # this too, is a 'table', list of lists (rows)
        if not (resources_list):
            return jsonify(Error="No resources found :("), 404
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    ####################### THE HOLLY GRAIL #########################################
    def get_resources_by_category(self, category):
        dao = ResourcesDAO()
        columns = self.getcol.get(category, [])
        if not columns:
            return jsonify(Error="Category not found"), 404
        else:
            resources = {
                'baby_foods': dao.getAllBabyFoods(),
                'ices': dao.getAllIces(),
                'fuels': dao.getAllFuels(),
                'heavy_equipments': dao.getAllHeavyEquipments(),
                'tools': dao.getAllTools(),
                'medications': dao.getAllMedications(),
                "power_generators": dao.getAllPowerGenerators(),
                'waters': dao.getAllWaters(),
                'medical_devices': dao.getAllMedicalDevices(),
                'batteries': dao.getAllBatteries(),
                'canned_foods': dao.getAllCannedFoods(),
                'dry_foods': dao.getAllDryFoods(),
                'clothings': dao.getAllClothings()
            }
            resources_list = resources.get(category, [])
            if not (resources_list):
                return jsonify(Error="No resources found :("), 404
            result_list = []
            for row in resources_list:
                result = self.build_resource_dict(columns, row)
                result_list.append(result)

            return jsonify(Resources=result_list)

    def get_resource_details_by_rid(self, rid):
        dao = ResourceDetailsDAO()
        details = dao.getDetailsByResourceId(rid)
        if not (details):
            return jsonify(Error="No resource details for that resource id"), 404
        result = self.build_details_dict(details)
        return jsonify(Resource_Details=result)

    def get_resource_by_id(self, rid):
        dao = ResourcesDAO()

        #this section is to find which category the resource belongs to
        catcols = dao.getCategoryColumnsByRID(rid) #this is a tuple with all values
        catcolsdict = self.build_catcols_dict(catcols)
        actualcat = ""
        for catcol in catcolsdict:
            if (catcolsdict[catcol]):
                actualcat = catcol
        columns = self.getcol.get(actualcat, [])

        #this section is to get the row for the resource
        resources = {
            # 'baby_foods': dao.getBabyFoodByRID(rid),
            'ices': dao.getIcesByRID(rid),
            'fuels': dao.getFuelsByRID(rid),
            'heavy_equipments': dao.getHeavyEquipmentsByRID(rid),
            'tools': dao.getToolsByRID(rid),
            'medications': dao.getMedicationsByRID(rid),
            "power_generators": dao.getPowerGeneratorsByRID(rid),
            'waters': dao.getWatersByRID(rid),
            'medical_devices': dao.getMedicalDevicesByRID(rid),
            'batteries': dao.getBatteriesByRID(rid),
            'canned_foods': dao.getCannedFoodsByRID(rid),
            'dry_foods': dao.getDryFoodsByRID(rid),
            'clothings': dao.getClothingsByRID(rid)
        }
        row = resources.get(actualcat, []) # in this case, this is just a tuple
        if not (row):
            return jsonify(Error="No resources found for that id"), 404
        result = self.build_resource_dict(columns, row)
        return jsonify(Resource=result)

    def get_resource_by_name(self, rName):
        dao = ResourcesDAO()
        row = dao.getResourceByName(rName)  # in this case, this is just a tuple
        if not (row):
            return jsonify(Error="No resources found with that name"), 404
        result = self.build_resource_dict(row)
        return jsonify(Resources=result)

    def get_resources_by_availability(self, avail):
        if not (self.findEnumMatch(avail)):
            return jsonify(Error="Incorrect availability."), 400
        dao = ResourcesDAO()
        resources_list = dao.getResourcesByAvailability(avail)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def findEnumMatch(self, enum):
        daoRD = ResourceDetailsDAO()
        values = daoRD.getAvailabilityValues()  # this is a list of tuples with the enum values
        for val in values:
            if (val[0] == enum):
                return True
        return False

    def get_supplier_by_resource_id(self, rid):
        dao = ResourcesDAO()
        if not (dao.getResourceById(rid)):
            return jsonify(Error="Resource not found"), 404
        row = dao.getSupplierByResourceId(rid)
        if not (row):
            return jsonify(Error="No supplier found."), 404
        result = self.build_supplier_dict(row)
        return jsonify(Supplier=result)

    def add_resource(self, form):
        rName = form['rName']
        rcid = form[
            'rcid']  # this will probably be replaced by category name, followed by a lookup of rcid with respect to its name
        # the attributes below are for the insertion into the resoruce details table
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
        rcid = form[
            'rcid']  # this will probably be replaced by category name, followed by a lookup of rcid with respect to its name
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
        if not (resources_list):
            return jsonify(Error="No requested resources found"), 404
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def get_dispatched_requested_resources(self):
        dao = ResourcesDAO()
        resources_list = dao.getRequestedResourcesDispatched()
        if not (resources_list):
            return jsonify(Error="No dispatched requested resources found"), 404
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def get_undispatched_requested_resources(self):
        dao = ResourcesDAO()
        resources_list = dao.getRequestedResourcesUndispatched()
        if not (resources_list):
            return jsonify(Error="No undispatched requested resources found"), 404
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
