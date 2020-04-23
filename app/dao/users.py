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
        self.conn = psycopg2.connect(
            user=pg_config["user"],
            password=pg_config['passwd'],
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database']
        )

    def getAllUsers(self): #Done
        cursor = self.conn.cursor()
        query = "select uid, ucid, ufirstName, ulastName, udob, uemail  from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, uid):
        cursor = self.conn.cursor()
        query = "select uid, ucid, ufirstName, ulastName, udob, uemail  from users where uid = %s;"
        cursor.execute(query, (uid,))
        return cursor.fetchone()

    def getUserByFirst(self, ufirstName):
       cursor = self.conn.cursor()
       query = "select uid, ucid, ufirstName, ulastName, udob, uemail  from users where ufirstName = %s;"
       cursor.execute(query, ufirstName)
       result = []
       for row in cursor:
           result.append(row)
       return result

    def getUserByLast(self, ulastName):
       cursor = self.conn.cursor()
       query = "select uid, ucid, ufirstName, ulastName, udob, uemail  from users where ulastName = %s;"
       cursor.execute(query, ulastName)
       result = []
       for row in cursor:
           result.append(row)
       return result

    def getUserByFirstAndLastName(self, ufirstName, ulastName):
        cursor = self.conn.cursor()
        query = "select uid, ucid, ufirstName, ulastName, udob, uemail  from users where ufirstName = %s AND ulastName = %s;"
        cursor.execute(query, (ufirstName, ulastName))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def count_users(self):
        return len(self.users)


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
