#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Entry, Button, Label


def calculate(operation: str) -> None:
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        label_result["text"] = result
    except ValueError:
        label_result["text"] = "Ошибка"


if __name__ == "__main__":
    root = Tk()

    entry1 = Entry(root, width=12)
    entry1.pack()

    entry2 = Entry(root, width=12)
    entry2.pack()

    button_add = Button(root, text="+", command=lambda: calculate("+"), width=10)
    button_add.pack()

    button_subtract = Button(root, text="-", command=lambda: calculate("-"), width=10)
    button_subtract.pack()

    button_multiply = Button(root, text="*", command=lambda: calculate("*"), width=10)
    button_multiply.pack()

    button_divide = Button(root, text="/", command=lambda: calculate("/"), width=10)
    button_divide.pack()

    label_result = Label(root)
    label_result.pack()

    root.mainloop()
