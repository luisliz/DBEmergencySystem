from flask import jsonify
from app.dao.user import UsersDAO


class UserHandler:
    def build_user_dict(self, row): #DONE
        # result = {}
        # result['uid'] = row[0]
        # result['user_rank'] = row[1]
        # result['first_name'] = row[2]
        # result['last_name'] = row[3]
        # result['email'] = row[4]
        return row

    def get_all_users(self):#DONE
        dao = UsersDAO()
        users_list = dao.getAllUsers()
        result_list = []
        for row in users_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users=result_list)

    def get_ranks(self): #DONE
        dao = UsersDAO()
        ranks = dao.getRanks()
        return jsonify(Ranks=ranks)

    def get_user_rank(self, uid): #Done
        dao = UsersDAO()
        rank = dao.getUserRank(uid)
        return jsonify(uid=uid, Rank=rank)

    def get_users_byrank(self, rank): #Done
        dao = UsersDAO()
        users = dao.getUsersByRank(rank)
        return jsonify(Users=users)

    def get_user_byid(self, uid): #Done
        dao = UsersDAO()
        user = dao.getUserById(uid)
        result = self.build_user_dict(user)
        return jsonify(User=result)

    def add_user(self, form): #Done
        first_name = form['firstname']
        last_name = form['lastname']
        dob = form['dob']
        email = form['email']
        password = form['password'] #Have to hash this

        dao = UsersDAO()
        uid = dao.insert(first_name, last_name, dob, email, password)
        return jsonify(uid=uid)

    def delete_user(self, form):
        dao = UsersDAO()
        uid = form['uid']
        user = dao.delete(uid)
        return jsonify(deleted=user)

    def logout_user(self, uid):
        #LogoutUser
        print("Logout User")
        return uid
    # def delete_user_byid(self, uid):
    #     dao = UsersDAO()
    #     dao.delete(uid)
    #
    # def update_user(self, uid, form):
    #     dao = UsersDAO()
    #     dao.update
    #
    def count_users(self): #Done
        dao = UsersDAO()
        userCount = dao.count_users()
        return jsonify(UserCount = userCount)
    #
    def count_ranks(self): #Done
        dao = UsersDAO()
        user_ranks = dao.count_ranks()
        return jsonify(Ranks=user_ranks)

    def count_rank_byid(self, rid): #Done
        dao = UsersDAO()
        total = dao.count_rank(rid)
        return jsonify(Rank=total)
    #
    # def search_users(self, args):
    #     dao = UsersDAO()
    #     dao.

