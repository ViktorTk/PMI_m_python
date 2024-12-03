import pandas as pd

df = pd.read_csv('Lab_3_Lab_4\GoogleApps.csv')

# print(df)
print(f"Выведите на экран минимальную, медианную и максимальную цену платных ")
print(f"приложений для разных целевых аудиторий.")


free_apps = df[df['Type'] == 'Free']
paid_apps = df[df['Type'] == 'Paid']

paid_apps_prices = paid_apps.groupby('Content Rating')['Price'].agg(['min', 'median', 'max']).round(2)
print("\nЦены платных приложений по целевым аудиториям:")
print(paid_apps_prices)


