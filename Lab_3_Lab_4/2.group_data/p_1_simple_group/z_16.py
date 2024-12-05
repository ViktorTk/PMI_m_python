import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps.csv')


print(f"Чему равен средний рейтинг платных приложений?")


paid_apps = df[df['Price'] > 0]
average_rating_paid = paid_apps['Rating'].mean()


print(f"Ответ: {average_rating_paid}")


