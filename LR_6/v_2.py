""" 
Кейс № 2. Страны мира
 География, экономика и социология разных стран мира.
 ● 20 столбцов : численность населения | уровень миграции | 
показатель ВВП | уровень грамотности | количество телефонов | тип 
экономики | выход к морю и др.
 Идея продукта: социальная реклама.
 Рынок: рекламный рынок.
 Целевая аудитория: государственные учреждения.
 Пример исследовательского вопроса для изучения рынка: какие факторы влияют на 
качество жизни населения?
 Гипотеза: показатель ВВП зависит от уровня грамотности населения.
"""

# импорт библиотеки Pandas и Numpy
import pandas as pd
import numpy as np

# Читаем данные из CSV файла
df = pd.read_csv(r'LR_6\countries of the world.csv')



# Столбец Literacy (%) - 1) привели значение к числовому виду, 2) пустышки - заменил на NaN, 3) привели столбец к числовому (дробному) значению
df['Literacy (%)'] = df['Literacy (%)'].str.replace(',','.').fillna(np.nan).astype(float)

# Цикл для очистки выбранных столбцов от пустых значений:
for col in ['Literacy (%)', 'GDP ($ per capita)']:
    # print(col) # столбец, с которым проводится операция

    # print(df[df[col].isna()]['Country']) # вывод пустых значений по выбранному столбцу

    # Ищем среднее значение столбца 'GDP ($ per capita)', группируем по столбцу 'Region'
    avg_per_region = df.groupby('Region')[col].mean()

    # Соединяем датафрейм с найденными средними значениями по регионам (т.к. столбцы 'Literacy (%)' - имеют одинаковые названия - теперь называются 'Literacy (%)_x' и 'Literacy (%)_y')
    df = df.merge(avg_per_region, on=['Region'], how='left')

    # loc = фильтр
    df.loc[
        df[col + '_x'].isna() # выбор пустых значений из df
        , col + '_x' # выбор столбца, куда буду записывать значение
    ] = df.loc[
        df[col + '_x'].isna() # выбрали также пустые значения из df
        , col + '_y' # столбец из которого брал значения для df => среднее значение по региону
    ]

    # удалили лишний столбец - со средними значениями по региону
    del df[col + '_y']

    # переименовываем столбец в изначальное название
    df = df.rename(
        columns={
            col + '_x':col 
        }
    )
    
    # print(df.info())
    # print(df[df[col].isna()]['Country']) # проверка на NaN после обработки данных


# Поиск максимального значения из значений ВВП:
avg_per_GDP = df['GDP ($ per capita)'].max()

# определение % по уровню ВВП в сравнении с максимальным значением в списке:
df['percent_for_max_GDP'] = df['GDP ($ per capita)'] / df['GDP ($ per capita)'].max()


# Функция для определения рейтинга
def rating(value):
    if value < 0.15:
        return 'Очень низкий'
    elif value < 0.3:
        return 'Низкий'
    elif value < 0.65:
        return 'Средний'
    else:
        return 'Высокий'

# Применяем функцию к столбцу и создаем новый столбец с рейтингом
df['Rating_per_GDP'] = df['percent_for_max_GDP'].apply(rating)

# Среднее значение уровня образования, сгруппированное по рейтингу ВВП
avg_GDP_per_Lit = df.groupby('Rating_per_GDP')['Literacy (%)'].mean()


# Переименование Series и индекса
avg_GDP_per_Lit = avg_GDP_per_Lit.rename('Average Literacy Rate').rename_axis('GDP Rating')

# Преобразование Series в DataFrame для удобства сортировки
avg_GDP_per_Lit_df = avg_GDP_per_Lit.reset_index()

# Сортировка по столбцу 'GDP Rating'
avg_GDP_per_Lit_df = avg_GDP_per_Lit_df.sort_values(by='Average Literacy Rate', ascending=False)

print(avg_GDP_per_Lit_df)


