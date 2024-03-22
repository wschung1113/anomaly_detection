import pandas as pd
import numpy as np

from scipy.io import arff


PATH = '/mnt/c/Users/wschu/OneDrive/Documents/data/creditcard_fraud'

# Load ARFF file
data, meta = arff.loadarff(PATH + "/creditcard_fraud.arff")

# Convert ARFF data to pandas DataFrame
df = pd.DataFrame(data)

# If you want to convert attribute names to column names
df.columns = meta.names()

# Save DataFrame to CSV file
df.to_csv(PATH + '/creditcard_fraud.csv', index=False)