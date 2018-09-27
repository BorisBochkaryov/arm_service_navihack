from flask import Flask, jsonify
import DB

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({'status':'ok'})

@app.route("/get_user_data/<id>")
def getUserData(id):
    return DB.getUserData(id, json=True)

@app.route("/set_user_data/<id>/<field>/<data>")
def setUserData(id, field, data):
    DB.setUserData(id, field, data)
    return jsonify({'status':'ok'})

@app.route("/get_category")
def getCategory():
    return DB.getCategory(json=True)

@app.route("/get_subcategory/<id>")
def getSubCategory(id):
    return DB.getSubCategory(id, json=True)

@app.route("/get_staff/<category>/<subcategory>")
def getStaff(category, subcategory):
    return DB.getStaff(category, subcategory, json=True)

@app.route("/add_order/<user_id>/<staff_id>/<date>/<comment>")
def addOrder(user_id, staff_id, date, comment):
    DB.addOrder(user_id, staff_id, date, comment)
    return jsonify({'status':'ok'})

if __name__ == "__main__":
    app.run()