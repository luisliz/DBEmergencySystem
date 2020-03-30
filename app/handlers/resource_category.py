from flask import jsonify
from app.dao.resource_category import ResourceCategoryDAO

class ResourceCategoryHandler:
    def build_resource_category_dict(self, row):
        # result = {}
        # result['rcid'] = row[0]
        # result['rcName'] = row[1]
        return row

    def get_all_categories(self):
        dao = ResourceCategoryDAO()
        resource_category_list = dao.getAllCategories()
        result_list = []
        for row in resource_category_list:
            result = self.build_resource_category_dict(row)
            result_list.append(result)
        return jsonify(Resource_Categories=result_list)

    def get_category_by_id(self, rcid):
        dao = ResourceCategoryDAO()
        result = self.build_resource_category_dict(dao.getCategoryById(rcid))
        return jsonify(Category = result)

    def add_category(self, form):
        rcName = form['rcName']
        dao = ResourceCategoryDAO()
        rcid = dao.insert(rcName)
        return jsonify(rcid=rcid)

    def delete_category(self, form):
        dao = ResourceCategoryDAO()
        rcid = form['rcid']
        rc = dao.delete(rcid)
        return jsonify(deleted=rc)

    def update_category(self, rcid, form):
        # rcid = form['rcid']
        rcName = form['rcName']
        dao = ResourceCategoryDAO()
        result = dao.updateCat(rcid, rcName)
        return jsonify(updated = result)

