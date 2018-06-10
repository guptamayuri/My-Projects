#store history into database(mysql)
import pymysql
import history #import history.py program
import os
from uuid import getnode as get_mac

db = pymysql.connect("172.16.6.160", "root", "oracle123", "monitor")#database connection
cursor = db.cursor()


def chrome_history_fetch():
    mac = get_mac()
    cursor.callproc('test_pro', [mac])#call procedure "test_pro" from mysql
    for result in cursor.fetchall():
        result1 = result[0]
    print(result1)

    sql = "update record set search ='{0}' where mac_add ='{1}' and u_logon = STR_TO_DATE('{2}', '%Y-%m-%d %H:%i:%s');".format(history.s, mac, result1)
    cursor.execute(sql)
    db.commit()
    os.system("shutdown /s /t 1");#system shutdown command


chrome_history_fetch()
