#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Radiobutton, Label, Frame, StringVar


def update_label() -> None:
    label["text"] = f"{var.get()}"


root = Tk()
root.geometry("200x120")

var = StringVar()
contactList = [
    ("Вася", "+3 645456456"),
    ("Петя", "+6 5141414"),
    ("Маша", "+5 645456123"),
]

frame = Frame(root)
for name, phoneNumber in contactList:
    Radiobutton(
        frame,
        text=name,
        variable=var,
        value=phoneNumber,
        command=update_label,
        indicatoron=False,
        width=10,
        height=2,
    ).pack(anchor="w")

frame.pack(side="left")

label = Label(root, text="Выберите контакт")
label.pack(side="left")

root.mainloop()
