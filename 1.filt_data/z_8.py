import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Сколько стоит самое дешёвое платное приложение (тип — ‘Paid’)?")
print(f"Самое дешёвое платное приложение (тип — ‘Paid’) стоит: {df[df['Type'] == 'Paid']['Price'].min()}")


