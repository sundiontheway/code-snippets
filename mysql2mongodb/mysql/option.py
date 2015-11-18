# coding: utf-8

import MySQLdb as _mysql


class MysqlClient(object):
    def __init__(self, param):
        host = param['host']
        port = param['port']
        user = param['user']
        passwd = param['passwd']
        db = param['database']
        table = param['table']
        self._column = param['column']
        self._db = _mysql.connect(host=host, port=port, user=user,
                                passwd=passwd, db=db)
        self._table = '%s.%s' % (db, table)

        if isinstance(self._column, list) and len(self._column):
            column_str = map(lambda x:"`%s`" % x, self._column)
            self._column_str = ' ,'.join(column_str)

    def tuple2dict(self, sql_data):
        r = {}
        for i, col in enumerate(self._column):
            r[col] = sql_data[i]

        return r

    def read(self):
        c = self._db.cursor()
        sql = "select %s from %s ;" % (self._column_str, self._table)
        print '[MySQL]<in>: ', sql
        c.execute(sql)
        r = c.fetchone()
        while r:
            yield self.tuple2dict(r)
            r= c.fetchone()

    def write(self):
        pass
