import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps.csv')


print(f'''Чему равно соотношение количества приложений для подростков и для
детей старше 10? ''')


teen_apps = df[df['Content Rating'] == 'Teen']
children_apps = df[df['Content Rating'] == 'Everyone 10+']

ratio = (teen_apps.shape[0] / children_apps.shape[0]) if children_apps.shape[0] > 0 else 0


print(f"Ответ: {ratio}")


