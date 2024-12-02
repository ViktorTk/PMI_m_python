import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"К какой категории относится приложение с самым большим количеством")
print(f"отзывов?")


print(f"Категория приложения с самым большим количеством отзывов: {df.loc[df['Reviews'].idxmax()]['Category']}")


