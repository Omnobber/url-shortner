import pyshorteners
from tkinter import *

win = Tk()
win.geometry("400x270")
win.configure(bg="pink")

# Button Function
def short():
    url = entry1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    entry2.delete(0, END)  # Clear previous content
    entry2.insert(END, s)

# Label for entering user url
Label(win, text="Enter Your Url Link", font="impack 17 bold", bg="black", fg="white", width="14").pack(fill="x")

# Entry box
entry1 = Entry(win, font="10", bd=3, width=40)
entry1.pack(pady=10)

# Button
Button(win, text="Click Me", font="impack 12 bold", bg="blue", fg="white", command=short).pack()

# Entry
entry2 = Entry(win, font="impack 16 bold", bg="pink", width=24, bd=0)
entry2.pack(pady=10)

mainloop()
