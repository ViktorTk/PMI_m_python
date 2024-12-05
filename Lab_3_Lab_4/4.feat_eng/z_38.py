import pandas as pd


# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Выведите на экран сезоны и их количество в датасете. ''')


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
df['Season Count'] = df.groupby(['Season name'])['Season name'].transform('count')


selection_columns = df[['Season name', 'Season Count']]
season_name_and_count = selection_columns.groupby('Season name').max()
season_name_and_count = season_name_and_count.sort_values(by='Season Count',ascending=False)


print(season_name_and_count)


