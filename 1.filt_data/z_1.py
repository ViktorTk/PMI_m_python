import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Название приложения, расположенного на 1 строке: {df.loc[0, 'App']}")


