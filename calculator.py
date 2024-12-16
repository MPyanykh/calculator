import tkinter as tk

def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return num1, num2

def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)

def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)

def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)

def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)

def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)

window = tk.Tk()
window.title("Калькулятор") # название
window.geometry('400x400') # размер
window.resizable(False, False) # запрет на изменение размера
button_add = tk.Button(window, text = '+', width = '4', height = '2', command = add) # создание элемента - кнопка, принадлежашего ранее созданному окну
button_add.place(x = 100, y = 200) # размещение элемента по координатам  - отсчет как в 4м квадранте (от левого верхнего угла)
button_sub = tk.Button(window, text = '-', width = '4', height = '2', command = sub)
button_sub.place(x = 150, y = 200)
button_mul = tk.Button(window, text = '*', width = '4', height = '2', command = mul)
button_mul.place(x = 200, y = 200)
button_div = tk.Button(window, text = '/', width = '4', height = '2', command = div)
button_div.place(x = 250, y = 200)
number1_entry = tk.Entry(window, width = '25') # создание элемента - текстовое поле (для ввода)
number1_entry.place(x = 100, y = 100)
number2_entry = tk.Entry(window, width = '25') # аналогично
number2_entry.place(x = 100, y = 150)
answer_entry = tk.Entry(window, width = '25') # аналогично, но для вывода ответа
answer_entry.place(x = 100, y = 275)
number1 = tk.Label(window, text = 'Введите первое число:') # создание элемента - надпись
number1.place(x = 100, y = 75)
number2 = tk.Label(window, text = 'Введите второе число:') # создание элемента - надпись
number2.place(x = 100, y = 125)
answer = tk.Label(window, text = 'Ответ:') # создание элемента - надпись
answer.place(x = 100, y = 250)
window.mainloop()