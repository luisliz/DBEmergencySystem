from flask import jsonify
from app.dao.user_category import UserCategoryDAO

class UserCategoryHandler:
    def build_user_category_dict(self, row):
        # result = {}
        # result['ucid'] = row[0]
        # result['ucName'] = row[1]
        return row

    def get_all_categories(self):
        dao = UserCategoryDAO()
        user_category_list = dao.getAllCategories()
        result_list = []
        for row in user_category_list:
            result = self.build_user_category_dict(row)
            result_list.append(result)
        return jsonify(User_Categories=result_list)

    def get_category_by_id(self, ucid):
        dao = UserCategoryDAO()
        result = self.build_user_category_dict(dao.getCategoryById(ucid))
        return jsonify(Category = result)

    def add_category(self, form):
        ucName = form['ucName']
        dao = UserCategoryDAO()
        ucid = dao.insert(ucName)
        return jsonify(ucid=ucid)

    def delete_category(self, form):
        dao = UserCategoryDAO()
        ucid = form['ucid']
        rc = dao.delete(ucid)
        return jsonify(deleted=rc)

    def update_category(self, form):
        ucid = form['ucid']
        ucName = form['ucName']
        dao = UserCategoryDAO()
        result = dao.update(ucid, ucName)
        return jsonify(updated = result)

