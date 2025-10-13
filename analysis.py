import pandas as pd
df = pd.read_csv('titanic.csv')

# First 5 lines
df.head()

# Get summary stats
df.describe()

# Column names
df.columns