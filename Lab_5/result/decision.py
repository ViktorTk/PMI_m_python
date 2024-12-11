import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score


df = pd.read_csv('Lab_5/titanic.csv')


def fill_age(row):# row – это Series конкретного пассажира
 # Тело функции...
    age_1 = df[df['Pclass'] == 1]['Age'].median()
    age_2 = df[df['Pclass'] == 2]['Age'].median()
    age_3 = df[df['Pclass'] == 3]['Age'].median()
    if pd.isnull(row['Age']):
        if row['Pclass'] == 1:
            return age_1
        if row['Pclass'] == 2:
            return age_2
        return age_3
    return row['Age']

def fill_sex(sex):
    if sex == 'male':
        return 1
    return 0


print(df.head())
print(df.groupby('Sex')['Survived'].mean())
print(df.pivot_table(index = 'Survived', columns = 'Pclass',
values = 'Age', aggfunc = 'mean'))
df.drop(['PassengerId', 'Name', 'Ticket', 'Cabin'],axis = 1,
inplace = True)
print(df['Embarked'].value_counts())
df['Embarked'].fillna('S', inplace = True)
print(df.groupby('Pclass')['Age'].median())
df['Age'] = df.apply(fill_age, axis = 1)
df['Sex'] = df['Sex'].apply(fill_sex)
print(pd.get_dummies(df['Embarked']))
df[list(pd.get_dummies(df['Embarked']).columns)] = pd.get_dummies(df['Embarked'])
df.drop('Embarked', axis = 1, inplace = True)


def is_alone(row):
    if row['SibSp'] + row['Parch'] == 0:
        return 1
    return 0
df['Alone'] = df.apply(is_alone, axis = 1)

print(df.pivot_table(values = 'Age', columns = 'Alone',
index = 'Survived', aggfunc = 'count'))
print(df.head())
x = df.drop('Survived', axis = 1) # Данные о пассажирах
y = df['Survived'] # Целевая переменная

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)

sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
classifier = KNeighborsClassifier(n_neighbors = 3)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
percent = accuracy_score(y_test, y_pred) * 100


# Применяем 1 вариант решения:
TP, TN, FP, FN = 0, 0, 0, 0
for test, pred in zip(y_test, y_pred):
    if test - pred == 0:
        if test == 1:
            TP += 1
        else:
            TN += 1
    else:
        if test == 1:
            FN += 1
        else:
            FP += 1

#алгоритм распределения по категориям
print('Верный прогноз: выжившие -', TP, 'погибшие -', TN)
print('Ошибочный прогноз: выжившие -', FP, 'погибшие -', FN)
confusion_matrix(y_test, y_pred)


