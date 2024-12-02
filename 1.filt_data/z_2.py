import pandas as pd

df = pd.read_csv('GoogleApps.csv')

# print(df)
print(f"К какой категории относится приложение, расположенное последним в наборе данных? ")


print(f"{df.iloc[-1]['Category']}")


