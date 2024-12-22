#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from tkinter import Tk, Text, Button, Entry, Frame


def get_script_directory() -> str:
    return os.path.dirname(os.path.abspath(__file__))


def open_file() -> None:
    file_path = entry_filename.get()
    if file_path:
        try:
            if os.path.isabs(file_path) or "/" in file_path or "\\" in file_path:
                full_path = file_path
            else:
                full_path = os.path.join(get_script_directory(), file_path)

            with open(full_path, "r", encoding="utf-8") as file:
                text.delete(1.0, "end")
                text.insert(1.0, file.read())
        except FileNotFoundError:
            text.delete(1.0, "end")
            text.insert(1.0, "Файл не найден")
        except Exception as e:
            text.delete(1.0, "end")
            text.insert(1.0, f"Ошибка: {str(e)}")


def save_file() -> None:
    file_path = entry_filename.get()
    if file_path:
        try:
            if os.path.isabs(file_path) or "/" in file_path or "\\" in file_path:
                full_path = file_path
            else:
                full_path = os.path.join(get_script_directory(), file_path)

            with open(full_path, "w", encoding="utf-8") as file:
                file.write(text.get(1.0, "end-1c"))
        except Exception as e:
            text.delete(1.0, "end")
            text.insert(1.0, f"Ошибка сохранения: {str(e)}")


root = Tk()

top_frame = Frame(root)
top_frame.pack(side="top", fill="x")

entry_filename = Entry(top_frame, width=40)
entry_filename.pack(side="left")

button_open = Button(top_frame, text="Открыть", command=open_file)
button_open.pack(side="left")

button_save = Button(top_frame, text="Сохранить", command=save_file)
button_save.pack(side="left")

text = Text(root, width=45, height=20)
text.pack(side="bottom", padx=10, pady=10)

root.mainloop()
