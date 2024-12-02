import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Каков минимальный размер приложения для тинейджеров (рейтинг контента")
print(f"— 'Teen')?")


print(f"Минимальный размер приложения для тинейджеров: {df[df['Content Rating'] == 'Teen']['Size'].min()}")


