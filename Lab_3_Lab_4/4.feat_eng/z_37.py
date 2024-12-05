import pandas as pd


# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Создайте новый столбец, хранящий сезон, в котором было произведено 
последнее обновление приложения. ''')


def season_search(text):
    if text in ['January', 'February', 'December']:
        return 'Зима'
    elif text in ['March', 'April', 'May']:
        return 'Весна'
    elif text in ['June', 'July', 'August']:
        return 'Лето'
    else:
        return 'Осень' 


df['Season name'] = df['Last Updated'].str.split(' ').str[0].apply(season_search)


print(df)


