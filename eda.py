import pandas as pd

df = pd.read_csv('titanic.csv')
df.head()
df.tail()
df.describe()
df.info()

df.value_counts('type')
