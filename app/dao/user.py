from app.config.database_config import pg_config
#import psycopg2
class UsersDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        #self.conn = psycopg2._connect(connection_url)

        users = {
            1: {
                'user_category_id': 1,
                'first_name': 'Luis',
                'last_name': 'Liz',
                'dob': 938509285,
                'email': 'luis@gmail.com',
            },
            2: {
                'user_category_id': 1,
                'first_name': 'Yeniel',
                'last_name': 'Diaz',
                'dob': 95002395,
                'email': 'yeniel@gmail.com',
            }
        }

        def getAllUsers(self):
            # cursor = self.conn.cursor()
            # query = "select pid, pname, pmaterial, pcolor, pprice from parts;"
            # cursor.execute(query)
            # result = []
            # for row in cursor:
            #     result.append(row)
            result = users
            return result

        def getUserById(self, uid):
            for id, user in users:
                if id == uid:
                    return user
            return None

        # def getUserByRank(self, rank):
        #
        #     return result

        def getUserByFirst(self, first_name):
            for i, user in users:
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


        def insert(self, pname, pcolor, pmaterial, pprice):

            return pid

        def delete(self, pid):

            return pid

        def update(self, pid, pname, pcolor, pmaterial, pprice):

            return pid
