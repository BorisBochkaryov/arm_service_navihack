from flask import Flask, jsonify, send_file
import DB

app = Flask(__name__)

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

@app.route("/get_order")
def getOrder():
    return DB.getOrder(json=True)


# web сайт
@app.after_request
def set_response_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route("/")
def index():
    return send_file("../webARM/index.html")

@app.route("/css/<file>")
def css(file):
    return send_file("../webARM/css/" + str(file))

@app.route("/js/<file>")
def js(file):
    return send_file("../webARM/js/" + str(file))

if __name__ == "__main__":
    app.run()