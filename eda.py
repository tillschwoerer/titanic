import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import sklearn

df = pd.read_csv('titanic.csv')
df.head()
df.tail()
df.describe()
df.info()

df.value_counts('type')
