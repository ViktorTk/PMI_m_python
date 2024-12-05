import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Выведи информацию о всем DataFrame, чтобы узнать, какие столбцы
нуждаются в очистке. ''')


print(df.info())


