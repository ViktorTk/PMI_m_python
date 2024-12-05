import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps.csv')


print(f'''Чему равен минимальный и максимальный размер приложений в категории
'COMICS'?''')


# Преобразуем столбец 'Size' в строковый тип
df['Size'] = df['Size'].astype(str)

# Убираем любые символы (например, 'M' и 'k'), оставляем только числовую часть
df['Size'] = df['Size'].replace(r'[^\d\.]', '', regex=True)

# Преобразуем 'Size' обратно в числовой тип
df['Size'] = pd.to_numeric(df['Size'], errors='coerce')

# Учитываем категорию 'COMICS'
comics_apps = df[df['Category'] == 'COMICS']

# Находим минимальный и максимальный размер
min_size = comics_apps['Size'].min()
max_size = comics_apps['Size'].max()


print(f"Минимальный размер: {min_size} MB")
print(f"Максимальный размер: {max_size} MB")


