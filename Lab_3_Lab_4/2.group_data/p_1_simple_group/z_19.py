import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps.csv')


print(f"Сколько приложений с рейтингом строго больше 4.5 в категории ‘FINANCE’?")


finance_apps = df[df['Category'] == 'FINANCE']
high_rating_finance_apps = finance_apps[finance_apps['Rating'] > 4.5]
num_high_rating_finance_apps = high_rating_finance_apps.shape[0]


print(num_high_rating_finance_apps)


