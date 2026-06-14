import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('pack')
window.geometry('200x200')

button = ttk.Button(window,text='klik acu')
button.grid(row=4,column=15,padx=15,pady=25,sticky='n')


window.mainloop()