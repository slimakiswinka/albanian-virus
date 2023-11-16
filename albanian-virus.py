import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()  # Hide the main window

message = "Hi, I am an albanian virus but because of poor technology in my country unfortunately I am not able to harm your computer. Please be so kind to delete one of your important files yourself and then forward me other users. Many thanks for your cooperation! Best regards, Albanian virus"
title = "Virus Alert"

messagebox.showinfo(title, message)
