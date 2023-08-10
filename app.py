from flask import Flask, jsonify, request
from property_data_fetcher import PropertyDataFetcher
from property_data_storage import PropertyDataStorage
from property_data_analyser import PropertyDataAnalyser

app = Flask(__name__)
fetcher = PropertyDataFetcher()
storage = PropertyDataStorage()
analyser = PropertyDataAnalyser()

@app.route('/properties', methods=['GET'])
def get_properties():
    properties = storage.get_all_properties()
    return jsonify(properties)

@app.route('/properties/<id>', methods=['GET'])
def get_property(id):
    property = storage.get_property_data(id)
    return jsonify(property)

@app.route('/undervalued_properties', methods=['GET'])
def get_undervalued_properties():
    undervalued_properties = analyser.find_undervalued_properties()
    return jsonify(undervalued_properties)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
