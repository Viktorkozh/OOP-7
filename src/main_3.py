#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Entry, Button, Label
from typing import Callable


def insert_color_code(color_code: str, color_name: str) -> None:
    entry.delete(0, "end")
    entry.insert(0, color_code)
    label_color["text"] = color_name


def create_color_button(color_code: str, color_name: str) -> Callable[[], None]:
    def button_command() -> None:
        insert_color_code(color_code, color_name)

    return button_command


if __name__ == "__main__":
    root = Tk()

    label_color = Label(root, text="", width=12)
    label_color.pack()

    entry = Entry(root, width=13, bd=0, highlightthickness=0)
    entry.pack()

    colors = [
        ("Красный", "#ff0000"),
        ("Оранжевый", "#ff7d00"),
        ("Желтый", "#ffff00"),
        ("Зеленый", "#00ff00"),
        ("Голубой", "#007dff"),
        ("Синий", "#0000ff"),
        ("Фиолетовый", "#7d00ff"),
    ]

    for color_name, color_code in colors:
        button = Button(
            root,
            bg=color_code,
            command=create_color_button(color_code, color_name),
            width=2,
        )
        button.pack(side="left")

    root.mainloop()
