import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Сколько столбцов содержится в наборе данных?")
print(f"{df.shape[1]}")


