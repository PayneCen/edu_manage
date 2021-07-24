# coding:utf-8

import pymysql

userID = ""
userPwd = ""
userType = ""
idType = ""

def open():
    db = pymysql.connect(
        host="",
        port=,
        user="",
        password="",
        database="",
        charset="utf8"
    )
    return db


def exec(sql, values):
    db = open()
    cursor = db.cursor()
    try:
        cursor.execute(sql, values)
        db.commit()
        return 1
    except:
        db.rollback()
        return 0
    finally:
        cursor.close()
        db.close()

# 精准查询
def query(sql, *keys):
    db = open()
    cursor = db.cursor()
    cursor.execute(sql, keys)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

# 模糊查询
def query2(sql):
    db = open()
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result
