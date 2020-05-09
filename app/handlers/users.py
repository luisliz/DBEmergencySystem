from flask import jsonify
from app.dao.users import UsersDAO
from app.dao.user_category import UserCategoryDAO


class UserHandler:
    def build_user_dict(self, row): #DONE
        result = {}
        if row == None:
            return {'error': 'User Not found'}
        else:
            result['uid'] = row[0]
            result['ucid'] = row[1]
            result['ufirstName'] = row[2]
            result['ulastName'] = row[3]
            result['udob'] = row[4]
            result['uemail'] = row[5]
            return result

    def get_all_users(self):#DONE
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def getUsersByCategory(self, category): #Done
        dao = UsersDAO()
        users = dao.getUsersByCategory(category)
        return jsonify(Users=users)

    def getUserById(self, uid): #Done
        dao = UsersDAO()
        user = dao.getUserById(uid)
        result = self.build_user_dict(user)
        return jsonify(User=result)

    def add_user(self, form):
        udao = UsersDAO()
        catDao = UserCategoryDAO()

        ucid = form['ucid']
        ufirstname = form['ufirstname']
        ulastname = form['ulastname']
        udob = form['udob']
        uemail = form['uemail']
        upassword = form['upassword']

        if 'ucid' in form:
            categoryid = ucid
            catid = catDao.getCategoryById(ucid)
            if not catid:
                return jsonify(error='category id: ' + ucid + ' does not exist')

        if udao.checkEmailExists(uemail):
            return jsonify(error=uemail + ' already exists')

        uid = udao.insert(categoryid, ufirstname, ulastname, udob, uemail, upassword)
        return jsonify(uid=uid)

    def count_users(self): #Done
        dao = UsersDAO()
        userCount = dao.count_users()
        return jsonify(UserCount = userCount)

    # def search_users(self, args):
    #     dao = UsersDAO()
    #     dao.

