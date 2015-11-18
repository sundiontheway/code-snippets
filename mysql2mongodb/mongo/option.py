# coding: utf-8
import pymongo


class MongoClient(object):
    def __init__(self, param):
        host = param['host']
        port = param['port']
        # user = param['user']
        # passwd = param['passwd']
        db = param['database']
        table = param['table']
        self._column = param['column']
        self._cli= pymongo.MongoClient(host=host, port=port)
        self._db = self._cli[db]
        self._table = self._db[table]

    def write(self, resobj):
        r = {}
        for k in self._column:
            r[k] = getattr(resobj, k, None)
        try:
            self._table.insert(r)
        except:
            import traceback
            traceback.print_exc()
            return False

        return True

    def read(self):
        yield
