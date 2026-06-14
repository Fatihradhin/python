import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('pack')
window.geometry('200x200')

label = ttk.Label(window,text="ini tkss")
label.pack(side='top',fill='x',expand=True)


window.mainloop()