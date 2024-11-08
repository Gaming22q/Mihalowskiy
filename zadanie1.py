Код:

import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import filedialog

class DataAnalyzer:
    def __init__(self, master):
        self.master = master
        master.title("Анализатор данных")

        # Фрейм для загрузки файла
        self.file_frame = tk.Frame(master)
        self.file_frame.pack(pady=10)

        # Кнопка загрузки файла
        self.load_button = tk.Button(self.file_frame, text="Загрузить файл", command=self.load_data)
        self.load_button.pack(side=tk.LEFT)

        # Фрейм для таблицы данных
        self.data_frame = tk.Frame(master)
        self.data_frame.pack()

        # Создание Treeview
        self.data_tree = ttk.Treeview(self.data_frame, columns=("Column 1", "Column 2", "Column 3"), show="headings")
        self.data_tree.heading("Column 1", text="Column 1")
        self.data_tree.heading("Column 2", text="Column 2")
        self.data_tree.heading("Column 3", text="Column 3")
        self.data_tree.pack()

        # Фрейм для элементов управления
        self.control_frame = tk.Frame(master)
        self.control_frame.pack(pady=10)

        # Поле ввода для фильтрации
        self.filter_entry = tk.Entry(self.control_frame)
        self.filter_entry.pack(side=tk.LEFT)

        # Поле выбора столбца
        self.column_combobox = ttk.Combobox(self.control_frame, values=[])
        self.column_combobox.pack(side=tk.LEFT)

        # Кнопки анализа
        self.mean_button = tk.Button(self.control_frame, text="Среднее", command=self.calculate_mean)
        self.mean_button.pack(side=tk.LEFT)
        self.min_button = tk.Button(self.control_frame, text="Минимум", command=self.calculate_min)
        self.min_button.pack(side=tk.LEFT)
        self.max_button = tk.Button(self.control_frame, text="Максимум", command=self.calculate_max)
        self.max_button.pack(side=tk.LEFT)

        # Кнопка фильтрации
        self.filter_button = tk.Button(self.control_frame, text="Фильтрация", command=self.filter_data)
        self.filter_button.pack(side=tk.LEFT)

        # Кнопка сброса
        self.reset_button = tk.Button(self.control_frame, text="Сброс", command=self.reset_data)
        self.reset_button.pack(side=tk.LEFT)

        # Инициализация данных
        self.data = None
        self.filtered_data = None  # Добавлено для хранения отфильтрованных данных

    def load_data(self):
        # Открытие диалогового окна для выбора файла
        file_path = filedialog.askopenfilename(initialdir="/", title="Выберите файл", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
        if file_path:
            # Загрузка данных из CSV файла
            self.data = pd.read_csv(file_path)
            self.filtered_data = self.data.copy()  # Инициализация filtered_data
            self.display_data()

    def display_data(self, data=None):
        # Очистка таблицы
        for i in self.data_tree.get_children():
            self.data_tree.delete(i)

        # Добавление данных в таблицу
        display_data = data if data is not None else self.filtered_data  # Используем filtered_data по умолчанию
        for index, row in display_data.iterrows():
            self.data_tree.insert("", tk.END, values=list(row))

        # Обновление списка столбцов
        self.column_combobox['values'] = list(self.data.columns)

    def calculate_mean(self):
        if self.data is not None:
            column = self.column_combobox.get()
            if column:
                mean_value = self.filtered_data[column].mean()  # Используем filtered_data
                tk.messagebox.showinfo("Среднее значение", f"Среднее значение для столбца {column}: {mean_value}")

    def calculate_min(self):
        if self.data is not None:
            column = self.column_combobox.get()
            if column:
                min_value = self.filtered_data[column].min()  # Используем filtered_data
                tk.messagebox.showinfo("Минимум", f"Минимальное значение для столбца {column}: {min_value}")

    def calculate_max(self):
        if self.data is not None:
            column = self.column_combobox.get()
            if column:
                max_value = self.filtered_data[column].max()  # Используем filtered_data
                tk.messagebox.showinfo("Максимум", f"Максимальное значение для столбца {column}: {max_value}")

    def filter_data(self):
        if self.data is not None:
            filter_value = self.filter_entry.get()
            column = self.column_combobox.get()
            if filter_value and column:
                self.filtered_data = self.data[self.data[column].str.contains(filter_value, case=False)]  # Поиск по строке
                self.display_data(self.filtered_data)

    def reset_data(self):
        if self.data is not None:
            self.filtered_data = self.data.copy()  # Сброс фильтрации
            self.display_data()

root = tk.Tk()
app = DataAnalyzer(root)
root.mainloop()
