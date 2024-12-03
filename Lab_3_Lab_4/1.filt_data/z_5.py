import pandas as pd

df = pd.read_csv('Lab_3_Lab_4\GoogleApps.csv')

# print(df)
print(f"Укажите среднее арифметическое и медиану размера приложений.")


print(f"Средний размер приложений: {df['Size'].mean()}")
print(f"Медиана размера приложений: {df['Size'].median()}")


