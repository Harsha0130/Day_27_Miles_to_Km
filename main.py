from tkinter import *

window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)
# padding
window.config(padx=200, pady=200)

# Label
my_label = Label(text="Hello, I am new here!", font=("Arial", 26, "bold"))
my_label.grid(column=0, row=0)

# Changing thr label property(here text)
my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


# Button
button = Button(text="Click here", command=button_clicked)
button.grid(column=2, row=1)

button = Button(text="Click here", command=button_clicked)
button.grid(column=3, row=0)

# Entry
input = Entry(width=10)
input.grid(column=4, row=2)

window.mainloop()
