import sys
sys.path.insert(0,'../../')
from ds.db import data

def insert(_data):
    res = data.insertData(_data)
    return res
