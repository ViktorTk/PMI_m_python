import pandas as pd


# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Вычислите, сколько долларов разработчики заработали на каждом платном 
приложении. ''')

# Опциональное условие, чтобы в выборке участвовали только платные приложения
df = df[df['Price'] > 0]

stonks = df[['App', 'Price']]
group_dev_stonks = stonks.groupby('App').sum()


print(group_dev_stonks)


