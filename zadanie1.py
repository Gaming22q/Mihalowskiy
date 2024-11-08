Проект: Анализатор данных с GUI
Этот проект представляет собой простое приложение для анализа данных с графическим интерфейсом (GUI), разработанное с использованием Python, библиотек Tkinter и pandas.

Функции:

Загрузка файла CSV через GUI.
Отображение таблицы данных.
Базовые операции анализа:
Подсчет среднего значения.
Поиск минимального и максимального значения.
Фильтрация строк по введенному значению.
Установка:

Убедитесь, что у вас установлены Python и библиотеки Tkinter и pandas.
Скачайте или клонируйте этот репозиторий.
Запустите файл data_analyzer.py.
Использование:

Нажмите кнопку “Загрузить файл”, чтобы выбрать CSV-файл.
Данные будут отображены в таблице.
Выберите столбец для анализа.
Нажмите кнопки «Среднее», «Минимум», «Максимум», чтобы получить соответствующие значения.
Введите значение в поле ввода для фильтрации и нажмите кнопку «Фильтрация», чтобы отфильтровать данные.
    
Код:

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd

class DataAnalyzer:
    def __init__(self, master):
        self.master = master
        master.title("Анализатор данных")

        # Фрейм для загрузки файла
        self.file_frame = tk.Frame(master)
        self.file_frame.pack()

        self.load_button = tk.Button(self.file_frame, text="Загрузить файл", command=self.load_data)
        self.load_button.pack(side=tk.LEFT)

        # Фрейм для таблицы
        self.table_frame = tk.Frame(master)
        self.table_frame.pack()

        self.tree = ttk.Treeview(self.table_frame, columns=("Column"), show="headings")
        self.tree.heading("Column", text="Столбец")
        self.tree.pack()

        # Фрейм для кнопок анализа
        self.analysis_frame = tk.Frame(master)
        self.analysis_frame.pack()

        self.mean_button = tk.Button(self.analysis_frame, text="Среднее", command=self.calculate_mean)
        self.mean_button.pack(side=tk.LEFT)

        self.min_button = tk.Button(self.analysis_frame, text="Минимум", command=self.calculate_min)
        self.min_button.pack(side=tk.LEFT)

        self.max_button = tk.Button(self.analysis_frame, text="Максимум", command=self.calculate_max)
        self.max_button.pack(side=tk.LEFT)

        # Фрейм для фильтрации
        self.filter_frame = tk.Frame(master)
        self.filter_frame.pack()

        self.filter_label = tk.Label(self.filter_frame, text="Значение для фильтрации:")
        self.filter_label.pack(side=tk.LEFT)

        self.filter_entry = tk.Entry(self.filter_frame)
        self.filter_entry.pack(side=tk.LEFT)

        self.filter_button = tk.Button(self.filter_frame, text="Фильтрация", command=self.filter_data)
        self.filter_button.pack(side=tk.LEFT)

        self.data = None

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            self.data = pd.read_csv(file_path)
            self.update_table()

    def update_table(self):
        self.tree.delete(*self.tree.get_children())
        for column in self.data.columns:
            self.tree.column(column, width=100, anchor="center")
            self.tree.heading(column, text=column)
        for index, row in self.data.iterrows():
            self.tree.insert("", tk.END, values=list(row))

    def calculate_mean(self):
        column = self.tree.selection()[0]
        if self.data is not None:
            mean_value = self.data[column].mean()
            tk.messagebox.showinfo("Среднее значение", f"Среднее значение для столбца {column}: {mean_value}")

    def calculate_min(self):
        column = self.tree.selection()[0]
        if self.data is not None:
            min_value = self.data[column].min()
            tk.messagebox.showinfo("Минимальное значение", f"Минимальное значение для столбца {column}: {min_value}")

    def calculate_max(self):
        column = self.tree.selection()[0]
        if self.data is not None:
            max_value = self.data[column].max()
            tk.messagebox.showinfo("Максимальное значение", f"Максимальное значение для столбца {column}: {max_value}")

    def filter_data(self):
        filter_value = self.filter_entry.get()
        column = self.tree.selection()[0]
        if self.data is not None and filter_value:
            filtered_data = self.data[self.data[column] == filter_value]
            self.update_table()
            self.data = filtered_data

root = tk.Tk()
app = DataAnalyzer(root)
root.mainloop()
README.md:

Анализатор данных с GUI
Это простое приложение для анализа данных с графическим интерфейсом (GUI), разработанное с использованием Python, библиотек Tkinter и pandas.

Функции:

Загрузка файла CSV через GUI.
Отображение таблицы данных.
Базовые операции анализа:
Подсчет среднего значения.
Поиск минимального и максимального значения.
Фильтрация строк по введенному значению.
Установка:

Убедитесь, что у вас установлены Python и библиотеки Tkinter и pandas.
Скачайте или клонируйте этот репозиторий.
Запустите файл data_analyzer.py.
Использование:

Нажмите кнопку “Загрузить файл”, чтобы выбрать CSV-файл.
Данные будут отображены в таблице.
Выберите столбец для анализа.
Нажмите кнопки «Среднее», «Минимум», «Максимум», чтобы получить соответствующие значения.
Введите значение в поле ввода для фильтрации и нажмите кнопку «Фильтрация», чтобы отфильтровать данные.
Требования:

Python 3.13
Tkinter
pandas
Пример использования:

Загрузите файл CSV с данными, например, data.csv.
Выберите столбец Age для анализа.
Нажмите кнопку “Среднее”, чтобы получить средний возраст.
Введите значение 25 в поле ввода для фильтрации и нажмите кнопку «Фильтрация», чтобы отобразить только строки, в которых возраст равен 25.
Автор: [Алексей Хомичев]
