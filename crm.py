import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector
import csv
from tkinter import ttk, messagebox
from pathlib import Path

root = tk.Tk()
root.title("CRM Database")
root.geometry("400x600")

mydb = mysql.connector.connect(
        host="localhost",
        user="lokesh",
        passwd="password",
        database="tkinter",
    )

# Check if the connection was created
# print(mydb)

my_cursor = mydb.cursor()

# Create a database(one-time)
# my_cursor.execute("create database tkinter")

# Test if database is created
# my_cursor.execute("show databases")
# for db in my_cursor:
#     print(db)

# Create the customers table(one-time)
# my_cursor.execute("create table customers (\
#         first_name varchar(50),\
#         last_name varchar(50),\
#         zipcode int(10),\
#         price_paid decimal(10, 2),\
#         user_id int auto_increment primary key)")

# Alter table to add new columns (one-time)
# my_cursor.execute("alter table customers add (\
#         email varchar(255),\
#         address_1 varchar(255),\
#         address_2 varchar(255),\
#         city varchar(50),\
#         state varchar(50),\
#         country varchar(255),\
#         phone varchar(255),\
#         payment_method varchar(255),\
#         discount_code varchar(255))")

# Test if table is created
# my_cursor.execute("select * from customers")
# for item in my_cursor.description:
#     print(item)


# Clear text fields
def clear_fields():
    first_name_box.delete(0, tk.END)
    last_name_box.delete(0, tk.END)
    address_1_box.delete(0, tk.END)
    address_2_box.delete(0, tk.END)
    city_box.delete(0, tk.END)
    state_box.delete(0, tk.END)
    zipcode_box.delete(0, tk.END)
    country_box.delete(0, tk.END)
    phone_box.delete(0, tk.END)
    email_box.delete(0, tk.END)
    payment_method_box.delete(0, tk.END)
    discount_code_box.delete(0, tk.END)
    price_paid_box.delete(0, tk.END)

def add_customer():
    query = "insert into customers (\
            first_name,\
            last_name,\
            address_1,\
            address_2,\
            city,\
            state,\
            zipcode,\
            country,\
            phone,\
            email,\
            payment_method,\
            discount_code,\
            price_paid\
            ) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    values = (
            first_name_box.get(),
            last_name_box.get(),
            address_1_box.get(),
            address_2_box.get(),
            city_box.get(),
            state_box.get(),
            zipcode_box.get(),
            country_box.get(),
            phone_box.get(),
            email_box.get(),
            payment_method_box.get(),
            discount_code_box.get(),
            price_paid_box.get(),
            )

    my_cursor.execute(query, values)
    mydb.commit()

    clear_fields()

def write_to_csv(records):
    Path('public').mkdir(parents=True, exist_ok=True)
    with open('public/customers.csv', 'w', newline="") as f:
        w = csv.writer(f, dialect='excel')
        for record in records:
            w.writerow(record)

