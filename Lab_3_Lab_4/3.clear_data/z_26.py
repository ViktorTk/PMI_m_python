import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps_for_edit.csv')


print(f"Сколько в датасете приложений, у которых не указан рейтинг?")


missing_ratings = df[df['Rating'].isnull()]


print(f"Количество приложений без рейтинга: {len(missing_ratings)}")


