from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=50, pady=50, background="grey")


def mi_to_km():
    miles = float(spinbox.get())
    if miles < 0:
        km_answer_label.config(text="error")
    else:
        km = miles * 1.609
        km_answer_label.config(text=f"{km}")


label = Label(text="Miles to Kilometers", font=("Arial", 10, "bold"), background="grey")
label.grid(column=2, row=0, )
label.config(padx=10, pady=10)

spinbox = Spinbox(from_=0, to=100000, width=5, background="grey")
spinbox.grid(column=1, row=1)

miles_label = Label(text="Miles", background="grey")
miles_label.grid(column=1, row=2)
miles_label.config(padx=10, pady=10)

equal = Label(text="=", background="grey")
equal.grid(column=2, row=1)
equal.config(padx=10, pady=10)

km_answer_label = Label(text="", background="grey")
km_answer_label.grid(column=3, row=1)
km_answer_label.config(padx=10, pady=10)

km_label = Label(text="Km", background="grey")
km_label.grid(column=3, row=2)
km_label.config(padx=10, pady=10)

calculate = Button(text="Convert", width=5, background="grey", command=mi_to_km)
calculate.grid(column=2, row=3)
calculate.config(padx=10, pady=10)

window.mainloop()
