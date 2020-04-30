from app.config.database_config import pg_config
import psycopg2

class ResourceCategoryDAO:

    def __init__(self):
        self.conn = psycopg2.connect(
            user=pg_config["user"],
            password=pg_config['passwd'],
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database']
        )

        # self.resource_cat = [
        #     {
        #         'rcid': 1,
        #         'rcName': 'Water'
        #     },
        #     {
        #         'rcid': 2,
        #         'rcName': 'Medication'
        #     },
        #     {
        #         'rcid': 3,
        #         'rcName': 'Canned Food'
        #     }
        # ]

    def getAllCategories(self):
        cursor = self.conn.cursor()
        query = "select rcid, rcname from resource_category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryById(self, rcid):
        cursor = self.conn.cursor()
        query = "select rcid, rcname from resource_category where rcid = %s;"
        cursor.execute(query, (rcid,))
        result = cursor.fetchone()
        return result

    def insert(self, rcName):
        newrcID = len(self.resource_cat)+1
        new_cat = {
                'rcid': newrcID,
                'rcName': rcName
            }
        self.resource_cat.append(new_cat)
        return newrcID

    def delete(self, rcid):
        pos = 0
        for cat in self.resource_cat:
            if int(cat['rcid']) == int(rcid):
                del self.resource_cat[pos]
                return True
            pos += 1
        return False

    def update(self, rcid, rcName):
        pos = 0
        for cat in self.resource_cat:
            if int(cat['rcid']) == int(rcid):
                newCat = self.resource_cat[pos]
                newCat['rcName'] = rcName
                return True
            pos += 1
        return False
