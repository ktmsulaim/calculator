from tkinter import *
from tkinter.font import Font

# Instantiate the module
root = Tk()
# Basic layout configuration
root.title("Calculator | Crossroads challenge")
root.config(bg="#222")
root.geometry("250x400+300+300")
root.resizable(0, 0)

# Basic font
label_font = Font(family="Verdana", size=16)
button_font = Font(family="Verdana", size=10)

# Label row
label = Label(root, text="Label", anchor=SE, font=label_font, padx=10, pady=10, relief=FLAT)
label.pack(expand=True, fill="both")
# Button rows
# 1st row - contains (7 | 8 | 9 | +)
button_row_1 = Frame(root, bg="#222")
button_row_1.pack(expand=True, fill="both")

btn1 = Button(button_row_1, text="7", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
              font=button_font, bd=0, width=2)
btn1.pack(side=LEFT, expand=True, fill="both")

btn2 = Button(button_row_1, text="8", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
              font=button_font, bd=0, width=2)
btn2.pack(side=LEFT, expand=True, fill="both")

btn3 = Button(button_row_1, text="9", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
              font=button_font, bd=0, width=2)
btn3.pack(side=LEFT, expand=True, fill="both")

btn4 = Button(button_row_1, text="+", bg="#5f4bb6", fg="#f5f5f5", activebackground="#666", relief=FLAT,
              font=button_font, bd=0, width=3)
btn4.pack(side=LEFT, expand=True, fill="both")

# 2nd row - contains (4 | 5 | 6 | -)
button_row_2 = Frame(root, bg="#222")
button_row_2.pack(expand=True, fill="both")

btn5 = Button(button_row_2, text="4", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
              font=button_font, bd=0, width=2)
btn5.pack(side=LEFT, expand=True, fill="both")

btn6 = Button(button_row_2, text="5", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
              font=button_font, bd=0, width=2)
btn6.pack(side=LEFT, expand=True, fill="both")

btn7 = Button(button_row_2, text="6", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
              font=button_font, bd=0, width=2)
btn7.pack(side=LEFT, expand=True, fill="both")

btn8 = Button(button_row_2, text="-", bg="#5f4bb6", fg="#f5f5f5", activebackground="#666", relief=FLAT,
              font=button_font, bd=0, width=3)
btn8.pack(side=LEFT, expand=True, fill="both")


# 3rd row - contains (1 | 2 | 3 | x)
button_row_3 = Frame(root, bg="#222")
button_row_3.pack(expand=True, fill="both")

btn9 = Button(button_row_3, text="1", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
              font=button_font, bd=0, width=2)
btn9.pack(side=LEFT, expand=True, fill="both")

btn10 = Button(button_row_3, text="2", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
               font=button_font, bd=0, width=2)
btn10.pack(side=LEFT, expand=True, fill="both")

btn11 = Button(button_row_3, text="3", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
               font=button_font, bd=0, width=2)
btn11.pack(side=LEFT, expand=True, fill="both")

btn12 = Button(button_row_3, text="x", bg="#5f4bb6", fg="#f5f5f5", activebackground="#666", relief=FLAT,
               font=button_font, bd=0, width=3)
btn12.pack(side=LEFT, expand=True, fill="both")


# 4th row - contains (C | 0 | / | =)
button_row_4 = Frame(root, bg="#222")
button_row_4.pack(expand=True, fill="both")

btn13 = Button(button_row_4, text="C", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
               font=button_font, bd=0, width=2)
btn13.pack(side=LEFT, expand=True, fill="both")

btn14 = Button(button_row_4, text="0", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
               font=button_font, bd=0, width=2)
btn14.pack(side=LEFT, expand=True, fill="both")

btn15 = Button(button_row_4, text="/", bg="#222", fg="#f5f5f5", activebackground="#666", relief=FLAT,
               font=button_font, bd=0, width=2)
btn15.pack(side=LEFT, expand=True, fill="both")

btn16 = Button(button_row_4, text="=", bg="#ffc207", fg="#222", activebackground="#666", relief=FLAT,
               font=button_font, bd=0, width=3)
btn16.pack(side=LEFT, expand=True, fill="both")

# Run application
root.mainloop()
