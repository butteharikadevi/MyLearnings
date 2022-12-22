from flask import jsonify
from flask import *
import json

app = Flask(__name__)

countries = [{'id': 1, 'name': 'India', 'capital': 'Delhi'}, {'id': 2, 'name': 'USA', 'capital': 'NewYark'},
             {'id': 3, 'name': 'Canada', 'capital': 'Ottawa'}]


@app.route('/')
def index():
    return "Welcome to the python API \n Hi Harika we come to python develper club"


@app.route('/countries', methods=['GET'])
def getCountries():
    return jsonify(countries)


@app.route('/countries/<int:country_id>', methods=['GET'])
def getCountry(country_id):
    return jsonify(countries[country_id - 1])


@app.route('/countries', methods=['POST'])
def createCountry():
    country = request.get_json()
    countries.append(country)
    return jsonify(countries)


@app.route('/countries/<int:country_id>', methods=['PUT'])
def updateCountry(country_id):
    countries[country_id - 1] = request.get_json()
    return jsonify({'Updated': countries[country_id - 1]})


@app.route('/countries/<int:country_id>', methods=['DELETE'])
def deketeCountry(country_id):
    countries.remove(countries[country_id - 1])
    return jsonify({'Deleted': country_id})


if __name__ == "__main__":
    app.run(debug=True)