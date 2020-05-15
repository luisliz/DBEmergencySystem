from app.config.database_config import pg_config
import psycopg2


# TODO: see what routes can get grouped together, group them
# TODO: see what parameters can be body args, change
# TODO: aggregate queries de P2
# TODO: revisa that u meet all spec reqs

class ResourcesDAO:

    def __init__(self):
        self.conn = psycopg2.connect(
            user=pg_config["user"],
            password=pg_config['passwd'],
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database']
        )

        # variable to hold select * from resources + resource_details query
        self.allrplusrd = "select * from resources;"  # distinct r.rid, r.rname, rd.rdid, rd.rquantity, rd.rlocation, rd.ravailability, rd.supplieruid, rd.rprice from resources as r inner join resource_details as rd on r.rid = rd.rid "

        # self.resources = [
        #     {
        #         'rid': 1,
        #         'rName': 'Water',
        #         'rcId': 1
        #     },
        #     {
        #         'rid': 2,
        #         'rName': 'Cannabis',
        #         'rcId': 2
        #     },
        #     {
        #         'rid': 3,
        #         'rName': 'Chef Boyardee',
        #         'rcId': 3
        #     },
        #     {
        #         'rid': 4,
        #         'rName': 'Tylenol',
        #         'rcId': 2
        #     }
        # ]

    def getCategoryNameByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select rname from resources where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    # =============================================================================================================
    # =========================================== All In Category Field ===========================================
    # =============================================================================================================
    def getAllBabyFoods(self):
        cursor = self.conn.cursor()
        query = "select bid, bflavor, bbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join baby_foods;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllIces(self):
        cursor = self.conn.cursor()
        query = "select iid, ibrand, ibagsize, iweight, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join ices;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllFuels(self):
        cursor = self.conn.cursor()
        query = "SELECT fid, fbrand, ftype, fvolume, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join fuels;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllHeavyEquipments(self):
        cursor = self.conn.cursor()
        query = "select hid, hbrand, htype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join heavy_equipments;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllTools(self):
        cursor = self.conn.cursor()
        query = "SELECT toolid, toolbrand, tooltype, toolsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join tools;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMedications(self):
        cursor = self.conn.cursor()
        query = "SELECT mid, mmanufacturer, msize, mname, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medications;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllPowerGenerators(self):
        cursor = self.conn.cursor()
        query = "SELECT genid, genbrand, gentype, genpower, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join power_generators;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllWaters(self):
        cursor = self.conn.cursor()
        query = "SELECT wid, wcontainertype, wcontainersize, wbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join waters;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllMedicalDevices(self):
        cursor = self.conn.cursor()
        query = "SELECT meddevid, meddevbrand, meddevtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medical_devices;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllBatteries(self):
        cursor = self.conn.cursor()
        query = "select batid, battype, batsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join batteries;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllCannedFoods(self):
        cursor = self.conn.cursor()
        query = "select canid, canbrand, cantype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join canned_foods;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllDryFoods(self):
        cursor = self.conn.cursor()
        query = "select dryid, drybrand, drytype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join dry_foods;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllClothings(self):
        cursor = self.conn.cursor()
        query = "select clothid, clothbranch, clothmaterial, clothtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join clothings;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # =============================================================================================================
    # =========================================== get all resources requested by rname ============================
    # =============================================================================================================

    def getReqBabyFoodsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select bid, bflavor, bbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join baby_foods natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqIcesByName(self, rname):
        cursor = self.conn.cursor()
        query = "select iid, ibrand, ibagsize, iweight, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join ices natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqFuelsByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT fid, fbrand, ftype, fvolume, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join fuels natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqHeavyEquipmentsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select hid, hbrand, htype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join heavy_equipments natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqToolsByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT toolid, toolbrand, tooltype, toolsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join tools natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqMedicationsByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT mid, mmanufacturer, msize, mname, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medications natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqPowerGeneratorsByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT genid, genbrand, gentype, genpower, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join power_generators natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqWatersByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT wid, wcontainertype, wcontainersize, wbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join waters natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqMedicalDevicesByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT meddevid, meddevbrand, meddevtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medical_devices natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqBatteriesByName(self, rname):
        cursor = self.conn.cursor()
        query = "select batid, battype, batsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join batteries natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqCannedFoodsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select canid, canbrand, cantype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join canned_foods natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqDryFoodsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select dryid, drybrand, drytype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join dry_foods natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getReqClothingsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select clothid, clothbranch, clothmaterial, clothtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join clothings natural inner join resources_per_request where rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #==============================================================================================================
    #========================================== get all available resources =======================================
    #==============================================================================================================

    def getAllAvailBabyFoods(self):
        cursor = self.conn.cursor()
        query = "select bid, bflavor, bbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join baby_foods where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailIces(self):
        cursor = self.conn.cursor()
        query = "select iid, ibrand, ibagsize, iweight, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join ices where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailFuels(self):
        cursor = self.conn.cursor()
        query = "SELECT fid, fbrand, ftype, fvolume, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join fuels where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailHeavyEquipments(self):
        cursor = self.conn.cursor()
        query = "select hid, hbrand, htype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join heavy_equipments where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailTools(self):
        cursor = self.conn.cursor()
        query = "SELECT toolid, toolbrand, tooltype, toolsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join tools where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailMedications(self):
        cursor = self.conn.cursor()
        query = "SELECT mid, mmanufacturer, msize, mname, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medications where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailPowerGenerators(self):
        cursor = self.conn.cursor()
        query = "SELECT genid, genbrand, gentype, genpower, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join power_generators where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailWaters(self):
        cursor = self.conn.cursor()
        query = "SELECT wid, wcontainertype, wcontainersize, wbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join waters where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailMedicalDevices(self):
        cursor = self.conn.cursor()
        query = "SELECT meddevid, meddevbrand, meddevtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medical_devices where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailBatteries(self):
        cursor = self.conn.cursor()
        query = "select batid, battype, batsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join batteries where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailCannedFoods(self):
        cursor = self.conn.cursor()
        query = "select canid, canbrand, cantype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join canned_foods where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailDryFoods(self):
        cursor = self.conn.cursor()
        query = "select dryid, drybrand, drytype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join dry_foods where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailClothings(self):
        cursor = self.conn.cursor()
        query = "select clothid, clothbranch, clothmaterial, clothtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join clothings where ravailability = 'available';"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ==============================================================================================================
    # ========================================== get all available resources by name ===============================
    # ==============================================================================================================

    def getAllAvailBabyFoodsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select bid, bflavor, bbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join baby_foods where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailIcesByName(self, rname):
        cursor = self.conn.cursor()
        query = "select iid, ibrand, ibagsize, iweight, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join ices where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query,(rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailFuelsByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT fid, fbrand, ftype, fvolume, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join fuels where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailHeavyEquipmentsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select hid, hbrand, htype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join heavy_equipments where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailToolsByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT toolid, toolbrand, tooltype, toolsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join tools where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailMedicationsByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT mid, mmanufacturer, msize, mname, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medications where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailPowerGeneratorsByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT genid, genbrand, gentype, genpower, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join power_generators where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailWatersByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT wid, wcontainertype, wcontainersize, wbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join waters where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailMedicalDevicesByName(self, rname):
        cursor = self.conn.cursor()
        query = "SELECT meddevid, meddevbrand, meddevtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medical_devices where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailBatteriesByName(self, rname):
        cursor = self.conn.cursor()
        query = "select batid, battype, batsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join batteries where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailCannedFoodsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select canid, canbrand, cantype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join canned_foods where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailDryFoodsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select dryid, drybrand, drytype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join dry_foods where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllAvailClothingsByName(self, rname):
        cursor = self.conn.cursor()
        query = "select clothid, clothbranch, clothmaterial, clothtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join clothings where ravailability = 'available' and rname = %s order by rname;"
        cursor.execute(query, (rname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # =============================================================================================================
    # =========================================== Filter Category Field ===========================================
    # =============================================================================================================
    def filterCategoryByField(self, category, field, value):
        cursor = self.conn.cursor()
        where = {
            'baby_foods': {

                'bid': "select bid, bflavor, bbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join baby_foods where bid = %s;",
                'bflavor': "select bid, bflavor, bbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join baby_foods where bflavor = %s;",
                'bbrand': "select bid, bflavor, bbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join baby_foods where bbrand = %s;",
            },
            'power_generators': {
                'genid': "SELECT genid, genbrand, gentype, genpower, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join power_generators where genid = %s;",
                'genbrand': "SELECT genid, genbrand, gentype, genpower, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join power_generators where genbrand = %s;",
                'gentype': "SELECT genid, genbrand, gentype, genpower, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join power_generators where gentype = %s;",
                'genpower': "SELECT genid, genbrand, gentype, genpower, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join power_generators where genpower = %s;",
            },
            'ices': {
                'iid': "select iid, ibrand, ibagsize, iweight, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join ices where iid = %s;",
                'ibrand': "select iid, ibrand, ibagsize, iweight, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join ices where ibrand = %s;",
                'ibagsize': "select iid, ibrand, ibagsize, iweight, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join ices where ibagsize = %s;",
                'iweight': "select iid, ibrand, ibagsize, iweight, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join ices where iweight = %s;",
            },
            'fuels': {
                'fid': "SELECT fid, fbrand, ftype, fvolume, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join fuels where fid = %s;",
                'fbrand': "SELECT fid, fbrand, ftype, fvolume, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join fuels where fbrand = %s;",
                'ftype': "SELECT fid, fbrand, ftype, fvolume, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join fuels where ftype = %s;",
                'fvolume': "SELECT fid, fbrand, ftype, fvolume, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join fuels where fvolume = %s;",
            },
            'heavy_equipments': {
                'hid': "select hid, hbrand, htype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join heavy_equipments where hid = %s;",
                'hbrand': "select hid, hbrand, htype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join heavy_equipments where hbrand = %s;",
                'htype': "select hid, hbrand, htype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join heavy_equipments where htype = %s;",
            },
            'tools': {
                'toolid': "SELECT toolid, toolbrand, tooltype, toolsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join tools where toolid = %s;",
                'toolbrand': "SELECT toolid, toolbrand, tooltype, toolsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join tools where toolbrand = %s;",
                'tooltype': "SELECT toolid, toolbrand, tooltype, toolsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join tools where tooltype = %s;",
                'toolsize': "SELECT toolid, toolbrand, tooltype, toolsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join tools where toolsize = %s;",
            },
            'medications': {
                'mid': "SELECT mid, mmanufacturer, msize, mname, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medications where mid = %s;",
                'mmanufacturer': "SELECT mid, mmanufacturer, msize, mname, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medications where mmanufacturer = %s;",
                'msize': "SELECT mid, mmanufacturer, msize, mname, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medications where msize = %s;",
                'mname': "SELECT mid, mmanufacturer, msize, mname, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medications where mname = %s;",
            },
            'batteries': {
                'batid': "select batid, battype, batsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join batteries where batid = %s;",
                'battype': "select batid, battype, batsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join batteries where battype = %s;",
                'batsize': "select batid, battype, batsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join batteries where batsize = %s;",
            },
            'waters': {
                'wid': "SELECT wid, wcontainertype, wcontainersize, wbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join waters where wid = %s;",
                'wcontainertype': "SELECT wid, wcontainertype, wcontainersize, wbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join waters where wcontainertype = %s;",
                'wcontainersize': "SELECT wid, wcontainertype, wcontainersize, wbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join waters where wcontainersize = %s;",
                'wbrand': "SELECT wid, wcontainertype, wcontainersize, wbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join waters where wbrand = %s;",
            },
            'medical_devices': {
                'meddevid': "SELECT meddevid, meddevbrand, meddevtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medical_devices where meddevid = %s;",
                'meddevbrand': "SELECT meddevid, meddevbrand, meddevtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medical_devices where meddevbrand = %s;",
                'meddevtype': "SELECT meddevid, meddevbrand, meddevtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medical_devices where meddevtype = %s;",
            },
            'canned_foods': {
                'canid': "select canid, canbrand, cantype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join canned_foods where canid = %s;",
                'canbrand': "select canid, canbrand, cantype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join canned_foods where canbrand = %s;",
                'cantype': "select canid, canbrand, cantype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join canned_foods where cantype = %s;",
            },
            'dry_foods': {
                'dryid': "select dryid, drybrand, drytype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join dry_foods where dryid = %s;",
                'drybrand': "select dryid, drybrand, drytype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join dry_foods where drybrand = %s;",
                'drytype': "select dryid, drybrand, drytype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join dry_foods where drytype = %s;",
            },
            'clothings': {
                'clothid': "select clothid, clothbranch, clothmaterial, clothtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join clothings where clothid = %s;",
                'clothbranch': "select clothid, clothbranch, clothmaterial, clothtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join clothings where clothbranch = %s;",
                'clothmaterial': "select clothid, clothbranch, clothmaterial, clothtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join clothings where clothmaterial = %s;",
                'clothtype': "select clothid, clothbranch, clothmaterial, clothtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join clothings where clothtype = %s;",
            },
        }

        query = where[category][field]
        cursor.execute(query, (value,))
        if (cursor.rowcount == 0):
            return []
        else:
            result = []
            for row in cursor:
                result.append(row)
            return result

    # methods to get resources + cat info from a given rid
    ####################################################################################
    def getBabyFoodsByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select bid, bflavor, bbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join baby_foods where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getIcesByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select iid, ibrand, ibagsize, iweight, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join ices where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getFuelsByRID(self, rid):
        cursor = self.conn.cursor()
        query = "SELECT fid, fbrand, ftype, fvolume, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join fuels where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getHeavyEquipmentsByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select hid, hbrand, htype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join heavy_equipments where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getToolsByRID(self, rid):
        cursor = self.conn.cursor()
        query = "SELECT toolid, toolbrand, tooltype, toolsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join tools where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getMedicationsByRID(self, rid):
        cursor = self.conn.cursor()
        query = "SELECT mid, mmanufacturer, msize, mname, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medications where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getPowerGeneratorsByRID(self, rid):
        cursor = self.conn.cursor()
        query = "SELECT genid, genbrand, gentype, genpower, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join power_generators where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getWatersByRID(self, rid):
        cursor = self.conn.cursor()
        query = "SELECT wid, wcontainertype, wcontainersize, wbrand, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join waters where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getMedicalDevicesByRID(self, rid):
        cursor = self.conn.cursor()
        query = "SELECT meddevid, meddevbrand, meddevtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join medical_devices where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getBatteriesByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select batid, battype, batsize, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join batteries where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getCannedFoodsByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select canid, canbrand, cantype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join canned_foods where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getDryFoodsByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select dryid, drybrand, drytype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join dry_foods where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getClothingsByRID(self, rid):
        cursor = self.conn.cursor()
        query = "select clothid, clothbranch, clothmaterial, clothtype, rid, rname, rquantity, rlocation, ravailability, supplieruid, rprice from resources natural inner join resource_details natural inner join clothings where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result
    ####################################################################################

    # def getAllResources(self):
    #     cursor = self.conn.cursor()
    #     query = self.allrplusrd
    #     cursor.execute(query)
    #     result = []  # this is a 'table', a list of lists: result[0][0] --> first row, value in first col
    #     for row in cursor:
    #         result.append(row)
    #     return result

    def getResourceColumns(self, resource):
        cursor = self.conn.cursor()
        query = "SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = %s;"
        cursor.execute(query, (resource,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResources(self):
        cursor = self.conn.cursor()
        # query = "select distinct r.rid, r.rname, r.rcid, rd.rdid, rd.rquantity, rd.rlocation, rd.ravailability, rd.supplieruid, rd.rprice from resources as r inner join resource_details as rd on r.rid = rd.rid inner join requests as req on r.rid = req.rid;"
        query = self.allrplusrd + "inner join requests as req on r.rid = req.rid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResourcesUndispatched(self):
        cursor = self.conn.cursor()
        query = self.allrplusrd + "inner join requests as req on r.rid = req.rid where req.reqdispatchdate is null;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResourcesDispatched(self):
        cursor = self.conn.cursor()
        query = self.allrplusrd + "inner join requests as req on r.rid = req.rid where req.reqdispatchdate is not null;"  # might be problematix
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestedResourceById(self, rid):
        cursor = self.conn.cursor()
        query = self.allrplusrd + "inner join requests as req on r.rid = req.rid where r.rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        #query = self.allrplusrd + "where r.rid = %s;"OLD
        query = self.allrplusrd[:-1] + " where rid = %s;" #NEW
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getResourceByName(self, rName):  # Done
        cursor = self.conn.cursor()
        query = self.allrplusrd + "where rName ilike '" + rName + "%';"
        # query = "select * from resources where rName ilike %s%%;"
        # cursor.execute(query, (rName,))
        cursor.execute(query)
        result = cursor.fetchone()
        return result

    def getResourcesByCategory(self, category):  # Done
        cursor = self.conn.cursor()
        query = self.allrplusrd + "natural inner join resource_category where rcName = %s;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByAvailability(self, avail):  # Done
        cursor = self.conn.cursor()
        query = "SELECT rid from resource_details where ravailability = 'available';"
        cursor.execute(query, (avail,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByResourceId(self, rid):  # Done
        cursor = self.conn.cursor()
        query = "select * from users inner join resource_details on supplieruid = uid where rid = %s"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    #def getDayStatistics(self):
    #    cursor = self.conn.cursor()
    #    query = "SELECT reqid, reqpostdate, reqdispatchdate, rlocation, reqlocation, requestuid, rd.supplieruid, r.r#id, reqquantity, rname FROM requests NATURAL JOIN resources_per_request JOIN resources r on res#ources_per_request.rid = r.rid JOIN resource_details rd on r.rid = rd.rid WHERE rd.ravailability = 'available';;"
    #    cursor.execute(query)
    #     result = cursor.fetchall()
        # return result

    # -------------------------------------------------------------------------------------------------------------
    # ------------------------------------------------- Statistics ------------------------------------------------
    # -------------------------------------------------------------------------------------------------------------
    def countRequestsPerDay(self):
        cursor = self.conn.cursor()
        query = "SELECT reqpostdate, COUNT(rq.reqid) FROM requests AS rq GROUP BY rq.reqpostdate;"
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def countResourcesPerDay(self, orderType):
        cursor = self.conn.cursor()
        query = "SELECT reqpostdate, COUNT(rpq.rid) FROM requests AS rq JOIN resources_per_request rpq ON rpq.reqid = rq.reqid JOIN resource_details rd on rpq.rid = rd.rid WHERE rd.ravailability = %s GROUP BY rq.reqpostdate;"
        cursor.execute(query, (orderType,))
        result = cursor.fetchall()
        return result

    def countResourcesDispatchedPerDay(self, orderType):
        cursor = self.conn.cursor()
        query = "SELECT reqdispatchdate, COUNT(rpq.rid) FROM requests AS rq JOIN resources_per_request rpq ON rpq.reqid = rq.reqid JOIN resource_details rd on rpq.rid = rd.rid WHERE rd.ravailability = %s AND rq.reqdispatchdate IS NOT NULL GROUP BY rq.reqdispatchdate;"
        cursor.execute(query, (orderType,))
        result = cursor.fetchall()
        return result

    def countAverageResourcesPerOrderPerDay(self, orderType):
        cursor = self.conn.cursor()
        query = "SELECT reqpostdate, avg(ridCount) FROM (SELECT rq.reqpostdate, COUNT(rpq.rid) AS ridCount FROM requests AS rq JOIN resources_per_request rpq ON rpq.reqid = rq.reqid JOIN resource_details rd on rpq.rid = rd.rid WHERE rd.ravailability = %s GROUP BY rq.reqpostdate) as counter GROUP BY reqpostdate;"
        cursor.execute(query, (orderType,))
        result = cursor.fetchall()
        return result

    def averageResourcesPerOrder(self,orderType):
        cursor = self.conn.cursor()
        query = "SELECT avg(ridCount) FROM (SELECT COUNT(rpq.rid) AS ridCount FROM requests AS rq JOIN resources_per_request rpq ON rpq.reqid = rq.reqid JOIN resource_details rd on rpq.rid = rd.rid WHERE rd.ravailability = %s GROUP BY rq.reqid) as counter;"
        cursor.execute(query, (orderType,))
        result = cursor.fetchall()
        return result

    def insert(self, rName, mid, canid, bid, dryid, fid, hid, clothid, genid, meddevid, batid, toolid, iid, wid):
        cursor = self.conn.cursor()
        query = "insert into resources (rname, mid, canid, bid, dryid, fid, hid, clothid, genid, meddevid, batid, toolid, iid, wid) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rName, mid, canid, bid, dryid, fid, hid, clothid, genid, meddevid, batid, toolid, iid, wid))
        self.conn.commit()
        return cursor.fetchone()[0] #returns rid 

    # NEEDS TESTING ********
    def insertMedications(self, mmanufacturer, mname, msize):
        cursor = self.conn.cursor()
        query = "insert into medications (mmanufacturer, mname, msize) VALUES (%s, %s, %s) returning mid;"
        cursor.execute(query, (mmanufacturer, mname, msize))
        self.conn.commit()
        return cursor.fetchone()[0]

    # NEEDS TESTING ********
    def insertCannedFoods(self, canbrand, cantype):
        cursor = self.conn.cursor()
        query = "insert into canned_foods (canbrand, cantype) VALUES (%s, %s) returning canid;"
        cursor.execute(query, (canbrand, cantype))
        self.conn.commit()
        return cursor.fetchone()[0]

    # NEEDS TESTING ********
    def insertBabyFoods(self, bflavor, bbrand):
        cursor = self.conn.cursor()
        query = "insert into baby_foods (bflavor, bbrand) VALUES (%s, %s) returning bid;"
        cursor.execute(query, (bflavor, bbrand))
        self.conn.commit()
        return cursor.fetchone()[0]

    # NEEDS TESTING ********
    def insertDryFoods(self, drybrand, drytype):
        cursor = self.conn.cursor()
        query = "insert into dry_foods (drybrand, drytype) VALUES (%s, %s) returning dryid;"
        cursor.execute(query, (drybrand, drytype))
        self.conn.commit()
        return cursor.fetchone()[0]

    def insertIces(self, ibrand, ibagsize, iweight):
        cursor = self.conn.cursor()
        query = "insert into ices (ibrand, ibagsize, iweight) VALUES (%s, %s, %s) returning iid;"
        cursor.execute(query, (ibrand, ibagsize, iweight))
        self.conn.commit()
        return cursor.fetchone()[0]

    
    def insertFuels(self, ftype, fbrand, fvolume):
        cursor = self.conn.cursor()
        query = "insert into fuels (ftype, fbrand, fvolume) VALUES (%s, %s, %s) returning fid;"
        cursor.execute(query, (ftype, fbrand, fvolume))
        self.conn.commit()
        return cursor.fetchone()[0]

    # NEEDS TESTING ********
    def insertHeavyEquipments(self, hbrand, htype):
        cursor = self.conn.cursor()
        query = "insert into heavy_equipments (hbrand, htype) VALUES (%s, %s) returning hid;"
        cursor.execute(query, (hbrand, htype))
        self.conn.commit()
        return cursor.fetchone()[0]

    # NEEDS TESTING ********
    def insertClothings(self, clothbrand, clothmaterial, clothtype):
        cursor = self.conn.cursor()
        query = "insert into clothings (clothbrand, clothmaterial, clothtype) VALUES (%s, %s, %s) returning clothid;"
        cursor.execute(query, (clothbrand, clothmaterial, clothtype))
        self.conn.commit()
        return cursor.fetchone()[0]

    # NEEDS TESTING ********
    def insertPowerGenerators(self, genbrand, genpower, gentype):
        cursor = self.conn.cursor()
        query = "insert into power_generators (genbrand, genpower, gentype) VALUES (%s, %s, %s) returning genid;"
        cursor.execute(query, (genbrand, genpower, gentype))
        self.conn.commit()
        return cursor.fetchone()[0]

    # def insertBabyFoods(self, bflavor, bbrand):
    #     cursor = self.conn.cursor()
    #     query = "insert into baby_foods (bflavor, bbrand) VALUES (%s, %s) returning bid;"
    #     cursor.execute(query, (bflavor, bbrand))
    #     self.conn.commit()
    #     return cursor.fetchone()[0]

    # def insertBabyFoods(self, bflavor, bbrand):
    #     cursor = self.conn.cursor()
    #     query = "insert into baby_foods (bflavor, bbrand) VALUES (%s, %s) returning bid;"
    #     cursor.execute(query, (bflavor, bbrand))
    #     self.conn.commit()
    #     return cursor.fetchone()[0]

    # def insertBabyFoods(self, bflavor, bbrand):
    #     cursor = self.conn.cursor()
    #     query = "insert into baby_foods (bflavor, bbrand) VALUES (%s, %s) returning bid;"
    #     cursor.execute(query, (bflavor, bbrand))
    #     self.conn.commit()
    #     return cursor.fetchone()[0]

    # def insertBabyFoods(self, bflavor, bbrand):
    #     cursor = self.conn.cursor()
    #     query = "insert into baby_foods (bflavor, bbrand) VALUES (%s, %s) returning bid;"
    #     cursor.execute(query, (bflavor, bbrand))
    #     self.conn.commit()
    #     return cursor.fetchone()[0]

    # def insertBabyFoods(self, bflavor, bbrand):
    #     cursor = self.conn.cursor()
    #     query = "insert into baby_foods (bflavor, bbrand) VALUES (%s, %s) returning bid;"
    #     cursor.execute(query, (bflavor, bbrand))
    #     self.conn.commit()
    #     return cursor.fetchone()[0]

    # def insertBabyFoods(self, bflavor, bbrand):
    #     cursor = self.conn.cursor()
    #     query = "insert into baby_foods (bflavor, bbrand) VALUES (%s, %s) returning bid;"
    #     cursor.execute(query, (bflavor, bbrand))
    #     self.conn.commit()
    #     return cursor.fetchone()[0]

    # def insertBabyFoods(self, bflavor, bbrand):
    #     cursor = self.conn.cursor()
    #     query = "insert into baby_foods (bflavor, bbrand) VALUES (%s, %s) returning bid;"
    #     cursor.execute(query, (bflavor, bbrand))
    #     self.conn.commit()
    #     return cursor.fetchone()[0]

    # def insertBabyFoods(self, bflavor, bbrand):
    #     cursor = self.conn.cursor()
    #     query = "insert into baby_foods (bflavor, bbrand) VALUES (%s, %s) returning bid;"
    #     cursor.execute(query, (bflavor, bbrand))
    #     self.conn.commit()
    #     return cursor.fetchone()[0]

    # def insertBabyFoods(self, bflavor, bbrand):
    #     cursor = self.conn.cursor()
    #     query = "insert into baby_foods (bflavor, bbrand) VALUES (%s, %s) returning bid;"
    #     cursor.execute(query, (bflavor, bbrand))
    #     self.conn.commit()
    #     return cursor.fetchone()[0]

    def delete(self, rid):
        pos = 0
        for res in self.resources:
            if int(res['rid']) == int(rid):
                del self.resources[pos]
                return True
            pos += 1

        return False

    def update(self, rid, rName, rcId):
        pos = 0
        for res in self.resources:
            if int(res['rid']) == int(rid):
                newRes = self.resources[pos]
                newRes['rName'] = rName
                newRes['rcId'] = rcId
                return True
            pos += 1
        return False
