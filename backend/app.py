from flask import Flask,jsonify
from flask_cors import CORS
from db import connection

app=Flask(__name__)
CORS(app)

@app.route("/users")
def users():

    cursor=connection.cursor()

    cursor.execute("SELECT * FROM users")

    rows=cursor.fetchall()

    result=[]

    for row in rows:

        result.append({
            "id":row[0],
            "name":row[1]
        })

    return jsonify(result)

app.run(host="0.0.0.0",port=5000)
