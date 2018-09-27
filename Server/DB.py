import sqlite3
from flask import jsonify

def __sql_exec_one(sql):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    return result

def __sql_exec_all(sql):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    conn.close()
    return result

def getUserData(id, json=False):
    result_user = __sql_exec_one("SELECT * FROM users WHERE id = '" + str(id) + "'")
    id, fio, address, phone = result_user
    if json == True:
        return jsonify({'id':id, 'fio':fio, 'address':address, 'phone':phone})
    else:
        return result_user

def getCategory(json=False):
    result_category = __sql_exec_all("SELECT * FROM category")
    categories = [dict(zip(('id', 'title'), X)) for X in result_category]
    if json == True:
        return jsonify({'status':'ok', 'categories':categories})
    else:
        return result_category

def getSubCategory(id, json=False):
    result_subcategory = __sql_exec_all("SELECT * FROM subcategory WHERE category_id = '" + str(id) + "'")
    subcategories = [dict(zip(('id', 'category_id', 'title'), X)) for X in result_subcategory]
    if json == True:
        return jsonify({'status':'ok', 'category_id':id, 'subcategories':subcategories})
    else:
        return result_subcategory
