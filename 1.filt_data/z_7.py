import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Укажите среднее арифметическое и медиану количества установок приложений.")


print(f"Среднее количество установок: {df['Installs'].mean()}")
print(f"Медиана количества установок: {df['Installs'].median()}")


