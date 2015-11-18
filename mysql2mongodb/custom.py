# coding: utf-8
"""
There are some custome rules for exchanging your data. You can define the
function custom_rules(resobj). Parameter 'resobj' is a object that store the
result. For example, there is a column named 'id' in mySQL, you want to keep
it as "mysql_id" in mongoDB, you can define the function as below.
"""

def custom_rules(resobj):
    resobj.mysql_id = resobj.id
    return resobj
