# Программа анализа .csv файлов

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import numpy as np
import pandas as pd
import chardet
import re

# Создание главного окна
window = tk.Tk()
window.geometry("900x690")
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

label_191 = tk.Label(window, text = "Ссылка", font = ('Helvetica', 10, 'bold'), fg = '#008800')
label_191.place(x=220, y=530)

label_200 = tk.Label(window, text = "Номер столбца", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_200.place(x=40, y=550)

label_201 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_201.place(x=220, y=550)

label_210 = tk.Label(window, text = "Количество значений", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_210.place(x=40, y=575)

label_211 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_211.place(x=220, y=575)

label_221 = tk.Label(window, text = "Пол", font = ('Helvetica', 10, 'bold'), fg = '#008800')
label_221.place(x=220, y=610)

label_230 = tk.Label(window, text = "Номер столбца", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_230.place(x=40, y=630)

label_231 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_231.place(x=220, y=630)

label_240 = tk.Label(window, text = "Количество значений", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_240.place(x=40, y=655)

label_241 = tk.Label(window, text = "", font = ('Helvetica', 10, 'bold'), fg = '#000000')
label_241.place(x=220, y=655)

# Диалог открытия файла
def do_dialog():
    my_dir = os.getcwd()
    name=fd.askopenfilename(initialdir=my_dir)
    return name
    
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

# Выборка столбца в список
def get_list_column(df, column_ix):
    cnt_rows = df.shape[0]
    lst = []
    for i in range(cnt_rows):
        lst.append(df.iat[i, column_ix])
    return lst

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

file_name = do_dialog()
df = pandas_read_csv(file_name)
arr = find_tel_number_column(df)
print(arr)

# Подсчет количества телефонов в найденных столбцах
def count_tel_number(df):
    numbers = find_tel_number_column(df)
    arr1 = []
    b=0
    for index, item in enumerate(numbers):
        if item <= 1: 
            b = 0
        else:
            lst = get_list_column(df, index)
            mySeries = pd.Series(lst)
            data = mySeries.value_counts()
            b = len(data)
        arr1.append(b)
    return arr1

arr1 = count_tel_number(df)
print(arr1)
print(type(arr1))

# Вывод результата по email
def get_result_email(file_name):
    df = pandas_read_csv(file_name)
    try:
        index, max_number = get_max_column(df)
        label_21['text'] = index
        label_31['text'] = max_number        
    except:
        label_21['text'] = 'нет данных'
        label_31['text'] = 'нет данных'

# Обработчик нажатия кнопки
def process_button():
    file_name=do_dialog()
    label_01['text'] = file_name
    get_result_email(file_name)
    fill_telephone_label(file_name)
    #get_result_firstname(file_name)
    #get_result_lastname(file_name)
    #get_result_secondname(file_name)
    #get_result_address(file_name)
    #get_result_link(file_name)
    #get_result_gender(file_name)
    mb.showinfo(title=file_name, message = "Готово")

# Создание кнопки
button = tk.Button(window, text="Прочитать файл", command=process_button)
button.grid(row=4, column=1)

# Запуск цикла mainloop
window.mainloop()