def update_record(frame, record):
    # Create labels
    first_name_label = tk.Label(frame, text="First Name").grid(row=1, column=0, sticky=tk.W, padx=10)
    last_name_label = tk.Label(frame, text="Last Name").grid(row=2, column=0, sticky=tk.W, padx=10)
    address_1_label = tk.Label(frame, text="Address 1").grid(row=3, column=0, sticky=tk.W, padx=10)
    address_2_label = tk.Label(frame, text="Address 2").grid(row=4, column=0, sticky=tk.W, padx=10)
    city_label = tk.Label(frame, text="City").grid(row=5, column=0, sticky=tk.W, padx=10)
    state_label = tk.Label(frame, text="State").grid(row=6, column=0, sticky=tk.W, padx=10)
    zipdcode_label = tk.Label(frame, text="Zipcode").grid(row=7, column=0, sticky=tk.W, padx=10)
    country_label = tk.Label(frame, text="Country").grid(row=8, column=0, sticky=tk.W, padx=10)
    phone_label = tk.Label(frame, text="Phone Number").grid(row=9, column=0, sticky=tk.W, padx=10)
    email_label = tk.Label(frame, text="Email Address").grid(row=10, column=0, sticky=tk.W, padx=10)
    payment_method_label = tk.Label(frame, text="Payment Method").grid(row=11, column=0, sticky=tk.W, padx=10)
    discount_code_label = tk.Label(frame, text="Discount Code").grid(row=12, column=0, sticky=tk.W, padx=10)
    price_paid_label = tk.Label(frame, text="Price Paid").grid(row=13, column=0, sticky=tk.W, padx=10)

    # Create Entry boxes
    first_name_box = tk.Entry(frame)
    first_name_box.grid(row=1, column=1, pady=5)
    first_name_box.insert(0, record[0])

    last_name_box = tk.Entry(frame)
    last_name_box.grid(row=2, column=1, pady=5)
    last_name_box.insert(0, record[1])

    address_1_box = tk.Entry(frame)
    address_1_box.grid(row=3, column=1, pady=5)
    address_1_box.insert(0, record[6])

    address_2_box = tk.Entry(frame)
    address_2_box.grid(row=4, column=1, pady=5)
    address_2_box.insert(0, record[7])

    city_box = tk.Entry(frame)
    city_box.grid(row=5, column=1, pady=5)
    city_box.insert(0, record[8])

    state_box = tk.Entry(frame)
    state_box.grid(row=6, column=1, pady=5)
    state_box.insert(0, record[9])

    zipcode_box = tk.Entry(frame)
    zipcode_box.grid(row=7, column=1, pady=5)
    zipcode_box.insert(0, record[2])

    country_box = tk.Entry(frame)
    country_box.grid(row=8, column=1, pady=5)
    country_box.insert(0, record[10])

    phone_box = tk.Entry(frame)
    phone_box.grid(row=9, column=1, pady=5)
    phone_box.insert(0, record[11])

    email_box = tk.Entry(frame)
    email_box.grid(row=10, column=1, pady=5)
    email_box.insert(0, record[5])

    payment_method_box = tk.Entry(frame)
    payment_method_box.grid(row=11, column=1, pady=5)
    payment_method_box.insert(0, record[12])

    discount_code_box = tk.Entry(frame)
    discount_code_box.grid(row=12, column=1, pady=5)
    discount_code_box.insert(0, record[13])

    price_paid_box = tk.Entry(frame)
    price_paid_box.grid(row=13, column=1, pady=5)
    price_paid_box.insert(0, record[3])

    def update_now():
        query = "update customers\
                set first_name=%s,\
                last_name=%s,\
                address_1=%s,\
                address_2=%s,\
                city=%s,\
                state=%s,\
                zipcode=%s,\
                country=%s,\
                phone=%s,\
                email=%s,\
                payment_method=%s,\
                discount_code=%s,\
                price_paid=%s where user_id=%s"

        values = (
                first_name_box.get(),
                last_name_box.get(),
                address_1_box.get(),
                address_2_box.get(),
                city_box.get(),
                state_box.get(),
                zipcode_box.get(),
                country_box.get(),
                phone_box.get(),
                email_box.get(),
                payment_method_box.get(),
                discount_code_box.get(),
                price_paid_box.get(),
                record[4],
                )

        my_cursor.execute(query, values)
        mydb.commit()
        frame.destroy()


    update_button = tk.Button(frame, text="Update Now", command=update_now)
    update_button.grid(row=14, column=0)

def list_customers():
    window = tk.Tk()
    window.title("List All Customers")
    window.geometry("800x600")

    my_cursor.execute("select * from customers")
    result = my_cursor.fetchall()
    list_frame = tk.LabelFrame(window, borderwidth=0, highlightthickness=0)
    list_frame.grid(row=0, column=0, sticky="nesw")
    edit_frame = tk.LabelFrame(window, borderwidth=0, highlightthickness=0)
    edit_frame.grid(row=1, column=0, sticky="nesw")
    for index, record in enumerate(result):
        edit_button = tk.Button(list_frame, text="Edit", command=lambda: update_record(edit_frame, record))
        edit_button.grid(row=index, column=0, padx=10, pady=10)
        for column, item in enumerate(record):
            lookup_label = tk.Label(list_frame, text=record[column])
            lookup_label.grid(row=index, column=column+1)

    csv_button = tk.Button(list_frame, text="Save to Excel", command=lambda: write_to_csv(result))
    csv_button.grid(row=index+1, column=0)

def search_customers():
    window = tk.Tk()
    window.title("Search Customers")
    window.geometry("800x600")

    search_box_frame = tk.LabelFrame(window, borderwidth=0, highlightthickness=0)
    search_box_frame.grid(row=0, column=0, ipady=10, sticky="nesw")
    result_frame = tk.LabelFrame(window, borderwidth=0, highlightthickness=0)
    result_frame.grid(row=1, column=0, ipady=10, sticky="nesw")
    edit_frame = tk.LabelFrame(window, borderwidth=0, highlightthickness=0)
    edit_frame.grid(row=2, column=0, sticky="nesw")

    def search_now(selected, searched):
        if selected == "Search by...":
            messagebox.showerror("Result", "Select some parameter to search by")
            return
        elif selected == "First Name":
            selected = "first_name"
        elif selected == "Last Name":
            selected = "last_name"
        elif selected == "Email Address":
            selected = "email"
        elif selected == "Id":
            selected = "user_id"

        query = "select * from customers where " + selected + " = '" + searched + "'"

        my_cursor.execute(query)
        result = my_cursor.fetchall()

        if not result:
            messagebox.showinfo("Result", "Record doesn't exist")

        else:
            for index, record in enumerate(result):
                edit_button = tk.Button(result_frame, text="Edit", command=lambda: update_record(edit_frame, record))
                edit_button.grid(row=index, column=0, padx=10, pady=10)
                for column, item in enumerate(record):
                    lookup_label = tk.Label(result_frame, text=record[column])
                    lookup_label.grid(row=index, column=column+1)

            csv_button = tk.Button(result_frame, text="Save to Excel", command=lambda: write_to_csv(result))
            csv_button.grid(row=index+1, column=0)

    search_label = tk.Label(search_box_frame, text="Search Customer:")
    search_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    search_box = tk.Entry(search_box_frame)
    search_box.grid(row=0, column=1, padx=10, pady=10, sticky=tk.N + tk.E + tk.S + tk.W)

    drop = ttk.Combobox(search_box_frame, value=[
        "Search by...", 
        "First Name", 
        "Last Name", 
        "Email Address", 
        "Id"
    ])
    drop.current(0)
    drop.grid(row=0, column=2, sticky=tk.E)

    search_button = tk.Button(
            search_box_frame, 
            text="Search Now", 
            command=lambda: search_now(drop.get(), search_box.get())
        )
    search_button.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)


