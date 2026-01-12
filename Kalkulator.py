import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
    ]

right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%"]

row_count = len(button_values) #5 row
column_count = len(button_values[0]) #4 column

color_black = "#1C1C1C"
color_white = "#FFFFFF"

window = tkinter.Tk()
window.title("Kalkulator")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", bg=color_black, font=("Arial 50"), background=color_black, 
                      foreground=color_white, anchor="e")

label.grid(row=0, column=0, columnspan=column_count, sticky="nsew")

for row in range(row_count):
    for colomn in range(column_count):
        value = button_values[row][colomn]
        button = tkinter.Button(frame, text=value, font =("Arial 30"),
                                width = column_count-1, heigh=1,
                                command=lambda value=value : button_clicked(value))
        button.grid(row=row+1, column=colomn)
        

frame.pack()

def button_clicked(value) :
    pass
    
window.mainloop()


