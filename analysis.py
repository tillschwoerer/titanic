import pandas as pd
import seaborn as sns

df = pd.read_csv('titanic.csv')
df.head()

df.info()
df.columns

sns.histplot(df, x='price')
sns.scatterplot(df, x='price', y='age')

df.tail()

print('Hello, Till')
