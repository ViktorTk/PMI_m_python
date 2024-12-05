import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Замените тип данных на целочисленный для количества установок. В записи 
количества установок знак “+” необходимо игнорировать. ''')


# Преобразуем столбец 'Installs' в строковый тип перед заменой
df['Installs'] = df['Installs'].astype(str)  # Преобразуем в строку, чтобы использовать методы str
df['Installs'] = df['Installs'].str.replace(',', '')  # убираем запятые
df['Installs'] = df['Installs'].str.replace('+', '')  # убираем знак плюса
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')  # преобразуем в числовой формат


# Проверим тип данных
print(f"Тип данных в столбце 'Installs' {df['Installs'].dtype}")


