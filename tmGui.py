import tkinter
from tkinter import *
from tkinter import messagebox
import tmDB


def add():
    if(len(addtask.get()) == 0):
        messagebox.showerror(
            "ERROR", "No data Available\nPlease Enter Some Task")
    else:
        tmDB.insertdata(addtask.get())
        addtask.delete(0, END)
        populate()


def populate():
    listbox.delete(0, END)
    for rows in tmDB.show():
        listbox.insert(END, rows[1])


def deletetask(event):
    tmDB.deletebytask(listbox.get(ANCHOR))
    populate()


main = tkinter.Tk()
main.title("TODO")
main.geometry("500x600")
main.resizable(True, True)
main.configure(
    background="#1d1d1d",
)

tkinter.Label(
    main,
    text="Task Manager",
    background="#1d1d1d",
    foreground="#eeeeee",
    font=("Verdana 20")
).pack(pady=10)

addframe = tkinter.Frame(
    main,
    bg="#1d1d1d",
)
addframe.pack()
addtask = tkinter.Entry(
    addframe,
    font=("Verdana"),
    background="#eeeeee",
)
addtask.pack(ipadx=20, ipady=5, side="left")

addbtn = tkinter.Button(
    addframe,
    text="ADD TASK",
    command=add,
    background="#000000",
    foreground="#eeeeee",
    relief="flat",
    font=("Verdana"),
    highlightcolor="#000000",
    activebackground="#1d1d1d",
    border=0,
    activeforeground="#eeeeee",
)
addbtn.pack(padx=20, ipadx=20, ipady=5)

tkinter.Label(
    main,
    text="Your Tasks",
    background="#1d1d1d",
    foreground="#eeeeee",
    font=("Calibri", 18),
).pack(pady=10)

taskframe = tkinter.Frame(
    main,
    bg="#1d1d1d",
)
taskframe.pack(fill=BOTH, expand=300)
scrollbar = Scrollbar(taskframe)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(
    taskframe,
    font=("Verdana 18 bold"),
    bg="#1d1d1d",
    fg="#eeeeee",
    selectbackground="#eeeeee",
    selectforeground="#1d1d1d",
)
listbox.pack(fill=BOTH, expand=300)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

listbox.bind("<Double-Button-1>", deletetask)
listbox.bind("<Delete>", deletetask)

populate()

tkinter.Label(
    main,
    text="TIP : Double Click On A Task to Delete",
    background="#1d1d1d",
    foreground="#FFEB3B",
    font=("Calibri 18"),
).pack(side=BOTTOM, pady=10)

main.mainloop()
