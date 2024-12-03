import pandas as pd

df = pd.read_csv('Lab_3_Lab_4\GoogleApps.csv')

# print(df)
print(f"На сколько максимальное количество отзывов для бесплатных приложений")
print(f"тип 'Free') больше максимального количества отзывов для платных ")
print(f"приложений? ")


print(f"Разница в максимальном количестве отзывов: {df[df['Type'] == 'Free']['Reviews'].max() - df[df['Type'] == 'Paid']['Reviews'].max()}")


