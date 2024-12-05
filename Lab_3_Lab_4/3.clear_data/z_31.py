import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''У какого приложения не указан тип? Какой тип там необходимо записать в 
зависимости от цены? ''')


missing_type_apps = df[df['Type'].isnull()]

# Для каждого приложения без типа определим тип в зависимости от цены
def fill_type_based_on_price(row):
    if pd.isnull(row['Type']):
        if row['Price'] == 0:
            return 'Free'
        else:
            return 'Paid'
    return row['Type']

df['Type'] = df.apply(fill_type_based_on_price, axis=1)


# Проверим, есть ли еще записи без типа
missing_type_apps = df[df['Type'].isnull()]
print(f"Количество приложений без типа после обработки: {len(missing_type_apps)}")


