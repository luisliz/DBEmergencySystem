from flask import jsonify
from app.dao.resources import ResourcesDAO


class CategoryHandler:

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

    def add_baby_foods(self, form):
        bflavor = form['bflavor']
        bbrand = form['bbrand']

        if bflavor and bbrand:
            daoR = ResourcesDAO()
            bid = daoR.insertBabyFoods(bflavor, bbrand)
            return bid
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

