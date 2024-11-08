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

        self.tree = ttk.Treeview(self.table_frame, columns=("Column1", "Column2", "Column3"), show="headings")
        self.tree.heading("Column1", text="Столбец 1")
        self.tree.heading("Column2", text="Столбец 2")
        self.tree.heading("Column3", text="Столбец 3")
        self.tree.pack()

        # Фрейм для галочек
        self.checkbox_frame = tk.Frame(master)
        self.checkbox_frame.pack()

        self.checkboxes = []
        for i in range(3):
            var = tk.IntVar()
            checkbox = tk.Checkbutton(self.checkbox_frame, text=f"Столбец {i+1}", variable=var)
            checkbox.pack(side=tk.LEFT)
            self.checkboxes.append(var)

        # Фрейм для вывода значений
        self.output_frame = tk.Frame(master)
        self.output_frame.pack()

        self.output_label = tk.Label(self.output_frame, text="Результат:")
        self.output_label.pack(side=tk.LEFT)

        self.output_value = tk.Label(self.output_frame, text="")
        self.output_value.pack(side=tk.LEFT)

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
        # Отображение только первых трех столбцов
        for i in range(min(3, len(self.data.columns))):
            column_name = self.data.columns[i]
            self.tree.column(f"Column{i+1}", width=100, anchor="center")
            self.tree.heading(f"Column{i+1}", text=column_name)
        for index, row in self.data.iterrows():
            self.tree.insert("", tk.END, values=list(row[:3]))  # Отобразить только первые три значения

    def get_selected_column(self):
        for i, checkbox in enumerate(self.checkboxes):
            if checkbox.get() == 1:
                return i  # Возвращает индекс выбранного столбца (0, 1, 2)
        return None  # Ни один столбец не выбран

    def calculate_mean(self):
        column_index = self.get_selected_column()
        if self.data is not None and column_index is not None:
            mean_value = self.data.iloc[:, column_index].mean()
            self.output_value.config(text=f"Среднее значение: {mean_value}")

    def calculate_min(self):
        column_index = self.get_selected_column()
        if self.data is not None and column_index is not None:
            min_value = self.data.iloc[:, column_index].min()
            self.output_value.config(text=f"Минимальное значение: {min_value}")

    def calculate_max(self):
        column_index = self.get_selected_column()
        if self.data is not None and column_index is not None:
            max_value = self.data.iloc[:, column_index].max()
            self.output_value.config(text=f"Максимальное значение: {max_value}")

    def filter_data(self):
        filter_value = self.filter_entry.get()
        column_index = self.get_selected_column()
        if self.data is not None and filter_value and column_index is not None:
            filtered_data = self.data[self.data.iloc[:, column_index] == filter_value]
            self.update_table()
            self.data = filtered_data
            self.output_value.config(text=f"Отфильтровано: {len(filtered_data)} строк")

root = tk.Tk()
app = DataAnalyzer(root)
root.mainloop()

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
