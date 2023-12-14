import tkinter
import turtle

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)

def calculate():
    miles = int(input.get())
    conversion = (miles * 5) / 8
    label4.config(text=f"{conversion}")


label1 = tkinter.Label(text="is equal to")
label1.grid(column=0, row=1, padx = 20)

label2 = tkinter.Label(text="Miles")
label2.grid(column=2, row=0)

label3 = tkinter.Label(text="Km")
label3.grid(column=2, row=1)

label4 = tkinter.Label(text="0")
label4.grid(column=1, row=1)


input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

button = tkinter.Button(text="Calculate", command = calculate)
button.grid(column=1, row=3)


window.mainloop()
