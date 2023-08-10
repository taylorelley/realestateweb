from realestate_api import RealEstateAPI
from database_handler import DatabaseHandler
from data_analyzer import DataAnalyzer
from web_interface import WebInterface

def main():
    # Create instances of the classes
    api = RealEstateAPI()
    db = DatabaseHandler()
    analyzer = DataAnalyzer()
    web = WebInterface()

    # Fetch all the data from the API
    data = api.fetch_all_data()

    # Store the data in the database
    db.store_data(data)

    # Analyze the data to find undervalued properties
    undervalued_properties = analyzer.find_undervalued_properties(data)

    # Display the results on the web interface
    web.display_results(undervalued_properties)

if __name__ == "__main__":
    main()
