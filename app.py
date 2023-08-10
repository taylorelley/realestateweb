from flask import Flask, render_template
from real_estate_api import RealEstateAPI
from property_analyser import PropertyAnalyser

app = Flask(__name__)

@app.route('/')
def index():
    api = RealEstateAPI()
    analyser = PropertyAnalyser(api.fetch_properties())
    undervalued_properties = analyser.find_undervalued()
    return render_template('index.html', properties=undervalued_properties)

if __name__ == '__main__':
    app.run(debug=True)
