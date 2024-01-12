# Программа анализа .csv файлов
import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import numpy as np
import pandas as pd
import chardet
import re


#DESIGN
# Создание главного окна
window = tk.Tk()
window.geometry("600x550")
window.title("Программа анализа .csv файлов")

# Создание меток вывода
label_00 = tk.Label(window, text = "Файл: ", font = ('Helvetica', 10, 'bold'), fg = '#0000CC')
label_00.place(x=40, y=25)

label_01 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#0000CC')
label_01.place(x=105, y=25)

label_11 = tk.Label(window, text = "Email", font = ('Helvetica', 10, 'bold'), fg = '#008800')
label_11.place(x=220, y=50)

label_20 = tk.Label(window, text = "Номер столбца", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_20.place(x=40, y=70)

label_21 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_21.place(x=220, y=70)

label_30 = tk.Label(window, text = "Количество значений", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_30.place(x=40, y=95)

label_31 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_31.place(x=220, y=95)

label_41 = tk.Label(window, text = "Телефон", font = ('Helvetica', 10, 'bold'), fg = '#008800')
label_41.place(x=220, y=130)

label_50 = tk.Label(window, text = "Номер столбца", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_50.place(x=40, y=150)

label_51 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_51.place(x=220, y=150)

label_52 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_52.place(x=320, y=150)

label_60 = tk.Label(window, text = "Количество значений", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_60.place(x=40, y=175)

label_61 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_61.place(x=220, y=175)

label_62 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_62.place(x=320, y=175)

label_71 = tk.Label(window, text = "Имя", font = ('Helvetica', 10, 'bold'), fg = '#008800')
label_71.place(x=220, y=210)

label_80 = tk.Label(window, text = "Номер столбца", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_80.place(x=40, y=230)

label_81 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_81.place(x=220, y=230)

label_90 = tk.Label(window, text = "Количество значений", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_90.place(x=40, y=255)

label_91 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_91.place(x=220, y=255)

label_101 = tk.Label(window, text = "Фамилия", font = ('Helvetica', 10, 'bold'), fg = '#008800')
label_101.place(x=220, y=290)

label_110 = tk.Label(window, text = "Номер столбца", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_110.place(x=40, y=310)

label_111 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_111.place(x=220, y=310)

label_120 = tk.Label(window, text = "Количество значений", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_120.place(x=40, y=335)

label_121 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_121.place(x=220, y=335)

label_131 = tk.Label(window, text = "Отчество", font = ('Helvetica', 10, 'bold'), fg = '#008800')
label_131.place(x=220, y=370)

label_140 = tk.Label(window, text = "Номер столбца", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_140.place(x=40, y=390)

label_141 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_141.place(x=220, y=390)

label_150 = tk.Label(window, text = "Количество значений", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_150.place(x=40, y=415)

label_151 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_151.place(x=220, y=415)

label_161 = tk.Label(window, text = "Адрес", font = ('Helvetica', 10, 'bold'), fg = '#008800')
label_161.place(x=220, y=450)

label_170 = tk.Label(window, text = "Номер столбца", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_170.place(x=40, y=470)

label_171 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_171.place(x=220, y=470)

label_180 = tk.Label(window, text = "Количество значений", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_180.place(x=40, y=495)

label_181 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_181.place(x=220, y=495)

# ~ label_191 = tk.Label(window, text = "Ссылка", font = ('Helvetica', 10, 'bold'), fg = '#008800')
# ~ label_191.place(x=220, y=530)

# ~ label_200 = tk.Label(window, text = "Номер столбца", font = ('Helvetica', 10, 'bold'), fg = '#000000')
# ~ label_200.place(x=40, y=550)

# ~ label_201 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
# ~ label_201.place(x=220, y=550)

# ~ label_210 = tk.Label(window, text = "Количество значений", font = ('Helvetica', 10, 'bold'), fg = '#000000')
# ~ label_210.place(x=40, y=575)

# ~ label_211 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
# ~ label_211.place(x=220, y=575)

# ~ label_221 = tk.Label(window, text = "Пол", font = ('Helvetica', 10, 'bold'), fg = '#008800')
# ~ label_221.place(x=220, y=610)

# ~ label_230 = tk.Label(window, text = "Номер столбца", font = ('Helvetica', 10, 'bold'), fg = '#000000')
# ~ label_230.place(x=40, y=630)

# ~ label_231 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
# ~ label_231.place(x=220, y=630)

# ~ label_240 = tk.Label(window, text = "Количество значений", font = ('Helvetica', 10, 'bold'), fg = '#000000')
# ~ label_240.place(x=40, y=655)

# ~ label_241 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
# ~ label_241.place(x=220, y=655)


#COMMON
# Диалог открытия файла
def do_dialog():
    my_dir = os.getcwd()
    name=fd.askopenfilename(initialdir=my_dir)
    return name

# Выборка столбца в список
def get_list_column(df, column_ix):
    cnt_rows = df.shape[0]
    lst = []
    for i in range(cnt_rows):
        lst.append(df.iat[i, column_ix])
    return lst

# Обработка csv файла при помощи pandas
def pandas_read_csv(file_name):
    with open(file_name, 'rb') as f:
        result = chardet.detect(f.read())
        if 'utf' in result['encoding'] :
            encoding = 'utf-8'
        else:
            encoding = 'Windows-1251'
        df = pd.read_csv(file_name, header=0, sep=';', encoding=encoding, dtype=str)
    return df



# EMAIL
# Подсчет количества emails в столбце
def count_email(df):
    cnt_columns = df.shape[1]
    arr = []
    for i in range(cnt_columns):
        try:
            lst = get_list_column(df, i)
            a = 0
            for item in lst:
                if '@' in item:
                    a += 1
        except:
            continue
        finally:
            arr.append(a)
    return arr

# Определение столбца с максимальным числом emails
def get_max_column(df):
    numbers = count_email(df)
    max_number = numbers[0]
    for item in numbers:
        if item > max_number:
            max_number = item
            index = numbers.index(max_number)+1
    return index, max_number



#TELEPHONE
# Поиск столбцов с номерами телефонов по заданным шаблонам
def find_tel_number_column(df):
    cnt_columns = df.shape[1]
    arr = []
    for i in range(cnt_columns):
        lst = get_list_column(df, i)
        a = 0
        for item in lst:
            if isinstance(item, float) and np.isnan(item):
                continue
            elif re.findall(r'[(]\d{3}[)]\d{3}[-]\d{4}', item):
                a += 1
            elif re.findall(r'\d{3}[-]\d{4}', item):
                a += 1
            elif re.findall(r'(\d){11}', item):
                a += 1
        arr.append(a)
    return arr

# Подсчет количества телефонов в найденных столбцах
def count_tel_number(df):
    numbers = find_tel_number_column(df)
    arr1 = []
    b=0
    for index, item in enumerate(numbers):
        if item <= 1: 
            b = 0
        else:
            lst = get_list_column(df, index)   # получаю столбец из таблицы
            mySeries = pd.Series(lst)          # делаю из этого столбца массив pandas Series индекс / значение
            data = mySeries.value_counts()     # сверачиваю массив данных по уникальным значениям и считаю их частотность
            # ~ print(data)
            b = sum(data)                      # суммирую количество данных. Если нужно вывести количество уникальных значений, можно написать len(data)
        arr1.append(b)
    return arr1

# Определение результата по telephone
def get_result_telephone(df):
    arr1 = count_tel_number(df)
    arr2 = []
    arr3 = []
    for index, item in enumerate(arr1):
        if item <= 0:
            continue
        else:
            a = index+1
            arr2.append(a)
            b = item
            arr3.append(b)
    return arr2, arr3

# ~ file_name = do_dialog()
# ~ df = pandas_read_csv(file_name)
# ~ arr = find_tel_number_column(df)
# ~ print(arr)
# ~ arr1 = count_tel_number(df)
# ~ print(arr1)
# ~ print(type(arr1))
# ~ result = get_result_telephone(df)
# ~ print(result)
# ~ print(type(result))



#FIRSTNAME
# Поиск столбцов с именами по заданным шаблонам
def find_firstname_column(df):
    cnt_columns = df.shape[1]
    arfn = []
    for i in range(cnt_columns):
        lst = get_list_column(df, i)
        a = 0
        for item in lst:
            if isinstance(item, float) and np.isnan(item):
                continue
            elif re.findall(r'Александр\b|Анна\b|Михаил\b|Ольга\b', item):
                a += 1
        arfn.append(a)
    return arfn

# Подсчет количества имен в найденных столбцах
def count_firstname(df):
    numbers = find_firstname_column(df)
    arfn1 = []
    b=0
    for index, item in enumerate(numbers):
        if item <= 0: 
            b = 0
        else:
            lst = get_list_column(df, index)   # получаю столбец из таблицы
            mySeries = pd.Series(lst)          # селаю из этого столбца массив pandas Series индекс / значение
            # ~ print(mySeries[421])           # проверяю по файлу Contact.csv типа данных в ячейке со значением NaN
            # ~ print(type(mySeries[421]))
            data = mySeries.value_counts()     # сверачиваю массив данных по уникальным значениям и считаю их частотность
            # ~ print(data)
            b = sum(data)                      # суммирую количество данных. Если нужно вывести количество уникальных значений, можно написать len(data)
        arfn1.append(b)
    return arfn1

# Определение результата по firstname
def get_result_firstname(df):
    arfn1 = count_firstname(df)
    arfn2 = []
    arfn3 = []
    for index, item in enumerate(arfn1):
        if item <= 0:
            continue
        else:
            a = index+1
            arfn2.append(a)
            b = item
            arfn3.append(b)
    return arfn2, arfn3

# ~ file_name = do_dialog()
# ~ df = pandas_read_csv(file_name)
# ~ arfn = find_firstname_column(df)
# ~ print(arfn)
# ~ print(type(arfn))
# ~ arfn1 = count_firstname(df)
# ~ print(arfn1)
# ~ result = get_result_firstname(df)
# ~ print(result)
# ~ print(type(result))



#LASTNAME
# Поиск столбцов с фамилиями по заданным шаблонам
def find_lastname_column(df):
    cnt_columns = df.shape[1]
    arln = []
    for i in range(cnt_columns):
        lst = get_list_column(df, i)
        a = 0
        for item in lst:
            if isinstance(item, float) and np.isnan(item):
                continue
            elif re.findall(r'ова\b', item):
                a += 1
        arln.append(a)
    return arln

# Подсчет количества фамилий в найденных столбцах
def count_lastname(df):
    numbers = find_lastname_column(df)
    arln1 = []
    b=0
    for index, item in enumerate(numbers):
        if item <= 0: 
            b = 0
        else:
            lst = get_list_column(df, index)
            mySeries = pd.Series(lst)
            data = mySeries.value_counts()
            # ~ print(data)
            b = sum(data)
        arln1.append(b)
    return arln1

# Определение результата по lastname
def get_result_lastname(df):
    arln1 = count_lastname(df)
    arln2 = []
    arln3 = []
    for index, item in enumerate(arln1):
        if item <= 0:
            continue
        else:
            a = index+1
            arln2.append(a)
            b = item
            arln3.append(b)
    return arln2, arln3

# ~ file_name = do_dialog()
# ~ df = pandas_read_csv(file_name)
# ~ arln = find_lastname_column(df)
# ~ print(arln)
# ~ print(type(arln))
# ~ arln1 = count_lastname(df)
# ~ print(arln1)
# ~ result = get_result_lastname(df)
# ~ print(result)
# ~ print(type(result))



#SECONDNAME
# Поиск столбцов с отчествами по заданным шаблонам
def find_secondname_column(df):
    cnt_columns = df.shape[1]
    arsn = []
    for i in range(cnt_columns):
        lst = get_list_column(df, i)
        a = 0
        for item in lst:
            if isinstance(item, float) and np.isnan(item):
                continue
            elif re.findall(r'\Bвич|\Bвна', item):
                a += 1
        arsn.append(a)
    return arsn

# Подсчет количества отчеств в найденных столбцах
def count_secondname(df):
    numbers = find_secondname_column(df)
    arsn1 = []
    b=0
    for index, item in enumerate(numbers):
        if item <= 0: 
            b = 0
        else:
            lst = get_list_column(df, index)
            mySeries = pd.Series(lst) 
            data = mySeries.value_counts()
            # ~ print(data)
            b = sum(data)
        arsn1.append(b)
    return arsn1

# Определение результата по secondname
def get_result_secondname(df):
    arsn1 = count_secondname(df)
    arsn2 = []
    arsn3 = []
    for index, item in enumerate(arsn1):
        if item <= 0:
            continue
        else:
            a = index+1
            arsn2.append(a)
            b = item
            arsn3.append(b)
    return arsn2, arsn3

# ~ file_name = do_dialog()
# ~ df = pandas_read_csv(file_name)
# ~ arsn = find_secondname_column(df)
# ~ print(arsn)
# ~ print(type(arsn))
# ~ arsn1 = count_secondname(df)
# ~ print(arsn1)
# ~ result = get_result_secondname(df)
# ~ print(result)
# ~ print(type(result))



#ADDRESS
# Поиск столбцов с адресами по заданным шаблонам
def find_address_column(df):
    cnt_columns = df.shape[1]
    arad = []
    for i in range(cnt_columns):
        lst = get_list_column(df, i)
        a = 0
        for item in lst:
            if isinstance(item, float) and np.isnan(item):
                continue
            elif re.findall(r'ул\.|str\.', item):
                a += 1
        arad.append(a)
    return arad

# Подсчет количества адресов в найденных столбцах
def count_address(df):
    numbers = find_address_column(df)
    arad1 = []
    b=0
    for index, item in enumerate(numbers):
        if item <= 0: 
            b = 0
        else:
            lst = get_list_column(df, index)
            mySeries = pd.Series(lst)
            data = mySeries.value_counts()
            # ~ print(data)
            b = sum(data)
        arad1.append(b)
    return arad1

# Определение результата по address
def get_result_address(df):
    arad1 = count_address(df)
    arad2 = []
    arad3 = []
    for index, item in enumerate(arad1):
        if item <= 0:
            continue
        else:
            a = index+1
            arad2.append(a)
            b = item
            arad3.append(b)
    return arad2, arad3

# ~ file_name = do_dialog()
# ~ df = pandas_read_csv(file_name)
# ~ arad = find_address_column(df)
# ~ print(arad)
# ~ print(type(arad))
# ~ arad1 = count_address(df)
# ~ print(arad1)
# ~ result = get_result_address(df)
# ~ print(result)
# ~ print(type(result))




#RESULTS
# Вывод результата по email
def fill_email_label(file_name):
    df = pandas_read_csv(file_name)
    try:
        index, max_number = get_max_column(df)
        label_21['text'] = index
        label_31['text'] = max_number        
    except:
        label_21['text'] = 'нет данных'
        label_31['text'] = 'нет данных'

# Вывод результата по telephone
def fill_telephone_label(file_name):
    df = pandas_read_csv(file_name)    
    arr2, arr3 = get_result_telephone(df)
    if arr2 and arr3:
        label_51['text'] = arr2
        label_61['text'] = arr3
    else: 
        label_51['text'] = 'нет данных'
        label_61['text'] = 'нет данных'
    
# Вывод результата по firstname
def fill_firstname_label(file_name):
    df = pandas_read_csv(file_name)
    arfn2, arfn3 = get_result_firstname(df)
    if arfn2 and arfn3:
        label_81['text'] = arfn2
        label_91['text'] = arfn3        
    else:
        label_81['text'] = 'нет данных'
        label_91['text'] = 'нет данных'

# Вывод результата по lastname
def fill_lastname_label(file_name):
    df = pandas_read_csv(file_name)
    arln2, arln3 = get_result_lastname(df)
    if arln2 and arln3:
        label_111['text'] = arln2
        label_121['text'] = arln3        
    else:
        label_111['text'] = 'нет данных'
        label_121['text'] = 'нет данных'

# Вывод результата по secondname
def fill_secondname_label(file_name):
    df = pandas_read_csv(file_name)
    arsn2, arsn3 = get_result_secondname(df)
    if arsn2 and arsn3:
        label_141['text'] = arsn2
        label_151['text'] = arsn3        
    else:
        label_141['text'] = 'нет данных'
        label_151['text'] = 'нет данных'

# Вывод результата по address
def fill_address_label(file_name):
    df = pandas_read_csv(file_name)
    arad2, arad3 = get_result_address(df)
    if arad2 and arad3:
        label_171['text'] = arad2
        label_181['text'] = arad3        
    else:
        label_171['text'] = 'нет данных'
        label_181['text'] = 'нет данных'

# ~ # Вывод результата по link
# ~ def get_result_link(file_name):
    # ~ df = pandas_read_csv(file_name)
    # ~ try:
        # ~ index, max_number = get_max_column(df)
        # ~ label_201['text'] = index
        # ~ label_211['text'] = max_number        
    # ~ except:
        # ~ label_201['text'] = 'нет данных'
        # ~ label_211['text'] = 'нет данных'

# ~ # Вывод результата по gender
# ~ def get_result_gender(file_name):
    # ~ df = pandas_read_csv(file_name)
    # ~ try:
        # ~ index, max_number = get_max_column(df)
        # ~ label_231['text'] = index
        # ~ label_241['text'] = max_number        
    # ~ except:
        # ~ label_231['text'] = 'нет данных'
        # ~ label_241['text'] = 'нет данных'


# Обработчик нажатия кнопки
def process_button():
    file_name=do_dialog()
    label_01['text'] = file_name
    fill_email_label(file_name)
    fill_telephone_label(file_name)
    fill_firstname_label(file_name)
    fill_lastname_label(file_name)
    fill_secondname_label(file_name)
    fill_address_label(file_name)
    # ~ get_result_link(file_name)
    # ~ get_result_gender(file_name)
    mb.showinfo(title=file_name, message = "Готово")

# Создание кнопки
button = tk.Button(window, text="Прочитать файл", command=process_button)
button.grid(row=4, column=1)

# Запуск цикла mainloop
window.mainloop()
