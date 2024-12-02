import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Как называется приложение, расположенное первым в наборе данных? ")


print(f"{df.loc[0, 'App']}")


