import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Сгруппируйте данные по типу и целевой аудитории, посчитай среднее 
количество установок в каждой группе. Найдите ячейку с самым большим 
значением. К какой возрастной группе и типу приложений относятся данные 
из этой ячейки? ''')


grouped = df.groupby(['Type', 'Content Rating'])['Installs'].mean()

# Находим максимальное значение
max_installs_group = grouped.idxmax()
max_installs_value = grouped.max()


print(f"Самая большая ячейка - Тип: {max_installs_group[0]}")
print(f"Целевая аудитория: {max_installs_group[1]}")
print(f"Среднее количество установок: {max_installs_value}")


