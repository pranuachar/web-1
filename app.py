import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)

def get_product():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pranu_achar@07",
        database="product"
    )

    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT id, name, price FROM product")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return rows

@app.route("/")
def home():
    return render_template("index.html", products=get_product())

if __name__ == "__main__":
    app.run(debug=True)