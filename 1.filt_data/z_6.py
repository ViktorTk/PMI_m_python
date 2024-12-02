import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Самое дорогое приложение: ")
print(f"{df['Price'].max()}")


