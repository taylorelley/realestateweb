import pandas as pd

class PropertyDataAnalyser:
    def __init__(self, storage):
        self.storage = storage

    def find_undervalued_properties(self):
        properties = self.storage.get_all_properties()
        df = pd.DataFrame(properties)
        # Implement logic to find undervalued properties
