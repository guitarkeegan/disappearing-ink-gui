from tkinter import *
from tkinter import ttk
from tkinter import font


# functions


def delete_placeholder(event):
    written_text = text_field.get("1.0", "end")
    if written_text[0:4] == "When":
        text_field.replace("1.0", "end", "")


def delete_message():
    global timer
    text_field.replace("1.0", "end", "")
    timer = 0


def timer_countdown(event):
    global timer
    if timer != 0:
        text_field.after_cancel(timer)
        timer = text_field.after(5000, func=delete_message)
    else:
        timer = text_field.after(5000, func=delete_message)


timer = 0
FONT = ("honey script", 40, "normal")
PLACEHOLDER = "When you stop typing, the text will disappear."

# UI setup
root = Tk()
root.title("Disapearing Ink")

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

text_field = Text(mainframe, width=40, height=10, font=FONT)
text_field.insert("1.0", PLACEHOLDER)
y_axis = ttk.Scrollbar(root, orient="vertical", command=text_field.yview)
text_field['yscrollcommand'] = y_axis.set
y_axis.grid(column=2, row=0, sticky="ns")
text_field.grid(column=1, row=1, columnspan=2)

# delete placeholder text on click

text_field.bind("<Button-1>", delete_placeholder)

# delete message after 5 seconds

text_field.bind_all("<Key>", timer_countdown)

root.mainloop()
