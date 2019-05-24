import sys
sys.path.insert(0,'../../')
from ds.db import connect

cursor = connect.Connection.getCursor()

def getData(_idx):
    select  = "SELECT * FROM data "
    where = "WHERE idx=%s"
    cursor.execute(select+where,(_idx))
    res = cursor.fetchone()
    return res

def getDataFromKey(_key):
    select = "SELECT * FROM data "
    where = "WHERE k=%s"
    cursor.execute(select+where,(_key))
    res = cursor.fetchone()
    return res


def insertData(_key,_value):
    insert = "INSERT INTO data(k,v) "
    values = "VALUES(%s,%s)"
    cursor.execute(insert+values,(_key,_value));
    connect.Connection.commit()
    res = cursor.lastrowid
    return res

def updateData(_idx,_data):
    update = "UPDATE data SET data=%s "
    where = "WHERE idx=%s"
    cursor.execute(update+where, (_data,_idx))
    connect.Connection.commit()
    res = cursor.lastrowid
    return res

def updateValue(_key,_value):
    update = "UPDATE data SET v=%s"
    where = "WHERE k=%s"

    cursor.execute(update+where,(_value,_key))
    connect.Connection.commit()
    res = cursor.lastrowid
    return res

