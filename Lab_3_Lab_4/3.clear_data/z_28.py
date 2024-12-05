import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Чему равен максимальный размер приложений из категории ‘TOOLS’? ''')


tools_apps = df[df['Category'] == 'TOOLS']
max_size_tools = tools_apps['Size'].max()


print(f"Максимальный размер приложения в категории 'TOOLS': {max_size_tools} MB")


