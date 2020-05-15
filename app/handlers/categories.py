from flask import jsonify
from app.dao.resources import ResourcesDAO


class CategoryHandler:

    def add_medications(self, form):
        mmanufacturer = form['mmanufacturer']
        mname = form['mname']
        msize = form['msize']

        if mmanufacturer and mname and msize:
            daoR = ResourcesDAO()
            mid = daoR.insertMedications(mmanufacturer, mname, msize)
            return mid
        else:
            return None

    def add_canned_foods(self, form):
        canbrand = form['canbrand']
        cantype = form['cantype']

        if canbrand and cantype:
            daoR = ResourcesDAO()
            canid = daoR.insertCannedFoods(canbrand, cantype)
            return canid
        else:
            return None

    def add_baby_foods(self, form):
        bflavor = form['bflavor']
        bbrand = form['bbrand']

        if bflavor and bbrand:
            daoR = ResourcesDAO()
            bid = daoR.insertBabyFoods(bflavor, bbrand)
            return bid
        else:
            return None

    def add_dry_foods(self, form):
        drybrand = form['drybrand']
        drytype = form['drytype']

        if drybrand and drytype:
            daoR = ResourcesDAO()
            dryid = daoR.insertDryFoods(drybrand, drytype)
            return dryid
        else:
            return None

    def add_ices(self, form):
        ibrand = form['ibrand']
        ibagsize = form['ibagsize']
        iweight = form['iweight']

        if ibrand and ibagsize and iweight:
            daoR = ResourcesDAO()
            iid = daoR.insertIces(ibrand, ibagsize, iweight)
            return iid
        else:
            return None 


    def add_fuels(self, form):
        ftype = form['ftype']
        fbrand = form['fbrand']
        fvolume = form['fvolume']

        if ftype and fbrand and fvolume:
            daoR = ResourcesDAO()
            fid = daoR.insertFuels(ftype, fbrand, fvolume)
            return fid
        else:
            return None

    def add_heavy_equipments(self, form):
        hbrand = form['hbrand']
        htype = form['htype']

        if hbrand and htype:
            daoR = ResourcesDAO()
            hid = daoR.insertHeavyEquipments(hbrand, htype)
            return hid
        else:
            return None

    def add_clothings(self, form):
        clothbrand = form['clothbrand']
        clothmaterial = form['clothmaterial']
        clothtype = form['clothtype']

        if clothbrand and clothmaterial and clothtype:
            daoR = ResourcesDAO()
            clothid = daoR.insertClothings(clothbrand, clothmaterial, clothtype)
            return clothid
        else:
            return None

    def add_power_generators(self, form):
        genbrand = form['genbrand']
        genpower = form['genpower']
        gentype = form['gentype']

        if genbrand and genpower and gentype:
            daoR = ResourcesDAO()
            genid = daoR.insertPowerGenerators(genbrand, genpower, gentype)
            return genid
        else:
            return None
