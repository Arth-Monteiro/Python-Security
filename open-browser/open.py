from tkinter import *
import webbrowser

root = Tk()
root.title = "Abrir Browser"
root.geometry("300x200")

def google():
    webbrowser.open("google.com")

myGoogle = Button(root, text="Abrir Google", command=google).pack(pady=20)

root.mainloop()