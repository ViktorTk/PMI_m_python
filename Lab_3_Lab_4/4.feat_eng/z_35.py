import pandas as pd


# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Чему равен максимальный доход среди платных приложений? ''')

stonks = df[['App', 'Price']]
group_dev_stonks = stonks.groupby('App').sum()
max_stonks = group_dev_stonks[group_dev_stonks['Price'] == group_dev_stonks['Price'].max()]


print(max_stonks)


