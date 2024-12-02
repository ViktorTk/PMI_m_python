import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Среднее арифметическое и медиана размера приложений: ")
print(f"Средний размер приложений: {df['Size'].mean()}")
print(f"Медиана размера приложений: {df['Size'].median()}")


