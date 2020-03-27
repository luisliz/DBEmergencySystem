from app.config.database_config import pg_config
#import psycopg2

class UsersDAO:

    users = [
        {
            'uid': 1,
            'user_rank': 1,
            'first_name': 'Luis',
            'last_name': 'Liz',
            'dob': 938509285,
            'email': 'luis@gmail.com',
            'password': 'passsword'
        },
        {
            'uid': 2,
            'user_rank': 2,
            'first_name': 'Yeniel',
            'last_name': 'Diaz',
            'dob': 95002395,
            'email': 'yeniel@gmail.com',
            'password': 'passswoiaodsih34'
        }
    ]

    user_ranks = [
        {'rid': 1, 'rank_name': 'admin'},
        {'rid': 2, 'rank_name': 'provider'},
        {'rid': 3, 'rank_name': 'supplier'},
        {'rid': 4, 'rank_name': 'user'},
    ]

    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        # self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self): #Done
        # cursor = self.conn.cursor()
        # query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
        # cursor.execute(query)
        # result = []
        # for row in self.users:#cursor:
        #     result.append(row)
        result = self.users
        return result

    def getUserById(self, uid): #Done
        for user in self.users:
            if user['uid'] == uid:
                return user
        return None

    def getRanks(self): #Done
        return self.user_ranks

    def getUserRank(self, uid): #Done
        user = self.getUserById(uid)

        for r in self.user_ranks:
            if r['rid'] == user['user_rank']:
                return r['rank_name']

        return None

    def getUsersByRank(self, rank):
        result = []
        rid = None
        for r in self.user_ranks:
            if r['rank_name'] == rank:
                rid = r['rid']

        if rid is not None:
            for user in self.users:
                if user['user_rank'] == rid:
                    result.append(user)

        return result

        # rank_id = None
        # for rid, r in self.user_ranks:
        #     if r == rank:
        #         rank_id = rid
        #
        # if rank_id is not None:
        #     for user in self.users:
        #         if user['user_rank'] == rank_id:
        #             result.append(user)
        #
        #return result

    def getUserByFirst(self, first_name):
        for i, user in self.users:
            if user['first_name'] == first_name:
                return user
        return None

    def getUserByLast(self, last_name):
        for i, user in users:
            if user['last_name'] == last_name:
                return user
        return result

    def getUserByFirstAndLastName(self, first_name, last_name):
        for i, user in users:
            if (user['first_name'] == first_name) and (user['last_name'] == last_name):
                return user
        return result

    def count_users(self): #Done
        return len(self.users)

    def count_ranks(self): #Done
        ranks = {}
        for rank in self.user_ranks:
            ranks[rank['rid']] = 0
            for user in self.users:
                if user['user_rank'] == rank['rid']:
                    ranks[rank['rid']] += 1

        return ranks

    def count_rank(self, rid): #Done
        total = 0
        for user in self.users:
            if user['user_rank'] == rid:
                total += 1
        return total

    def insert(self, ufirstname, ulastname, udob, uemail, upassword): #Done
        newUID = len(self.users)+1
        new_user = {
            'uid': len(self.users)+1,
            'user_rank': 4,
            'first_name': ufirstname,
            'last_name': ulastname,
            'dob': udob,
            'email': uemail,
            'password': upassword
        }
        self.users.append(new_user)

        return newUID

    def delete(self, uid): #Done
        pos = 0
        for user in self.users:
            if int(user['uid']) == int(uid):
                del self.users[pos]
                return True
            pos += 1

        return False

    def update(self, uid, ufirstname, ulastname, udob, uemail, upassword, rid):

        return uid
