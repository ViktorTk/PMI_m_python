import pandas as pd

df = pd.read_csv('Lab_3_Lab_4\GoogleApps.csv')

# print(df)
print(f"Сколько стоит самое дорогое приложение?")


print(f"{df['Price'].max()}")


