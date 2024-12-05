import pandas as pd


# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Создайте новый столбец, в котором будет храниться количество жанров. 
Какое максимальное количество жанров хранится в датасете? ''')


df['Counts_Category'] = df.groupby(['Category'])['Category'].transform('count')


print(df)


