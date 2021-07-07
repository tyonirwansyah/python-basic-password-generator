from tkinter import Button, Label
from utils.generate_password import createPassword


def showPassword(length, withNumbers, withSymbols, passwordResult: Label, clipboard: Button):
    result = createPassword(length, withNumbers, withSymbols)
    passwordResult.pack()
    clipboard.pack(pady=30)
    return passwordResult.config(text=result)
