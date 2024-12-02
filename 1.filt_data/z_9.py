import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"Чему равно медианное количество установок приложений из категории «ART_AND_DESIGN»? ")


print(f"Самое дешёвое платное приложение из категории «ART_AND_DESIGN» стоит: {df[df['Category'] == 'ART_AND_DESIGN']['Installs'].median()}")


