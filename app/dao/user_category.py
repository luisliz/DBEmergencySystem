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

        self.resource_cat = [
            {
                'ucid': 1,
                'ucName': 'User'
            },
            {
                'ucid': 2,
                'ucName': 'User'
            },
            {
                'ucid': 3,
                'ucName': 'Admin'
            }
        ]

    def getAllUserCategories(self):
        # cursor = self.conn.cursor()
        # query = "select ucid, ucName from resource_category;"
        # cursor.execute(query)
        # result = []
        # for row in self.users:#cursor:
        #     result.append(row)
        result = self.resource_cat
        return result

    def getCategoryById(self, ucid):
        for cat in self.resource_cat:
            if cat['ucid'] == ucid:
                return cat
        return None

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
