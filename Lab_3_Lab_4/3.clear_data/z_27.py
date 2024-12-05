import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f'''Определи, какое ещё значение размера хранится в датасете помимо 
Килобайтов и Мегабайтов, замени его на -1. Преобразуйте размеры 
приложений в числовой формат. Размер всех приложений должен 
измеряться в Мегабайтах.''')


def size_to_mb(size):
    if isinstance(size, str):
        if 'M' in size:
            return float(size.replace('M', '').replace(',', '').strip())
        elif 'K' in size:
            return float(size.replace('K', '').replace(',', '').strip()) / 1024  # конвертация из KB в MB
        else:
            return -1  # если размер в другой единице
    return -1

df['Size'] = df['Size'].apply(size_to_mb)

# Проверим, есть ли другие единицы измерения
unique_sizes = df['Size'].unique()


print("Уникальные размеры:", unique_sizes)


