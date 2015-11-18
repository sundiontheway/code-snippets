# coding: utf-8

DB_SRC = {'name': 'mysql', # mysql or mongo
          'host': '127.0.0.1', # host
          'port': 3306, # port
          'user': 'syswin', # db username
          'passwd': 'syswin', # password
          'database': 'appconfig', # database name
          'table': 'servicelist', # table name
          'column':['id', # a list of columns you will exchange to DB_DST
                    'col1',
                    'col2',
                    'col3',
                    'col4']}

DB_DST = {'name': 'mongo',
          'host': '127.0.0.1',
          'port': 27017,
          'user': '',
          'passwd': '',
          'database': 'test',
          'table': 'test',
          'column':['mysql_id',
                    'col1',
                    'col2',
                    'col3',
                    'col4']}

