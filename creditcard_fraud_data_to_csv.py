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

df['Class'] = df['Class'].apply(lambda x: int.from_bytes(x, byteorder='big')) - 48 # convert 48 --> 0, 49 --> 1

df_dropped = df.drop(columns='Time', axis=1)

# Save DataFrame to CSV file
df_dropped.to_csv(PATH + '/creditcard_fraud.csv', index=False)