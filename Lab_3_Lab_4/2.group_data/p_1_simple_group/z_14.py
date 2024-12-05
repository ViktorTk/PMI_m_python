import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps.csv')


print(f"Сколько всего приложений с категорией ‘BUSINESS’? ")


business_apps = df[df['Category'] == 'BUSINESS']
num_business_apps = business_apps.shape[0]


print(f"Ответ: {num_business_apps}")


