import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Сколько стоит самое дорогое приложение?")


print(f"{df['Price'].max()}")


