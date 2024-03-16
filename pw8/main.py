from output import cmdFunction as cmd
import tkinter as tk
from tkinter import ttk

#region window UI
window = tk.Tk()
window.title('Cursed UI')
window.geometry('300x300')
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
refreshButton = ttk.Button(master= window, text= 'refresh',command= cmd.clear)
refreshButton.pack(ipadx=7,ipady=7)

sortButton = ttk.Button(master= window, text= 'sort',command= cmd.sortButtonCmd)
sortButton.pack(ipadx=7,ipady=7)

shuffleButton = ttk.Button(master= window, text= 'shuffle',command= cmd.shuffleButtonCmd)
shuffleButton.pack(ipadx=7,ipady=7)

printButton = ttk.Button(master= window, text= 'list',command= cmd.listAllOutCmd)
printButton.pack(ipadx=7,ipady=7)

writeButton = ttk.Button(master= window, text= 'write',command= cmd.writeToTextFileCmd)
writeButton.pack(ipadx=7,ipady=7)

pickleButton = ttk.Button(master= window, text= 'compress', command= cmd.pickleWriteBackgroundCmd)
pickleButton.pack(ipadx=7,ipady=7)

window.mainloop()
#endregion