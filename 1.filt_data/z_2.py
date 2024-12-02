import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Категория последней строки: {df.iloc[-1]['Category']}")


