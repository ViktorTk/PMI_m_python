import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Данные какого типа хранятся в каждом из столбцов?")


print(f"{df.dtypes}")


