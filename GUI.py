from tkinter import *
from tkinter import ttk
from tkinter.ttk import Combobox
import Database
from datetime import date
import random
import sqlite3
from tkinter import messagebox
import csv


def login_page():
    global login_screen
    login_screen = Tk()
    login_screen.geometry("500x500")
    login_screen.title("Login Page")
    login_screen.configure(background="#FFEAAC")
    login_screen.resizable(False, False)
    heading = Label(text = "RMA Inventory System", fg = "white", bg = "#E8A66D",width="500", height ="1",font='times 35 bold').pack()
    headingline = Frame(login_screen, width=500, height=5, bd=3,bg="#FF9380")
    headingline.pack(side=TOP)

    #Frame
    topframe = Frame(login_screen, width=400, height=400, bd=3, relief='raise')
    topframe.place(x = 50, y = 94)

    #Title Name Login
    Label(text= "Login", font='times 25 bold').place(x = 200, y = 120)
    #Label
    Label(text= "USERNAME:", font='times 20 bold').place(x = 60, y = 220)
    Label(text= "PASSWORD:", font='times 20 bold').place(x = 60, y = 270)
    #Login
    global user_name, password
    user_name = StringVar()
    password = StringVar()
    username_entry = Entry(login_screen, textvariable=user_name, width=20,bg="white", font='times 15 bold').place(x = 228, y = 225 )
    password_entry = Entry(login_screen, textvariable=password, show="*", width=20,bg="white", font='times 15 bold').place(x = 228, y = 277 )
    #--------------------------------------------
    submit = Button(login_screen, text="Confirm",bg="lightgreen", font='times 18 bold',command=log_in, width=25)
    submit.place(x = 70, y = 340)

    login_screen.mainloop()

def log_in():

    if user_name.get() == "admin" and password.get() == "admin":
        main_page()
    else:
        error_screen = Toplevel(login_screen)
        ttk.Label(error_screen, text="Wrong Username or Password").pack()
        ttk.Button(error_screen, text="Back", command=lambda: error_screen.withdraw()).pack()



def main_page():
    global main_screen
    login_screen.destroy()
    main_screen = Tk()
    main_screen.title("Main Page")
    main_screen.geometry("1300x700")
    main_screen.configure(bg='#FFEAAC')

    Label(main_screen, text="Main Menu", fg="white", bg="#E8A66D", font='times 35 bold', width="500", height="1").pack()
    headingline = Frame(main_screen, width=1300, height=5, bd=3, bg="#FF9380")
    headingline.pack(side=TOP)

    buttons_frame = Frame(main_screen, width=500, height=250)
    buttons_frame.place(x=90, y=80)

    items_button = Button(buttons_frame, text="Items", width=50, height=50, command=inventory_page)
    items_button.grid(row=0,column=0, padx=10)

    customer_button = Button(buttons_frame, text="Customer", width=50, height=50, command=customer_page)
    customer_button.grid(row=0, column=1, padx=10)

    invoice_button = Button(buttons_frame, text="Invoice", width=50, height=50)
    invoice_button.grid(row=0, column=2, padx=10)

    main_screen.mainloop()

def inventory_page():

    global inventory_screen
    Database.create_item_table()
    inventory_screen = Tk()
    #inventory_screen = Toplevel(main_screen)

    global itemid, itemdescription, itemtype
    itemid = StringVar()
    itemdescription = StringVar()
    itemtype = StringVar()

    inventory_screen.title("Inventory")
    inventory_screen.geometry("600x600")
    inventory_screen.configure(bg='#FFEAAC')
    inventory_screen.resizable(False, False)

    Label(inventory_screen, text="Items", fg="white", bg="#E8A66D", font='times 35 bold', width="500", height="1").pack()
    headingline = Frame(inventory_screen, width=600, height=5, bd=3, bg="#FF9380")
    headingline.pack(side=TOP)

    # Top Frame
    topframe = Frame(inventory_screen, width=1300, height=50, bd=3, bg='#FFEAAC')
    topframe.pack(side=TOP)
    # ------------------------------------------------------------------------------------
    # Inside Top Frame
    # Left Frame
    leftmidframe = Frame(topframe, width=650, height=50, bg='#FFEAAC')
    leftmidframe.pack(side=LEFT)

    # Add Button
    add_item_button = Button(leftmidframe, text="Add Item", font='times 10 bold', bd=2, relief='raise',
                             command=add_item_page)
    add_item_button.grid(row=0, column=0, padx=2)

    # Remove Button
    remove_Item_button = Button(leftmidframe, text="Remove Item", font='times 10 bold', bd=2, relief='raise', \
                                command=remove_item)
    remove_Item_button.grid(row=0, column=1, padx=2)
    # ---------------------------------------------

    # Frame
    inventoryframe = Frame(inventory_screen, width=1350, height=750, bd=2, relief='raise')
    inventoryframe.pack(side=TOP)

    # UI for Items List Treeview
    global items_list
    items_list = ttk.Treeview(inventoryframe)
    items_list["columns"] = ("description", "type", "qty")
    items_list.column("#0", width=150, minwidth=100, stretch="YES")
    items_list.column("description", width=200, minwidth=100, stretch="YES")
    items_list.column("type", width=120, minwidth=100)
    items_list.column("qty", width=120, minwidth=100)

    items_list.heading("#0", text="Item ID", anchor="w")
    items_list.heading("description", text="Item Description", anchor="w")
    items_list.heading("type", text="Item Type", anchor="w")
    items_list.heading("qty", text="Quantity", anchor="w")

    items_list.pack(pady=100)

    view = Database.get_item_list()
    for data in view:
        items_list.insert('', 'end', text=data[0], values=data[1:])

    inventory_screen.mainloop()


