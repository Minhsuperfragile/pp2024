from output import *
import tkinter as tk
from tkinter import ttk

#region window UI
window = tk.Tk()
window.title('Cursed UI')
window.geometry('300x200')
window.resizable(False, False)

#ttk style
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton', background = '#FFBE98', foreground = 'black', width = 20, borderwidth=1, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active','#FFD1DC')])

#ttk label
label = ttk.Label(master= window,text= 'student management terminal controller')
label.pack()

#ttk button
refreshButton = ttk.Button(master= window, text= 'refresh',command= clear)
refreshButton.pack(ipadx=7,ipady=7)

sortButton = ttk.Button(master= window, text= 'sort',command= sortButtonCmd)
sortButton.pack(ipadx=7,ipady=7)

shuffleButton = ttk.Button(master= window, text= 'shuffle',command= shuffleButtonCmd)
shuffleButton.pack(ipadx=7,ipady=7)

printButton = ttk.Button(master= window, text= 'list',command= listAllOutCmd)
printButton.pack(ipadx=7,ipady=7)

window.mainloop()
#endregion