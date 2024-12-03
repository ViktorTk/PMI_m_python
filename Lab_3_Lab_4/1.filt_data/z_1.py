import pandas as pd

df = pd.read_csv('Lab_3_Lab_4\GoogleApps.csv')

# print(df)
print(f"Как называется приложение, расположенное первым в наборе данных? ")


print(f"{df.loc[0, 'App']}")


