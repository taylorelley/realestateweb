import pandas as pd
import numpy as np
from scipy import stats

class DataAnalyzer:
    def find_undervalued_properties(self, data):
        # Convert the data to a DataFrame
        df = pd.DataFrame(data)

        # Calculate the z-scores of the prices
        df['z_score'] = np.abs(stats.zscore(df['price']))

        # Properties with a z-score greater than 2 are considered undervalued
        undervalued_properties = df[df['z_score'] > 2]

        return undervalued_properties.to_dict('records')
