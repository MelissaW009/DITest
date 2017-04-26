# /usr/bin/python2
# coding=utf-8
import csv
import sys
import codecs
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')


'''
csv_filename = sys.argv[1]
database = sys.argv[2]
table_name = sys.argv[3]
'''
dbhost = "localhost"
password = '123wmx'
csv_filename = "/home/melissa/A/data/test2.csv"
database = "ditest"
table_name = "titanic_test"

file = codecs.open(csv_filename, 'r', 'utf-8')
reader = file.readline()
b = reader.split(',')
colum = ''
for a in b:
    colum = colum + a + ' varchar(255),'
colum = colum[:-1]
create = 'create table if not exists ' + table_name + ' ' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8'
data = 'LOAD DATA LOCAL INFILE \'' + csv_filename + '\' INTO TABLE ' + table_name + \
       ' character set utf8 FIELDS TERMINATED BY \',\' ENCLOSED BY \'\"\' LINES TERMINATED BY \'' + r'\r\n' + '\' IGNORE 1 LINES;'
e = unicode(data, 'utf8')

conn = MySQLdb.connect(
    host=dbhost,
    port=3306,
    user='root',
    passwd='123wmx',
    db=database)
conn.set_character_set('utf8')
cursor = conn.cursor()
cursor.execute('SET NAMES utf8;')
cursor.execute('SET character_set_connection=utf8;')
cursor.execute(create)
cursor.execute(e)
cursor.rowcount

conn.commit()
cursor.close()
print('OK')