def add_item_page():
    global add_item_screen
    add_item_screen = Toplevel(inventory_screen)
    #add_item_screen = Tk()
    global itemid, itemdescription, itemtype, itemqty, cost
    itemid = StringVar()
    itemdescription = StringVar()
    itemtype = StringVar()
    itemqty = IntVar()
    cost = DoubleVar()

    add_item_screen.title("Add Item")
    add_item_screen.geometry("600x600")
    add_item_screen.configure(bg='#FFEAAC')
    add_item_screen.resizable(False, False)

    Label(add_item_screen, text="Add Item", fg="white", bg="#E8A66D", font='times 35 bold', width="500", height="1").pack()
    headingline = Frame(add_item_screen, width=600, height=5, bd=3, bg="#FF9380")
    headingline.pack(side=TOP)
    # Frame
    firstframe = Frame(add_item_screen, width=600, bg="grey", height=520, bd=1, relief='raise')
    firstframe.place(x=0, y=100)
    # Inside Frame
    firstframe = Frame(add_item_screen, width=250, height=520, bd=2, relief='raise')
    firstframe.place(x=2, y=102)
    secondframe = Frame(add_item_screen, width=350, height=520, bd=2, relief='raise')
    secondframe.place(x=253, y=102)

    # label And Entry
    label1 = Label(add_item_screen, text="Item ID:", font='calibri 25 ').place(x=5, y=150)
    label2 = Label(add_item_screen, text="Item Description:", font='calibri 25 ').place(x=5, y=200)
    label3 = Label(add_item_screen, text="Item Type:", font='calibri 25 ').place(x=5, y=250)
    label4 = Label(add_item_screen, text="Qty:", font='calibri 25 ').place(x=5, y=300)
    label5 = Label(add_item_screen, text="Cost:", font='calibri 25 ').place(x=5, y=350)

    entry1 = Entry(add_item_screen, textvariable=itemid, width=20, bg="white", font='calibri 18 ').place(x=270, y=155)
    entry2 = Entry(add_item_screen, textvariable=itemdescription, width=20, bg="white", font='calibri 18 ').place(x=270, y=205)
    entry3 = Entry(add_item_screen, textvariable=itemtype, width=20, bg="white", font='calibri 18 ').place(x=270, y=255)
    entry4 = Entry(add_item_screen, textvariable=itemqty, width=20, bg="white", font='calibri 18 ').place(x=270, y=305)
    entry5 = Entry(add_item_screen, textvariable=cost, width=20, bg="white", font='calibri 18 ').place(x=270, y=355)

    # Submit Button
    submit = Button(add_item_screen, text="Submit", bg="lightgreen", font='times 18 bold', width=17, \
                    command=submit_item)
    submit.place(x=270, y=395)

    add_item_screen.mainloop()

def remove_item():
    cur_item = items_list.focus()
    contents = items_list.item(cur_item)
    selected_item = contents['text']
    Database.delete_item(selected_item)
    items_list.delete(cur_item)

def submit_item():
    global item_id, item_description, item_type, item_qty, item_cost
    item_id = itemid.get().strip().title()
    item_description = itemdescription.get().strip().title()
    item_type = itemtype.get().strip().title()
    item_qty = int(itemqty.get())
    item_cost = float(cost.get())
    Database.add_item(item_id, item_description, item_type, item_qty, item_cost)
    items_list.delete(*items_list.get_children())
    get = Database.get_item_list()
    for data in get:
        items_list.insert('', 'end', text=data[0], values=data[1:])
    add_item_screen.withdraw()

