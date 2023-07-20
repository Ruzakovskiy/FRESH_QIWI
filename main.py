import pandas as pd

# currency_rates --code=USD --date=2022-10-08 # формат запроса

try:
    x = input() # ввод данных пользователя

    #убираем из переменной x не нужные слова
    removal_list = ['currency_rates', '--code=', '--date=']
    for word in removal_list:
        x = x.replace(word, "")

    #разделяем значения на валюту и дату
    x = x.split()

    #print(x) #проверка значения преобразованного x

    code = x[0] # хранение значения с валютой

    date = x[1] # хранение значения с датой
    date = date.replace('-','/') # форматирование значения даты, для правильного взаимодействия с ссылкой
    date = date.split('/') # преобразуем строку в массив
    date = list(reversed(date)) # переворачиваем массив
    date = '/'.join(date) # делаем из массива обратно строку

    #print(currency,date) # проверка значений date и currency

    url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=' + date #ссылка на XML с изменяющейся датой
    df = pd.read_xml(url, encoding='cp1251') #считываем даннные из XML и записываем в датафрейм
    #print(df) #проверка данных в датафрейме, где хранятся все данные, запарсенные из XML

    size_df = df.shape #узнаем размер датафрейма по колонкам и строкам
    size_df = int(size_df[0]) #оставляем значение размера датафрейма только по колонкам

    #print(size_df) проверка размера массива

    #вывод данных в нужном формате
    for i in range(0, size_df + 1):
        if code == df['CharCode'].iloc[i]:
            print(df['CharCode'].iloc[i], '(', df['Name'].iloc[i], ')', ':', df['Value'].iloc[i])
            break

except:
    print('Неверно введен запрос!')






