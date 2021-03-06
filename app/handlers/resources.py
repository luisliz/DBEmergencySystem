import datetime
import simplejson
from flask import jsonify
from app.dao.resources import ResourcesDAO
from app.dao.resource_details import ResourceDetailsDAO
from app.handlers.transaction import TransactionHandler
from app.handlers.categories import CategoryHandler


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
        self.all_tables = {
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

    def build_resource_dict(self, columns, row):
        col = columns.copy()
        for c in range(len(col)):
            col[c] = col[c][0]

        col += ['rid', 'rname', 'rquantity', 'rlocation', 'ravailability', 'supplieruid', 'rprice']
        result = {}
        for i in range(len(col)):
            result[col[i]] = row[i]
        return result

    # def build_details_dict(self, row):
    #     result = {}
    #     result['rdid'] = row[0]
    #     result['rquantity'] = row[1]
    #     result['rlocation'] = row[2]
    #     result['ravailability'] = row[3]
    #     result['supplieruid'] = row[4]
    #     result['rprice'] = row[5]
    #
    #     return result

    def build_supplier_dict(self, row):
        result = {}
        result['supplierID'] = row[0]
        result['firstname'] = row[1]
        result['lastname'] = row[2]
        return result

    def get_all_resources(self):
        dao = ResourcesDAO()
        result_list = []
        for table in self.all_tables:
            columns = self.getcol.get(table, [])
            resources_list = self.all_tables.get(table, [])
            for row in resources_list:
                result = self.build_resource_dict(columns, row)
                result_list.append(result)
        return jsonify(Resources=result_list)

    def get_all_available_resources(self):
        dao = ResourcesDAO()

        all_tables_avail = {
            'baby_foods': dao.getAllAvailBabyFoods(),
            'ices': dao.getAllAvailIces(),
            'fuels': dao.getAllAvailFuels(),
            'heavy_equipments': dao.getAllAvailHeavyEquipments(),
            'tools': dao.getAllAvailTools(),
            'medications': dao.getAllAvailMedications(),
            "power_generators": dao.getAllAvailPowerGenerators(),
            'waters': dao.getAllAvailWaters(),
            'medical_devices': dao.getAllAvailMedicalDevices(),
            'batteries': dao.getAllAvailBatteries(),
            'canned_foods': dao.getAllAvailCannedFoods(),
            'dry_foods': dao.getAllAvailDryFoods(),
            'clothings': dao.getAllAvailClothings()
        }

        result_list = []
        for table in all_tables_avail:
            columns = self.getcol.get(table, [])
            resources_list = all_tables_avail.get(table, [])
            for row in resources_list:
                result = self.build_resource_dict(columns, row)
                result_list.append(result)
        return jsonify(Resources=result_list)

    def get_all_available_resources_by_name(self, rname):
        dao = ResourcesDAO()

        all_tables_avail_by_name = {
            'baby_foods': dao.getAllAvailBabyFoodsByName(rname),
            'ices': dao.getAllAvailIcesByName(rname),
            'fuels': dao.getAllAvailFuelsByName(rname),
            'heavy_equipments': dao.getAllAvailHeavyEquipmentsByName(rname),
            'tools': dao.getAllAvailToolsByName(rname),
            'medications': dao.getAllAvailMedicationsByName(rname),
            "power_generators": dao.getAllAvailPowerGeneratorsByName(rname),
            'waters': dao.getAllAvailWatersByName(rname),
            'medical_devices': dao.getAllAvailMedicalDevicesByName(rname),
            'batteries': dao.getAllAvailBatteriesByName(rname),
            'canned_foods': dao.getAllAvailCannedFoodsByName(rname),
            'dry_foods': dao.getAllAvailDryFoodsByName(rname),
            'clothings': dao.getAllAvailClothingsByName(rname)
        }

        result_list = []
        for table in all_tables_avail_by_name:
            columns = self.getcol.get(table, [])
            resources_list = all_tables_avail_by_name.get(table, [])
            for row in resources_list:
                result = self.build_resource_dict(columns, row)
                result_list.append(result)
        return jsonify(Resources=result_list)

    def getDayStatistics(self):
        dao = ResourcesDAO()
        countR = dao.countRequestsPerDay()
        resDayP = dao.countResourcesPerDay('purchased')
        resDayR = dao.countResourcesPerDay('reserved')
        dispatchedP = dao.countResourcesDispatchedPerDay('purchased')
        dispatchedR = dao.countResourcesDispatchedPerDay('reserved')
        averageP = dao.countAverageResourcesPerOrderPerDay('purchased')
        averageR = dao.countAverageResourcesPerOrderPerDay('reserved')
        # averageResourcesPerOrder

        res = {}
        data = {
            'requestsCount': 0,
            'resourcesPurchased': 0,
            'resourcesReserved': 0,
            'purchasesDispatched': 0,
            'reservedDispatched': 0,
            'averageResourcesPurchasedPerOrder': 0.0,
            'averageResourcesReservedPerOrder': 0.0,
        }

        for row in countR:
            post = row[0].strftime('%Y-%m-%d')
            if post not in res:
                res[post] = data.copy()
                res[post]['requestsCount'] += row[1]
            else:
                res[post]['requestsCount'] += row[1]

        for row in resDayP:
            post = row[0].strftime('%Y-%m-%d')
            if post not in res:
                res[post] = data.copy()
                res[post]['resourcesPurchased'] += row[1]
            else:
                res[post]['resourcesPurchased'] += row[1]

        for row in resDayR:
            post = row[0].strftime('%Y-%m-%d')
            if post not in res:
                res[post] = data.copy()
                res[post]['resourcesReserved'] += row[1]
            else:
                res[post]['resourcesReserved'] += row[1]

        for row in dispatchedP:
            post = row[0].strftime('%Y-%m-%d')
            if post not in res:
                res[post] = data.copy()
                res[post]['purchasesDispatched'] += row[1]
            else:
                res[post]['purchasesDispatched'] += row[1]

        for row in dispatchedR:
            post = row[0].strftime('%Y-%m-%d')
            if post not in res:
                res[post] = data.copy()
                res[post]['reservedDispatched'] += row[1]
            else:
                res[post]['reservedDispatched'] += row[1]

        for row in averageP:
            post = row[0].strftime('%Y-%m-%d')
            if post not in res:
                res[post] = data.copy()
                res[post]['averageResourcesPurchasedPerOrder'] = float(row[1])
            else:
                res[post]['averageResourcesPurchasedPerOrder'] = float(row[1])

        for row in averageR:
            post = row[0].strftime('%Y-%m-%d')
            if post not in res:
                res[post] = data.copy()
                res[post]['averageResourcesReservedPerOrder'] = float(row[1])
            else:
                res[post]['averageResourcesReservedPerOrder'] = float(row[1])

        return jsonify(Request=res)


    def get_requested_resources_by_name(self, rname):
        dao = ResourcesDAO()

        all_tables_requested_by_rname = {
            'baby_foods': dao.getReqBabyFoodsByName(rname),
            'ices': dao.getReqIcesByName(rname),
            'fuels': dao.getReqFuelsByName(rname),
            'heavy_equipments': dao.getReqHeavyEquipmentsByName(rname),
            'tools': dao.getReqToolsByName(rname),
            'medications': dao.getReqMedicationsByName(rname),
            "power_generators": dao.getReqPowerGeneratorsByName(rname),
            'waters': dao.getReqWatersByName(rname),
            'medical_devices': dao.getReqMedicalDevicesByName(rname),
            'batteries': dao.getReqBatteriesByName(rname),
            'canned_foods': dao.getReqCannedFoodsByName(rname),
            'dry_foods': dao.getReqDryFoodsByName(rname),
            'clothings': dao.getReqClothingsByName(rname)
        }

        result_list = []
        for table in all_tables_requested_by_rname:
            columns = self.getcol.get(table, [])
            resources_list = all_tables_requested_by_rname.get(table, [])
            for row in resources_list:
                result = self.build_resource_dict(columns, row)
                result_list.append(result)
        return jsonify(Resources=result_list)


    def get_resources_by_category(self, category):
        dao = ResourcesDAO()
        columns = self.getcol.get(category, [])
        if not columns:
            return jsonify(Error="Category not found"), 404
        else:
            resources_list = self.all_tables.get(category, [])
            if not (resources_list):
                return jsonify(Error="No resources found :("), 404
            result_list = []
            for row in resources_list:
                result = self.build_resource_dict(columns, row)
                result_list.append(result)
            return jsonify(Resources=result_list)


    def get_resources_by_category_field(self, category, afield, value):
        dao = ResourcesDAO()
        columns = self.getcol.get(category, [])
        if not columns:
            return jsonify(Error="Category not found"), 404
        else:
            field = ''
            for i in columns:
                if afield == i[0]:
                    field = afield

            if field == '':
                return jsonify(Error="Fields not found", Categories=columns), 404
            else:
                resources_list = dao.filterCategoryByField(category, field, value)
                if resources_list == []:
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
        actualcat_tuple = dao.getCategoryNameByRID(rid)
        if not (actualcat_tuple):
            return jsonify(Error="No resources found for that id"), 404
        actualcat = actualcat_tuple[0]
        # print("actualcat = %s" % actualcat)
        columns = self.getcol.get(actualcat, [])

        # this section is to get the row for the resource
        resources = {
            'baby_foods': dao.getBabyFoodsByRID(rid),
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
        row = resources.get(actualcat, [])  # in this case, this is just a tuple
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

    def add_resource(self, form):
        print(form)
        catHandler = CategoryHandler()

        if len(form) < 6:
            return jsonify(Error = "Malformed post request, not enough parameters"), 400
        else:           
            cat_id = 1 #remove this once all categories are dealt with 
            rName = form['rname']
            if (form['rname'] == 'medications'):
                mid = catHandler.add_medications(form)
            else: mid = None
            if (form['rname'] == 'canned_foods'):
                canid = catHandler.add_canned_foods(form)
            else: canid = None
            if (form['rname'] == 'baby_foods'):
                bid = catHandler.add_baby_foods(form)
            else: bid = None
            if (form['rname'] == 'dry_foods'):
                dryid = catHandler.add_dry_foods(form)
            else: dryid = None
            if (form['rname'] == 'fuels'):
                fid = catHandler.add_fuels(form)
            else: fid = None
            if (form['rname'] == 'heavy_equipments'):
                hid = catHandler.add_heavy_equipments(form)
            else: hid = None
            if (form['rname'] == 'clothings'):
                clothid = catHandler.add_clothings(form)
            else: clothid = None
            if (form['rname'] == 'power_generators'):
                genid = catHandler.add_power_generators(form)
            else: genid = None
            if (form['rname'] == 'medical_devices'):
                meddevid = catHandler.add_medical_devices(form)
            else: meddevid = None
            if (form['rname'] == 'batteries'):
                batid = catHandler.add_batteries(form)
            else: batid = None
            if (form['rname'] == 'tools'):
                toolid = catHandler.add_tools(form)
            else: toolid = None
            if (form['rname'] == 'ices'):
                iid = catHandler.add_ices(form)
            else: iid = None
            if (form['rname'] == 'waters'):
                wid = catHandler.add_waters(form)
            else: wid = None

            rdQuantity = form['rquantity']
            rdLocation = form['rlocation']
            rdAvailability = form['ravailability']
            supplierID = form['supplieruid']
            price_per_unit = form['rprice'] 

            if (rName):
                daoR = ResourcesDAO()
                daoRD = ResourceDetailsDAO()
                rid = daoR.insert(rName, mid, canid, bid, dryid, fid, hid, clothid, genid, meddevid, batid, toolid, iid, wid)
                daoRD.insert(rid, rdQuantity, rdLocation, rdAvailability, supplierID, price_per_unit)
                return jsonify(Resource_Id=rid), 201
            else:
                return jsonify(Error="Unexpected resource attributes in resource post request"), 400

            

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


    def reserve_resource(self, rid, status, form):
        dao = ResourceDetailsDAO()
        result = dao.updateAvailability(rid, status)

        transactionHandler = TransactionHandler()
        transactionHandler.insertTransaction(form, rid)

        return jsonify(Reserved=result)


    def purchase_resource(self, rid, status, form):
        dao = ResourceDetailsDAO()

        # Adding compatibility with transaction
        transactionHandler = TransactionHandler()
        transactionHandler.insertTransaction(form, rid)

        result = dao.updateAvailability(rid, status)
        return jsonify(Reserved=result)
