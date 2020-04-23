from app.config.database_config import pg_config
import psycopg2

class UsersDAO:
    ucids = [
        {'rid': 1, 'rank_name': 'admin'},
        {'rid': 2, 'rank_name': 'provider'},
        {'rid': 3, 'rank_name': 'supplier'},
        {'rid': 4, 'rank_name': 'user'},
    ]

    def __init__(self):
        #YEAH I GOTTA MAKE A DATABASE AND USER WITH THESE CONFIGURATIONS BUT FOR NOW WHILEI IM FIGURING STUFF OUT
        '''
        self.conn = psycopg2.connect(
            user=pg_config["user"],
            password=pg_config['passwd'],
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database']
        '''
        self.conn = psycopg2.connect(host="localhost",database="disasterAid", user="appusr", password="class")

    def getAllUsers(self): #Done
        cursor = self.conn.cursor()
        query = "select uid, ucid, ufirstName, ulastName, udob, uemail, upassword from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
        for user in self.users:
            if user['uid'] == uid:
                return user
        return None

    def getRanks(self):
        return self.ucids

    def getUserRank(self, uid):
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

    def count_users(self):
        return len(self.users)

    def count_ranks(self):
        ranks = {}
        for rank in self.ucids:
            ranks[rank['rid']] = 0
            for user in self.users:
                if user['ucid'] == rank['rid']:
                    ranks[rank['rid']] += 1

        return ranks

    def count_rank(self, rid):
        total = 0
        for user in self.users:
            if user['ucid'] == rid:
                total += 1
        return total

    def insert(self, ufirstname, ulastname, uudob, uuemail, uupassword):
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
