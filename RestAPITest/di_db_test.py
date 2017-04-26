

#refers to http://www.jb51.net/article/92516.htm

import pymysql
import pymysql.cursors

connection = pymysql.connect(host='127.0.0.1',
                             port=3306,
                             user='dolphin',
                             passwd='dolphin',
                             db='dolphin',
                             charset='utf8')

# 执行sql语句
try:
    cursor = connection.cursor()

    sql = 'SELECT * from user_model;'
    effect_rows= cursor.execute(sql)
    print(effect_rows)
    # 获取剩余结果的第一行数据
    row_1 = cursor.fetchone()
    print(row_1)
    # 获取剩余结果前n行数据
    # row_2 = cursor.fetchmany(3)

    # 获取剩余结果所有数据
    row_3 = cursor.fetchall()
    print(row_3)
    # 提交，不然无法保存新建或者修改的数据
    connection.commit()

finally:
    cursor.close()
    connection.close()