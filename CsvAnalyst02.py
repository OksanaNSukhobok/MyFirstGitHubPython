# Программа анализа .csv файлов

import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd
import os
import pandas as pd

# Создание главного окна
window = tk.Tk()
window.geometry("600x300")
window.title("Программа анализа .csv файлов")

# Создание меток вывода
label_00 = tk.Label(text = "Файл: ")
label_00.grid(row=0, column=0, padx=10, pady=10, sticky="e")

label_01 = tk.Label(text = "")
label_01.grid(row=0, column=1, sticky="w")

label_10 = tk.Label(text = "Заголовок")
label_10.grid(row=1, column=0, padx=10, pady=5, sticky="e")

label_11 = tk.Label(text = "")
label_11.grid(row=1, column=1, sticky="w")

label_20 = tk.Label(text = "Номер столбца: ")
label_20.grid(row=2, column=0, padx=10, pady=5, sticky="e")

label_21 = tk.Label(text = "")
label_21.grid(row=2, column=1, sticky="w")

label_30 = tk.Label(text = "Количество значений: ")
label_30.grid(row=3, column=0, padx=10, pady=5, sticky="e")

label_31 = tk.Label(text = "")
label_31.grid(row=3, column=1, sticky="w")

# Диалог открытия файла
def do_dialog():
    my_dir = os.getcwd()
    name=fd.askopenfilename(initialdir=my_dir)
    return name

# Обработка csv файла при помощи pandas
def pandas_read_csv(file_name):
    df = pd.read_csv(file_name, header=None, sep=';')
    cnt_rows = df.shape[0]
    cnt_columns = df.shape[1]
    label_11['text'] = 'Emails'
    label_21['text'] = cnt_columns
    label_31['text'] = cnt_rows
    return df

# Обработчик нажатия кнопки
def process_button():
    file_name=do_dialog()
    label_01['text'] = file_name
    pandas_read_csv(file_name)
    mb.showinfo(title=None, message = "Готово")

# Создание кнопки
button = tk.Button(window, text="Прочитать файл", command=process_button)
button.grid(row=4, column=1)

# Запуск цикла mainloop
window.mainloop()
