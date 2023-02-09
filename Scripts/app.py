import practice
from flask import Flask,jsonify


app = Flask(__name__)

@app.route("/dataframetojson", methods=["GET"])
def dataframe_to_json():
    a = practice.genrate_data()
    data = a.to_dict()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)