def customer_page():
    global customer_screen
    Database.create_customer_table()

    customer_screen = Toplevel(main_screen)

    global customerid, itemdescription, itemtype
    customerid = StringVar()
    itemdescription = StringVar()
    itemtype = StringVar()

    customer_screen.title("Inventory")
    customer_screen.geometry("800x600")
    customer_screen.configure(bg='#FFEAAC')
    customer_screen.resizable(False, False)

    Label(customer_screen, text="Customer List", fg="white", bg="#E8A66D", font='times 35 bold', width="500",
          height="1").pack()
    headingline = Frame(customer_screen, width=800, height=5, bd=3, bg="#FF9380")
    headingline.pack(side=TOP)

    # Top Frame
    topframe = Frame(customer_screen, width=1300, height=50, bd=3, bg='#FFEAAC')
    topframe.pack(side=TOP)
    # ------------------------------------------------------------------------------------
    # Inside Top Frame
    # Left Frame
    leftmidframe = Frame(topframe, width=800, height=50, bg='#FFEAAC')
    leftmidframe.pack(side=LEFT)

    # Add Button
    add_customer_button = Button(leftmidframe, text="New Customer", font='times 10 bold', bd=2, relief='raise',
                             command=add_costumer_page)
    add_customer_button.grid(row=0, column=0, padx=2)

    # Remove Button
    remove_customer_button = Button(leftmidframe, text="Delete", font='times 10 bold', bd=2, relief='raise',
                                    command=remove_customer)
    remove_customer_button.grid(row=0, column=1, padx=2)
    # ---------------------------------------------

    # Frame
    customer_frame = Frame(customer_screen, width=790, height=750, bd=2, relief='raise')
    customer_frame.pack(side=TOP)

    # UI for Customer List Treeview
    global customer_list
    customer_list = ttk.Treeview(customer_frame)
    customer_list["columns"] = ("name", "address")
    customer_list.column("#0", width=150, minwidth=100, stretch="YES")
    customer_list.column("name", width=200, minwidth=100, stretch="YES")
    customer_list.column("address", width=400, minwidth=100, stretch="YES")

    customer_list.heading("#0", text="Customer ID", anchor="w")
    customer_list.heading("name", text="Name", anchor="w")
    customer_list.heading("address", text="Address", anchor="w")

    customer_list.pack(pady=100)

    view = Database.get_customer_list()
    for data in view:
        customer_list.insert('', 'end', text=data[0], values=data[1:])

    customer_screen.mainloop()

def remove_customer():
    cur_item = customer_list.focus()
    contents = customer_list.item(cur_item)
    selected_item = contents['text']
    Database.delete_customer(selected_item)
    customer_list.delete(cur_item)

def add_costumer_page():
    global add_customer_screen
    #add_customer_page = Toplevel(main_screen)
    add_customer_screen = Tk()

    add_customer_screen.title("New Customer")
    add_customer_screen.geometry("600x500")
    add_customer_screen.configure(bg='#FFEAAC')
    add_customer_screen.resizable(False, False)
    Label(add_customer_screen, text="New Customer", fg="white", bg="#E8A66D", font='times 28 bold', width="500",
          height="2").pack()
    headingline = Frame(add_customer_screen, width=800, height=4, bd=3, bg="#FF9380")
    headingline.pack(side=TOP)
    # Frame
    #firstframe = Frame(add_customer_screen, width=600, bg="#FFEAAC", height=520, bd=1, relief='raise')
    #firstframe.place(x=0, y=100)
    # Inside Frame
    secondframe = Frame(add_customer_screen, width=200, height=500, bd=2, relief='raise')
    secondframe.place(x=2, y=100)
    thirdframe = Frame(add_customer_screen, width=400, height=500, bd=2, relief='raise')
    thirdframe.place(x=203, y=100)

    # Variables
    global customerID, customerName, customerAddress
    customerID = StringVar()
    customerName = StringVar()
    customerAddress = StringVar()


    # label And Entry
    label1 = Label(secondframe, text="Customer ID:", font='calibri 25 ').place(x=5, y=50)
    label2 = Label(secondframe, text="Name:", font='calibri 25 ').place(x=5, y=100)
    label3 = Label(secondframe, text="Address:", font='calibri 25 ').place(x=5, y=150)

    entry1 = Entry(thirdframe, textvariable=customerID, width=20, bg="white", font='calibri 18 ')\
        .place(x=5, y=58)

    entry2 = Entry(thirdframe, textvariable=customerName, width=28, bg="white", font='calibri 18 ')\
        .place(x=5, y=108)

    entry3 = Entry(thirdframe, textvariable=customerAddress, width=30
                   , bg="white", font='calibri 18 ')\
        .place(x=5, y=158)
    # Submit Button
    submit = Button(thirdframe, text="Submit", bg="lightgreen", font='times 18 bold', width=17,
                    command=submit_new_customer)
    submit.place(x=65, y=250)

    add_customer_screen.mainloop()


def submit_new_customer():
    global customer_id, customer_name, customer_address

    customer_id = customerID.get().strip().title()
    customer_name = customerName.get().strip().title()
    customer_address = customerAddress.get().strip().title()
    print(customer_id, customer_name, customer_address)

    Database.add_customer(customer_id, customer_name, customer_address)

    customer_list.delete(*customer_list.get_children())

    get = Database.get_customer_list()
    for data in get:
        customer_list.insert('', 'end', text=data[0], values=data[1:])

    add_customer_screen.withdraw()

inventory_page()