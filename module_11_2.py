'''
import requests

# Спортивные новости без рекламы
response = requests.get('https://www.sport-express.ru/services/materials/news/se/')
print(response.ok)  # проверяем, успешен ли запрос
print(response.text)  # выводим полученный ответ на экран
'''

import pandas
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FormatStrFormatter, LinearLocator, FuncFormatter
'''
Изменения погоды в Москве за историю наблюдений
на основе статьи https://habr.com/ru/articles/469259/
'''

# Средние месячные и годовые температуры воздуха в Москве (по online данным и литературным источникам)
# http://www.pogodaiklimat.ru/history
df = pandas.read_csv("module_11_2_weather.csv", sep=';', encoding='utf-8')
print(df)
for m in ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек', 'за год']:
    df = df[(df[m] != 999.9)]
print(df)

plt.rcParams["figure.figsize"] = (8, 5)
fig, ax = plt.subplots()

plt.bar(df['год'].values, df['за год'].values, label=f'средняя температура за год, C')
# plt.bar(df['год'].values, df['июн'].values, label=f'Июнь, температура, C')
plt.plot(df['год'].values, df['за год'].rolling(window=20, min_periods=1).mean(), 'r-')
# plt.plot(df['год'].values, df['июн'].rolling(window=20, min_periods=1).mean(), 'r-')

plt.legend(loc='best')
plt.tight_layout()
plt.show()