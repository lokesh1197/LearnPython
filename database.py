from tkinter import Tk, Entry, Label, Button, END, Toplevel, messagebox, DISABLED
import sqlite3

root = Tk()
root.title("Learn about database")
root.geometry("400x230")

# Create table
'''
cursor.execute("""CREATE TABLE addresses (
                first_name text,
                last_name text,
                address text,
                city text,
                state text,
                zipcode integer
            )""")
'''

# Create view function for database
def view():
    # Create a database or connect to one
    conn = sqlite3.connect('public/address_book.db')
    # Create cursor
    cursor = conn.cursor()

    # Query the database
    cursor.execute("SELECT *, oid FROM addresses")
    records = cursor.fetchall()

    # Close the connection
    conn.close()

    if len(records) == 0:
        messagebox.showinfo("No records. Please add some to view")
        return

    # Create a new window
    window = Toplevel()

    # Create text box labels
    f_name_label = Label(window, text="First Name")
    f_name_label.grid(row=1, column=0)

    l_name_label = Label(window, text="Last Name")
    l_name_label.grid(row=2, column=0)

    address_label = Label(window, text="Address")
    address_label.grid(row=3, column=0)

    city_label = Label(window, text="City")
    city_label.grid(row=4, column=0)

    state_label = Label(window, text="State")
    state_label.grid(row=5, column=0)

    zipcode_label = Label(window, text="Zipcode")
    zipcode_label.grid(row=6, column=0)

    records_label = {}

    def view_record(index):
        id = records[index][-1:][0]
        count_label = Label(window, text="Record " + str(index + 1) + " of " + str(len(records)))
        count_label.grid(row=0, column=0, columnspan=2, padx=50, pady=10)

        # Show data
        i = 1
        for key in records_label:
            records_label[key].destroy()

        for cell in records[index][:-1]:
            records_label[i - 1] = Label(window, text=str(cell))
            records_label[i - 1].grid(row=i, column=1)
            i += 1

        # Create update and delete record buttons
        update_btn = Button(window, text="Update", command=lambda: update(index))
        delete_btn = Button(window, text="Delete", command=lambda: delete(index))
        update_btn.grid(row=8, column=0)
        delete_btn.grid(row=8, column=1)

        # Create previous and next record buttons
        previous_btn = Button(window, text="Previous record", command=lambda: view_record(index - 1))
        next_btn = Button(window, text="Next record", command=lambda: view_record(index + 1))

        if index == 0:
            previous_btn = Button(window, text="Previous record", state=DISABLED)
        if index == len(records) - 1:
            next_btn = Button(window, text="Next record", state=DISABLED)

        previous_btn.grid(row=7, column=0)
        next_btn.grid(row=7, column=1)

    def update(index):
        id = records[index][-1:][0]
        record = records[index][:-1]

        # Create text boxes
        f_name = Entry(window, width=30)
        f_name.grid(row=1, column=1, padx=20)
        f_name.insert(0, record[0])

        l_name = Entry(window, width=30)
        l_name.grid(row=2, column=1, padx=20)
        l_name.insert(0, record[1])

        address = Entry(window, width=30)
        address.grid(row=3, column=1, padx=20)
        address.insert(0, record[2])

        city = Entry(window, width=30)
        city.grid(row=4, column=1, padx=20)
        city.insert(0, record[3])

        state = Entry(window, width=30)
        state.grid(row=5, column=1, padx=20)
        state.insert(0, record[4])

        zipcode = Entry(window, width=30)
        zipcode.grid(row=6, column=1, padx=20)
        zipcode.insert(0, record[5])

        def confirm_update(id, index):
            records[index] = (f_name.get(), l_name.get(), address.get(), city.get(), state.get(), zipcode.get(), id)
            # Create a database or connect to one
            conn = sqlite3.connect('address_book.db')

            # Create cursor
            cursor = conn.cursor()

            # Query the database
            cursor.execute("UPDATE addresses SET first_name=?, last_name=?, address=?, city=?, state=?, zipcode=? WHERE oid=?", records[index])

            # Commit changes
            conn.commit()

            # Close connection
            conn.close()


            # Destroy temporary entries
            f_name.destroy()
            l_name.destroy()
            address.destroy()
            city.destroy()
            state.destroy()
            zipcode.destroy()

            # Destroy temporary buttons
            confirm_btn.destroy()
            cancel_btn.destroy()
            previous_btn.destroy()
            next_btn.destroy()

            view_record(index)


        # Create update and delete record buttons
        confirm_btn = Button(window, text="Confirm", command=lambda: confirm_update(id, index))
        cancel_btn = Button(window, text="Cancel", command=lambda: view_record(index))
        confirm_btn.grid(row=8, column=0)
        cancel_btn.grid(row=8, column=1)

        # Create previous and next record buttons
        previous_btn = Button(window, text="Previous record", state=DISABLED)
        next_btn = Button(window, text="Next record", state=DISABLED)
        previous_btn.grid(row=7, column=0)
        next_btn.grid(row=7, column=1)

    def delete(index):
        id = records[index][-1:][0]

        # Create a database or connect to one
        conn = sqlite3.connect('address_book.db')

        # Create cursor
        cursor = conn.cursor()

        # Query the database
        cursor.execute("DELETE FROM addresses WHERE oid=?", (id,))

        # Commit changes
        conn.commit()

        # Close connection
        conn.close()

        records.pop(index)

        if len(records) == 0:
            messagebox.showinfo("No records. Please add some to view")

        if index == 0:
            view_record(1)
        else:
            view_record(index - 1)


    # Create exit button
    exit_btn = Button(window, text="Exit", command=window.destroy)
    exit_btn.grid(row=9, column=0, columnspan=2, padx=10, ipadx=165)

    view_record(0)

# Create submit function for database
def submit():
    # Create a database or connect to one
    conn = sqlite3.connect('address_book.db')
    # Create cursor
    cursor = conn.cursor()

    # Insert into table
    cursor.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)", 
            { 
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zipcode.get(),
            })

    # Commit changes
    conn.commit()

    # Close the connection to the database
    conn.close()

    # Clear the text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create text boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=20)

# Create text box labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0)

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zipcode_label = Label(root, text="Zipcode")
zipcode_label.grid(row=5, column=0)

# Create submit button
submit_btn = Button(root, text="Add record to database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, ipadx=100)

# Create view button
view_btn = Button(root, text="View records", command=view)
view_btn.grid(row=7, column=0, columnspan=2, padx=10, ipadx=135)

# Create exit button
exit_btn = Button(root, text="Exit", command=root.destroy)
exit_btn.grid(row=8, column=0, columnspan=2, padx=10, ipadx=165)

root.mainloop()
