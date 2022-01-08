from tkinter import messagebox
from tkinter import *
# from tkinter import ttk

p_list = Tk()
p_list.title("Product List")
p_list.geometry('800x320')
product_id = StringVar()
product_name = StringVar()
selling_price = StringVar()
quantity = StringVar()

# Functions
# clear function


def clear():
    i_d.delete(0, END)
    p_n.delete(0, END)
    s_n.delete(0, END)
    p_q.delete(0, END)


# show function


def show():

    file = open("product.txt", 'r')
    for each in reversed(file.readlines()):
        view_field.insert(0.0, each)
    file.close()

# insert function


def insert():
    id_num = product_id.get()
    n_product = product_name.get()
    s_price = selling_price.get()
    q_pr = quantity.get()
    file = open("product.txt")
    reading = file.read()
    if id_num in reading:
        messagebox.showerror("Wrong", "Product Already exist")
    elif id_num.isdigit() and n_product.isalpha() and s_price.isdigit() and q_pr.isdigit():
        file = open("product.txt", 'r')
        count = len(file.readlines())
        file = open("product.txt", 'a')
        file.write(str(count+1)+"\t\t" + id_num + "\t\t" + n_product +
                   "\t\t\t" + s_price + "\t\t" + q_pr + "\t\t\t" + '\n')
        messagebox.showinfo("Added", "Product added")
    else:
        messagebox.showerror("Wrong", "Invalid Input")
    file.close()


frame1 = LabelFrame(p_list)
frame2 = LabelFrame(p_list)
frame3 = LabelFrame(p_list)
frame4 = LabelFrame(p_list)
frame5 = LabelFrame(p_list)
frame6 = LabelFrame(p_list)
frame7 = LabelFrame(p_list)

frame1.place(x=3, y=10, width=150, height=320)
frame2.place(x=150, y=10, width=650, height=320)
# 650/5 = 130
frame3.place(x=150, y=22,  width=131, height=20)
frame4.place(x=280, y=22,  width=131, height=20)
frame5.place(x=410, y=22,  width=131, height=20)
frame6.place(x=540, y=22,  width=131, height=20)
frame7.place(x=670, y=22,  width=130, height=20)


item_no = Label(frame3, text="Item no")
item_no.pack()

pro_id = Label(frame4, text="Product Id")
pro_id.pack()

name = Label(frame5, text="Name")
name.pack()

sell_price = Label(frame6, text="Selling Price")
sell_price.pack()

q_pro = Label(frame7, text="Quantity")
q_pro.pack()

i_m = Label(p_list, text="Inventory Management")
i_m.place(x=5, y=0)

info = Label(p_list, text="Product List")
info.place(x=170, y=0)

p_id = Label(p_list, text="Product Id :")
p_id.place(x=10, y=30)
i_d = Entry(p_list, textvar=product_id)
i_d.place(x=10, y=60)


p_name = Label(p_list, text="Product Name :")
p_name.place(x=10, y=90)
p_n = Entry(p_list, textvar=product_name)
p_n.place(x=10, y=120)


p_price = Label(p_list, text="Selling Price :")
p_price.place(x=10, y=150)
s_n = Entry(p_list, textvar=selling_price)
s_n.place(x=10, y=180)


p_quantity = Label(p_list, text="Quantity :")
p_quantity.place(x=10, y=210)
p_q = Entry(p_list, textvar=quantity)
p_q.place(x=10, y=240)

view_field = Text(p_list, height=298, width=650)
view_field.place(x=150, y=43)

insert_button = Button(p_list, text='Insert', bg="lightblue", command=insert)
insert_button.place(x=10, y=275)

show_button = Button(p_list, text='Show', bg="lightblue", command=show)
show_button.place(x=55, y=275)

clear_button = Button(p_list, text='Clear', bg="lightblue", command=clear)
clear_button.place(x=100, y=275)

p_list.mainloop()