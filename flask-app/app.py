from flask import Flask, request, render_template, jsonify, url_for
from flask_cors import CORS
import pandas as pd

df = pd.read_excel("flask-app/extracted_text.xlsx")
app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search_autocomplete():
    query = request.args["q"].lower()
    if query == "":
        return jsonify([])
    res = [
        row["image_name"]
        for index, row in df.iterrows()
        if query in row["extracted_text"].lower()
    ]
    return jsonify([url_for("static", filename="Hiring/" + i) for i in res])


if __name__ == "__main__":
    app.run()
