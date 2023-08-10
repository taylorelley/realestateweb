class PropertyAnalyser:
    def __init__(self, properties):
        self.properties = properties

    def find_undervalued(self):
        # For simplicity, let's say a property is undervalued if its price is below the average price.
        average_price = sum(property.price for property in self.properties) / len(self.properties)
        return [property for property in self.properties if property.price < average_price]
