#fetching chrome's history
import sqlite3
from os.path import expanduser
import pymysql

History_DB = 'C:\\Users\\asus\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History' #address of chrome's history

db = pymysql.connect("172.16.6.160", "root", "oracle123", "monitor") #connect to mysql
cursor = db.cursor()
from uuid import getnode as get_mac #getting mac address of system
mac = get_mac()
cursor.callproc('history', [mac]) #call procedure "history" from mysql
for raw1 in cursor.fetchall():
    var2 = raw1[0]
db.close()

def chrome_history():
    global var5
    global s
    var5 = []
    global var4
    conn = sqlite3.connect(expanduser(History_DB)) #connect to sqlite
    c = conn.cursor()
    result = c.execute('SELECT datetime(last_visit_time/1000000-11644473600, "unixepoch","localtime") as last_visited, url FROM urls;')#sqlite query for fetching history
    for row in result:
       var = row[0]
       if var2 <= var:
           var4 = row[1]
           var5.append(var4)
    s = ", ".join(var5)
    print(s)


chrome_history()



