import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Каков средний рейтинг приложений стоимостью более 20 долларов и с")
print(f"количеством установок более 10000?")


print(f"Средний рейтинг для приложений (цена > 20$ и установки > 10000): {df[(df['Price'] > 20) & (df['Installs'] > 10000)]['Rating'].mean()}")


