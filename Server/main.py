from flask import Flask, jsonify
import DB

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({'status':'ok'})

@app.route("/get_user_data/<id>")
def getUserData(id):
    return DB.getUserData(id, json=True)

@app.route("/get_category")
def getCategory():
    return DB.getCategory(json=True)

@app.route("/get_subcategory/<id>")
def getSubCategory(id):
    return DB.getSubCategory(id, json=True)

if __name__ == "__main__":
    DB.getUserData(1)
    app.run()