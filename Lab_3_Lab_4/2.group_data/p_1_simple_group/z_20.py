import pandas as pd

# Читаем данные из CSV файла
df = pd.read_csv('Lab_3_Lab_4/GoogleApps.csv')


print(f"Чему равно соотношение бесплатных и платных игр с рейтингом больше 4.9?")


# Фильтруем игры, рейтинг которых больше 4.9
high_rating_games = df[(df['Category'] == 'GAME') & (df['Rating'] > 4.9)]

# Разделяем на бесплатные и платные
free_games = high_rating_games[high_rating_games['Price'] == 0]
paid_games = high_rating_games[high_rating_games['Price'] > 0]

# Соотношение
games_ratio = (free_games.shape[0] / paid_games.shape[0]) if paid_games.shape[0] > 0 else 0


print(games_ratio)


