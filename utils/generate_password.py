import random

# All Characters for Password
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!$%^&*()_+|~-=`{}[]:;'<>?,./"

# Creates Password
def createPassword(length=8, withNumbers=True, withSymbols=True):
    chars = letters
    if withNumbers == True:
        chars += numbers
    if withSymbols == True:
        chars += symbols
    return generatePassword(length, chars)


# Generates Password
def generatePassword(length, chars):
    password = ""
    for i in range(length):
        password += chars[random.randint(0, len(chars) - 1)]
    return password
