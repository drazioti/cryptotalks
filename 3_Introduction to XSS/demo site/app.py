from flask import Flask, request, Response, render_template
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)
DATABASE = 'reviews.db'
connection = sqlite3.connect(DATABASE, check_same_thread=False)
cursor = connection.cursor()

#check if table already exists
cursor.execute('''CREATE TABLE IF NOT EXISTS reviews
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              review TEXT)''')

connection.commit()

@app.route("/", methods=["GET"])
def search():

    reviews = cursor.execute("""
    SELECT review
    FROM reviews
    """)
    
    review_comments = []
    for review in reviews:
        review_comments.append(review[0])

    return render_template('index.html', reviews=review_comments)

@app.route("/new-comment", methods=["POST"])
def new_comment():

    comment = (request.get_json()["comment"],)
    
    cursor.execute("""
    INSERT INTO reviews (review)
    VALUES(?)
    """, comment)
    connection.commit()

    return {"":""}


app.run(host="localhost", port=5000, debug=False)


