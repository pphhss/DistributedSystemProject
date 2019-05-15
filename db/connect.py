import pymysql
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import config


class Connection():
    __conn=None

    @classmethod
    def __getConnection(cls):
        if cls.__conn == None:
            cls.__conn = pymysql.connect(host=config.db.get('host')
                    ,user=config.db.get('user')
                    , password=config.db.get('password')
                    , db=config.db.get('db')
                    ,charset=config.db.get('charset'))

    @classmethod
    def getCursor(cls):
        if cls.__conn==None:
            cls.__getConnection()

        return cls.__conn.cursor(pymysql.cursors.DictCursor)

