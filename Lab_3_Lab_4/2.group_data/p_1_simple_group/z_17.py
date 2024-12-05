import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps.csv')


print(f'''На сколько средний рейтинг бесплатных приложений меньше среднего
рейтинга платных приложений?''')


paid_apps = df[df['Price'] > 0]
average_rating_paid = paid_apps['Rating'].mean()

free_apps = df[df['Price'] == 0]
average_rating_free = free_apps['Rating'].mean()

rating_diff = average_rating_free - average_rating_paid


print(f"Ответ: {rating_diff}")


