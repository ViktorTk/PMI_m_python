import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Замените тип данных на дробное число для цен приложений. ''')


apps_with_price = df[['Price']].astype(float)
# apps_with_price = df.info()


print(apps_with_price.info())


