import pandas as pd

df = pd.read_csv('Lab_3_Lab_4\GoogleApps.csv')

# print(df)
print(f"Выведите на экран минимальный, средний и максимальный рейтинг платных ")
print(f"и бесплатных приложений с точностью до десятых")


free_apps = df[df['Type'] == 'Free']
paid_apps = df[df['Type'] == 'Paid']

free_ratings = free_apps['Rating'].agg(['min', 'mean', 'max']).round(1)
paid_ratings = paid_apps['Rating'].agg(['min', 'mean', 'max']).round(1)

print("Рейтинг бесплатных приложений:")
print(free_ratings)
print("\nРейтинг платных приложений:")
print(paid_ratings)


