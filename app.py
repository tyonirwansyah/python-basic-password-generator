import tkinter as tk
from tkinter.constants import LEFT
from utils.show_password import showPassword
from utils.copy_password import copyPassword

# Root Window
window = tk.Tk()

# Window Settings
window.title("Password Generator")
window.iconphoto(False, tk.PhotoImage(file="./assets/icon.ico"))
window.geometry("600x650")
window.configure(background="gray18")

# Create Frame

title = tk.Label(
    window,
    height=4,
    width=600,
    bg="gray30",
    padx=8,
    pady=8,
    text="Generate Password",
    font="Poppins",
    foreground="white",
)
title.pack()

lengthValue = tk.IntVar()
isSymbol = tk.BooleanVar()
isNumbers = tk.BooleanVar()

lengthLabel = tk.Label(window, text="Password Length")
lengthLabel.pack(pady=(60, 0), anchor="center")

passwordLength = tk.Spinbox(window, textvariable=lengthValue, from_=8, to=100)
passwordLength.pack(pady=(30, 0), anchor="center")

includeSymbols = tk.Checkbutton(window, text="Include Symbols", variable=isSymbol, onvalue=1, offvalue=0)
includeSymbols.pack(pady=30, anchor="center")

includeNumbers = tk.Checkbutton(window, text="Include Numbers", variable=isNumbers, onvalue=1, offvalue=0)
includeNumbers.pack()


password = tk.Button(
    window,
    text="Make Password",
    command=lambda: showPassword(lengthValue.get(), isNumbers.get(), isSymbol.get(), passwordResult, passCopy),
    width=14,
    cursor="circle",
)

password.pack(pady=30, anchor="center")

passwordResult = tk.Label(window)

copiedMessage = tk.Label(window, text="Copied!")

passCopy = tk.Button(
    window, text="Copy to Clipboard", command=lambda: copyPassword(passwordResult.cget("text"), copiedMessage)
)


# Creates Window
window.mainloop()
