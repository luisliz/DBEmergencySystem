from app.config.database_config import pg_config
#import psycopg2

class UsersDAO:

    users = [
        {
            'uid': 1,
            'ucid': 1,
            'ufirstName': 'Luis',
            'ulastName': 'Liz',
            'udob': 938509285,
            'uemail': 'luis@gmail.com',
            'upassword': 'passsword'
        },
        {
            'uid': 2,
            'ucid': 2,
            'ufirstName': 'Yeniel',
            'ulastName': 'Diaz',
            'udob': 95002395,
            'uemail': 'yeniel@gmail.com',
            'upassword': 'passswoiaodsih34'
        }
    ]

    ucids = [
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
        return self.ucids

    def getUserRank(self, uid): #Done
        user = self.getUserById(uid)

        for r in self.ucids:
            if r['rid'] == user['ucid']:
                return r['rank_name']

        return None

    def getUsersByRank(self, rank):
        result = []
        rid = None
        for r in self.ucids:
            if r['rank_name'] == rank:
                rid = r['rid']

        if rid is not None:
            for user in self.users:
                if user['ucid'] == rid:
                    result.append(user)

        return result

        # rank_id = None
        # for rid, r in self.ucids:
        #     if r == rank:
        #         rank_id = rid
        #
        # if rank_id is not None:
        #     for user in self.users:
        #         if user['ucid'] == rank_id:
        #             result.append(user)
        #
        #return result

    def getUserByFirst(self, ufirstName):
        for i, user in self.users:
            if user['ufirstName'] == ufirstName:
                return user
        return None

    def getUserByLast(self, ulastName):
        for i, user in users:
            if user['ulastName'] == ulastName:
                return user
        return result

    def getUserByFirstAndLastName(self, ufirstName, ulastName):
        for i, user in users:
            if (user['ufirstName'] == ufirstName) and (user['ulastName'] == ulastName):
                return user
        return result

    def count_users(self): #Done
        return len(self.users)

    def count_ranks(self): #Done
        ranks = {}
        for rank in self.ucids:
            ranks[rank['rid']] = 0
            for user in self.users:
                if user['ucid'] == rank['rid']:
                    ranks[rank['rid']] += 1

        return ranks

    def count_rank(self, rid): #Done
        total = 0
        for user in self.users:
            if user['ucid'] == rid:
                total += 1
        return total

    def insert(self, ufirstname, ulastname, uudob, uuemail, uupassword): #Done
        newUID = len(self.users)+1
        new_user = {
            'uid': len(self.users)+1,
            'ucid': 4,
            'ufirstName': ufirstname,
            'ulastName': ulastname,
            'udob': uudob,
            'uemail': uuemail,
            'upassword': uupassword
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

    def update(self, uid, ufirstname, ulastname, uudob, uuemail, uupassword, rid):

        return uid
