from app.config.database_config import pg_config
import psycopg2

class UserCategoryDAO:

    def __init__(self):
        self.conn = psycopg2.connect(
            user=pg_config["user"],
            password=pg_config['passwd'],
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database']
        )

    def getAllUserCategories(self):
        cursor = self.conn.cursor()
        query = "select ucid, ucname from resource_category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryById(self, ucid):
        cursor = self.conn.cursor()
        query = "select ucid, ucname from resource_category where ucid = %s;"
        cursor.execute(query, (ucid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def countCategories(self):
        cursor = self.conn.cursor()
        query = "select COUNT(*) from resource_category"
        cursor.execute(query)
        return cursor.fetchone()

    def insert(self, ucName):
        newucid = len(self.resource_cat)+1
        new_cat = {
                'ucid': newucid,
                'ucName': ucName
            }
        self.resource_cat.append(new_cat)
        return newucid

    def delete(self, ucid):
        pos = 0
        for cat in self.resource_cat:
            if int(cat['ucid']) == int(ucid):
                del self.resource_cat[pos]
                return True
            pos += 1
        return False

    def update(self, ucid, ucName):
        pos = 0
        for cat in self.resource_cat:
            if int(cat['ucid']) == int(ucid):
                newCat = self.resource_cat[pos]
                newCat['ucName'] = ucName
                return True
            pos += 1
        return False
