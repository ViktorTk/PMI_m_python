import pandas as pd

df = pd.read_csv('Lab_3_Lab_4\GoogleApps.csv')

# print(df)
print(f"Сгруппируйте данные по категории и целевой аудитории, посчитайте")
print(f"максимальное количество отзывов в каждой группе. Сравни результаты для") 
print(f"категорий ‘EDUCATION’, ‘FAMILY’ и ‘GAME’: В какой возрастной группе")
print(f"больше всего отзывов получило приложение из категории ‘EDUCATION’?") 
print(f"‘FAMILY’? ‘GAME’?")


reviews_grouped = df.groupby(['Category', 'Content Rating'])['Reviews'].max().reset_index()

categories = ['EDUCATION', 'FAMILY', 'GAME']
filtered_reviews = reviews_grouped[reviews_grouped['Category'].isin(categories)]

print("\nМаксимальное количество отзывов для категорий EDUCATION, FAMILY и GAME:")
print(filtered_reviews)

# Определение возрастной группы с наибольшим числом отзывов для каждой категории
for category in categories:
    top_group = filtered_reviews[filtered_reviews['Category'] == category].sort_values(by='Reviews', ascending=False).iloc[0]
    print(f"\nВ категории '{category}' больше всего отзывов ({top_group['Reviews']}) в возрастной группе '{top_group['Content Rating']}'.")


