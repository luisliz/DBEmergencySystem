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
        cursor = self.conn.cursor()
        query = "select ucid, ucname from resource_category;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCategoryById(self, ucid):
        for cat in self.resource_cat:
            if cat['ucid'] == ucid:
                return cat
        return None

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
