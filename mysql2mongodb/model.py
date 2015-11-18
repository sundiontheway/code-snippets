# coding: utf-8
from mysql import MysqlClient
from mongo import MongoClient

DB_MAP = {'mysql': MysqlClient,
          'mongo': MongoClient}


class ResultObj(object):
    def __init__(self, vattr):
        self.raw_attr = vattr
        self._attrs = {}
        for k,v in vattr.iteritems():
            self._attrs[k] = v

    def __getattr__(self, k):
        if k not in self._attrs:
            return None
        else:
            return self._attrs[k]


class DatabaseObj(object):
    def __init__(self, param):
        self._client = DB_MAP[param['name']](param)
        self._reader = self._client.read()

    def read(self):
        return ResultObj(self._reader.next())

    def write(self, resobj):
        return self._client.write(resobj)