# Create title label
title_label = tk.Label(root, text="Customer Database", font=("Helvetica", 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# Create Main Form to enter customer data
first_name_label = tk.Label(root, text="First Name").grid(row=1, column=0, sticky=tk.W, padx=10)
last_name_label = tk.Label(root, text="Last Name").grid(row=2, column=0, sticky=tk.W, padx=10)
address_1_label = tk.Label(root, text="Address 1").grid(row=3, column=0, sticky=tk.W, padx=10)
address_2_label = tk.Label(root, text="Address 2").grid(row=4, column=0, sticky=tk.W, padx=10)
city_label = tk.Label(root, text="City").grid(row=5, column=0, sticky=tk.W, padx=10)
state_label = tk.Label(root, text="State").grid(row=6, column=0, sticky=tk.W, padx=10)
zipdcode_label = tk.Label(root, text="Zipcode").grid(row=7, column=0, sticky=tk.W, padx=10)
country_label = tk.Label(root, text="Country").grid(row=8, column=0, sticky=tk.W, padx=10)
phone_label = tk.Label(root, text="Phone Number").grid(row=9, column=0, sticky=tk.W, padx=10)
email_label = tk.Label(root, text="Email Address").grid(row=10, column=0, sticky=tk.W, padx=10)
payment_method_label = tk.Label(root, text="Payment Method").grid(row=11, column=0, sticky=tk.W, padx=10)
discount_code_label = tk.Label(root, text="Discount Code").grid(row=12, column=0, sticky=tk.W, padx=10)
price_paid_label = tk.Label(root, text="Price Paid").grid(row=13, column=0, sticky=tk.W, padx=10)

# Create Entry boxes
first_name_box = tk.Entry(root)
first_name_box.grid(row=1, column=1, pady=5)

last_name_box = tk.Entry(root)
last_name_box.grid(row=2, column=1, pady=5)

address_1_box = tk.Entry(root)
address_1_box.grid(row=3, column=1, pady=5)

address_2_box = tk.Entry(root)
address_2_box.grid(row=4, column=1, pady=5)

city_box = tk.Entry(root)
city_box.grid(row=5, column=1, pady=5)

state_box = tk.Entry(root)
state_box.grid(row=6, column=1, pady=5)

zipcode_box = tk.Entry(root)
zipcode_box.grid(row=7, column=1, pady=5)

country_box = tk.Entry(root)
country_box.grid(row=8, column=1, pady=5)

phone_box = tk.Entry(root)
phone_box.grid(row=9, column=1, pady=5)

email_box = tk.Entry(root)
email_box.grid(row=10, column=1, pady=5)

payment_method_box = tk.Entry(root)
payment_method_box.grid(row=11, column=1, pady=5)

discount_code_box = tk.Entry(root)
discount_code_box.grid(row=12, column=1, pady=5)

price_paid_box = tk.Entry(root)
price_paid_box.grid(row=13, column=1, pady=5)

add_customer_button = tk.Button(root, text="Add Customer To Database", command=add_customer)
add_customer_button.grid(row=14, column=0, sticky=tk.W, padx=10, pady=10)
clear_fields_button = tk.Button(root, text="Clear Fields", command=clear_fields)
clear_fields_button.grid(row=14, column=1, sticky=tk.W, padx=10, pady=10)
list_customers_button = tk.Button(root, text="List Customers", command=list_customers)
list_customers_button.grid(row=15, column=0, sticky=tk.W, padx=10)
search_customers_button = tk.Button(root, text="Search Customers", command=search_customers)
search_customers_button.grid(row=15, column=1, sticky=tk.W, padx=10)

root.mainloop()
