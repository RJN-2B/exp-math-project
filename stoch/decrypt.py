import pandas as pd

print("hello world")
df = pd.read_csv('AustenCount.txt', sep=" ", header=None)
df.head()