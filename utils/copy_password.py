from tkinter import Label
from tkinter import Label
import pyperclip as clipper
import time


def copyPassword(text, copiedMessage: Label):
    clipper.copy(text)
    copiedMessage.pack()
    copiedMessage.after(800, lambda: copiedMessage.pack_forget())
