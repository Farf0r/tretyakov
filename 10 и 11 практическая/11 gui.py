from tkinter import *
from tkinter.ttk import Combobox
from tkinter import Radiobutton
from tkinter import ttk
from tkinter import messagebox

window = Tk()
window.title('Третьяков Денис Витальевич')
window.geometry("500x250")
tab = ttk.Notebook(window)
tab1 = ttk.Frame(tab)
tab2 = ttk.Frame(tab)
tab3 = ttk.Frame(tab)
tab.add(tab1, text='Калькулятор')
tab.add(tab2, text='Чекбоксы')
tab.add(tab3, text='Текст')
tab.pack(expand=1, fill='both')


# Калькулятор
def calculate():
    n1 = float(txt.get())
    n2 = float(txt2.get())
    operation = combobox.get()

    if operation == "+":
        result = n1 + n2
    elif operation == "-":
        result = n1 - n2
    elif operation == "*":
        result = n1 * n2
    elif operation == "/":
        if n2 != 0:
            result = n1 / n2
    else:
        result = "Неверная операция"

    lbl2.config(text=f"Ответ: {result}")


frame = Frame(window)
frame.pack(fill=Y)
frame.pack(expand=True)
lbl = Label(frame, text="Калькулятор", font=('Arial Bond', 12))
lbl.grid(row=1, column=2)
txt = Entry(frame, width=15)
txt.grid(row=2, column=1)
txt2 = Entry(frame, width=15)
txt2.grid(row=2, column=3)
methods = ['+', '-', '*', '/']
combobox = Combobox(frame, values=methods, width=5, state='readonly')
combobox.grid(row=2, column=2)
combobox.set('+')
btn = Button(frame, text="Вычислить", command=calculate)
btn.grid(row=3, column=2)
lbl2 = Label(frame, text='Ответ:')
lbl2.grid(row=4, column=2)


# Чекбоксы
def clicked():
    operation = selected.get()  # ?

    if operation == 'Первый':
        messagebox.showinfo('Выбор', 'Вы выбрали первый вариант')
    elif operation == 'Второй':
        messagebox.showinfo('Выбор', 'Вы выбрали второй вариант')
    elif operation == 'Третий':
        messagebox.showinfo('Выбор', 'Вы выбрали третий вариант')


selected = IntVar()
rad1 = Radiobutton(tab2, text='Первый', value=1, variable=selected)
rad2 = Radiobutton(tab2, text='Второй', value=2, variable=selected)
rad3 = Radiobutton(tab2, text='Третий', value=3, variable=selected)
rad1.grid(row=1, column=1)
rad2.grid(row=1, column=2)
rad3.grid(row=1, column=3)
btn2 = Button(tab2, text='Выбрать', command=clicked)
btn2.grid(row=1, column=4)

# Текст

txt = Text()
txt.pack()
window.mainloop()