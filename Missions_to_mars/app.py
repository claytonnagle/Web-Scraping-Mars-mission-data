#####flask setup#####
from flask import Flask, jsonify, render_template, redirect
import pymongo


app = Flask(__name__)
####################


@app.route("/scrape")
def scrape_page():

    from scrape_mars import scrape

    conn = 'mongodb://localhost:27017'

    client = pymongo.MongoClient(conn)

    db = client.mars_db
    db.mars_data.drop()

    scraped = scrape()

    db.mars_data.insert(
        scraped
    )

    return redirect("http://127.0.0.1:5000/")

@app.route("/")
def home():

    conn = 'mongodb://localhost:27017'

    client = pymongo.MongoClient(conn)

    db = client.mars_db

    mars_query = list(db.mars_data.find())[0]

    return render_template('index.html', mars_query = mars_query)





if __name__ == "__main__":
    app.run(debug=True)

    