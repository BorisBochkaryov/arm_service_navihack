import sqlite3
from flask import jsonify

def getUserData(id, json=False):
    conn = sqlite3.connect("db.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM users WHERE id = '" + str(id) + "';"
    cursor.execute(sql)
    result_user = cursor.fetchone()
    id, fio, address = result_user
    conn.close()
    if json == True:
        return jsonify({'id':id, 'fio':fio, 'address':address})
    else:
        return result_user