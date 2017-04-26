# coding=utf-8
import csv
import sys
import codecs
import pymysql.cursors


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
sql_create = 'create table if not exists ' + table_name + ' ' + '(' + colum + ')' + ' DEFAULT CHARSET=utf8'
sql_data = 'LOAD DATA LOCAL INFILE \'' + csv_filename + '\' INTO TABLE ' + table_name +\
           ' character set utf8 FIELDS TERMINATED BY \',\' ENCLOSED BY \'\"\' LINES TERMINATED BY \'' + r'\r\n' + '\' IGNORE 1 LINES;'

print("==================")
print(sql_data)
print("==================")

config = {
    'host':dbhost,
    'port':3306,
    'user':'root',
    'passwd':password,
    'db':database,
    'charset':'utf8',
    'cursorclass':pymysql.cursors.DictCursor,
    'local_infile':True
    }

#conn = pymysql.connect(**config)
conn = pymysql.connect(host=dbhost, user='root', passwd=password,
                 database=database, port=3306, charset='utf8',
                 cursorclass=pymysql.cursors.DictCursor, local_infile=True)

try:
    cursor= conn.cursor()
    cursor.execute('SET NAMES utf8;')
    cursor.execute(sql_create)
    #cursor.execute("SET @@global.local_infile = 1;")
    cursor.execute(sql_data)
    #cursor.execute("show global variables like \"local_infile\" ;")
    result = cursor.fetchall()
    print(result)
    conn.commit()

finally:
    conn.close()
print('OK')