import pandas as pd

df = pd.read_csv('Lab_3_Lab_4\GoogleApps.csv')

# print(df)
print(f"Сгруппируйте платные приложения по категории и целевой аудитории. ")
print(f"Посчитай среднее количество отзывов в каждой группе. Выберите названия ") 
print(f"категорий, в которых есть платные приложения для всех возрастных групп и ")
print(f"расположите их в алфавитном порядке.") 


paid_apps = df[df['Type'] == 'Paid']

paid_reviews_grouped = paid_apps.groupby(['Category', 'Content Rating'])['Reviews'].mean().round(1).reset_index()

# Выбор категорий с приложениями для всех возрастных групп
all_groups = paid_reviews_grouped.groupby('Category').filter(lambda x: len(x['Content Rating'].unique()) == len(df['Content Rating'].unique()))
categories_with_all_groups = sorted(all_groups['Category'].unique())

print("\nКатегории с платными приложениями для всех возрастных групп:")
print(categories_with_all_groups)


