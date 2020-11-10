import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar,DateEntry
from tkinter.scrolledtext import *
from tkinter import messagebox
import sqlite3
import csv

conn = sqlite3.connect('data.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXIST usersdata(firstname TEXT, lastname TEXT, email TEXT, age TEXT, date_of_birth TEXT, address TEXT, phonenumber REAL)')
    
def add_data(firstname, lastname, email, age, date_of_birth, address, phonenumber):
    c.execute('INSERT INTO userdata(firstname, lastname, email, age, date_of_birth, address, phonenumber) VALUES (?,?,?,?,?,?,?)', (firstname, lastname, email, age, date_of_birth, address, phonenumber))
    conn.commit()

def view_all_users():
    c.execute('SELECT * FROM usersdata')
    data = c.fetchall()
    for row in data:
        tree.insert('', tk.END, values = row)

def grt_single_user(irstname):
    c.execute('SELECT * FROM usersdata WHERE firstname = "{}"'.format(firstname))
    data = c.fetchall()
    return data

def clear_text():
    entry_fname.delete('0', END)
    entry_lname.delete('0', END)
    entry_email.delete('0', END)
    entry_age.delete('0', END)
    entry_address.delete('0', END)
    entry_phone.delete('0', END)



window = Tk()
window.title("Regitrio GUI")
window.geometry("750x450")

style = ttk.Style(window)
style.configure("lefttab.TNotebook", tabposition = "wm")

tab_control = ttk.Notebook(window, style = "lefttab.TNotebook")

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)

tab_control.add(tab1,text = f'{"Home":^20s}')
tab_control.add(tab2,text = f'{"View":^20s}')
tab_control.add(tab3,text = f'{"Search":^20s}')
tab_control.add(tab4,text = f'{"Export":^20s}')
tab_control.add(tab5,text = f'{"About":^20s}')

tab_control.pack(expand = 1, fill = "both")

label1 = Label(tab1, text = 'Registrio GUI', padx = 5, pady = 5)
label1.grid(column = 0, row = 0)

label2 = Label(tab2, text = 'View', padx = 5, pady = 5)
label2.grid(column = 0, row = 0)

label3 = Label(tab3, text = 'Serach', padx = 5, pady = 5)
label3.grid(column = 0, row = 0)

label4 = Label(tab4, text = 'Export', padx = 5, pady = 5)
label4.grid(column = 0, row = 0)

label5 = Label(tab5, text = 'About', padx = 5, pady = 5)
label5.grid(column = 0, row = 0)

#main Home
l1 = Label(tab1, text = 'First Name', padx = 5, pady = 5)
l1.grid(column = 0, row = 1)
fname_raw_entry = StringVar()
entry_fname = Entry(tab1, textvariable = fname_raw_entry, width = 50)
entry_fname.grid(row = 1, column = 1)

l2 = Label(tab1, text = 'Last Name', padx = 5, pady = 5)
l2.grid(column = 0, row = 2)
lname_raw_entry = StringVar()
entry_lname = Entry(tab1, textvariable = lname_raw_entry, width = 50)
entry_lname.grid(row = 2, column = 1)

l3 = Label(tab1, text = 'Email', padx = 5, pady = 5)
l3.grid(column = 0, row = 3)
email_raw_entry = StringVar()
entry_email = Entry(tab1, textvariable = email_raw_entry, width = 50)
entry_email.grid(row = 3, column = 1)

l4 = Label(tab1, text = 'Age', padx = 5, pady = 5)
l4.grid(column = 0, row = 4)
age_raw_entry = StringVar()
entry_age = Entry(tab1, textvariable = age_raw_entry, width = 50)
entry_age.grid(row = 4, column = 1)

l5 = Label(tab1, text = 'Date of birth', padx = 5, pady = 5)
l5.grid(column = 0, row = 5)
dob_raw_entry = StringVar()
cal = DateEntry(tab1, width = 30, textvariable = dob_raw_entry, background = 'darkblue', foreground = 'white', bordrwidth = 2, year = 2020)
cal.grid(row = 5, column = 1, padx = 10, pady = 10)

l6 = Label(tab1, text = 'Address', padx = 5, pady = 5)
l6.grid(column = 0, row = 6)
address_raw_entry = StringVar()
entry_address = Entry(tab1, textvariable = address_raw_entry, width = 50)
entry_address.grid(row = 6, column = 1)

l7 = Label(tab1, text = 'Phone Number', padx = 5, pady = 5)
l7.grid(column = 0, row = 7)
phone_raw_entry = StringVar()
entry_phone = Entry(tab1, textvariable = phone_raw_entry, width = 50)
entry_phone.grid(row = 7, column = 1)

button1 = Button(tab1, text = 'Add', width = 12, bg = '#03A9F4', fg = '#fff')
button1.grid(row = 8, column = 0, pady = 5)

button2 = Button(tab1, text = 'Clear', width = 12, bg = '#03A9F4', fg = '#fff')
button2.grid(row = 8, column = 1, padx = 5, pady = 5)

#Display Screen

tab1_display = ScrolledText(tab1, height = 5)
tab1_display.grid(row = 10, column = 1, padx = 5, pady = 5, columnspan = 3)

button3 = Button(tab1, text = 'Clear Result', width = 12, bg = '#03A9F4', fg = '#fff')
button3.grid(row = 12, column = 1, padx = 10, pady = 10)

#View

button_view2 = Button(tab2, text = 'View All', width = 12, bg = '#03A9F4', fg = '#fff', command = view_all_users)
button_view2.geid(row = 1, column = 0, padx = 10, pady = 10)
tree = ttk.Treeview(tab2, column = ('column1', 'column2', 'column3', 'column4', 'column5', 'column6', 'column7'), show = 'headings')
tree.heading('#1', text = 'First Name')
tree.heading('#2', text = 'Last Name')
tree.heading('#3', text = 'Age')
tree.heading('#1', text = '')
tree.heading('#2', text = '')
tree.heading('#3', text = 'SURNAME')
tree.heading('#7', text = 'Phone Number')
tree.grid(row = 10, column = 3, columnspan = 3, padx = 5, pady = 5)

#Search

label_search1 = Label(tab3, text = 'Search Name', padx = 5, pady = 5)
label_search1.grid(column = 0, row = 1)
search_raw_entry = StringVar()
entry_search = entry(tab3, textvariable = search_raw_entry, width = 30)
entry_search.grid(row = 1, column = 1)

button_view3 = Button(tab3, text = 'Clear Search', width = 12, bg = '#03A9F4', fg = '#fff', command = clear_enter)

window.mainloop()