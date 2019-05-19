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

def insertData(_data):
    insert = "INSERT INTO data(data) "
    values = "VALUES(%s)"
    cursor.execute(insert+values,(_data));
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

    

    
