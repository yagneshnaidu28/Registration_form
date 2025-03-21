import mysql.connector
from tkinter import *

root = Tk()
root.geometry("500x300")

# MySQL connection setup
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # replace with your MySQL username
        password="Yagneshram@28",  # replace with your MySQL password
        database="registration_db"  # replace with your database name
    )

def getvals():
    # Getting the data from the form
    name_data = nameval.get()
    number_data = numberval.get()
    gender_data = genderval.get()
    remember_me_data = Checkval.get()
    
    # Connecting to MySQL
    db_connection = connect_to_db()
    cursor = db_connection.cursor()
    
    # SQL query to insert data into the table
    insert_query = """
    INSERT INTO users (name, number, gender, remember_me)
    VALUES (%s, %s, %s, %s)
    """
    
    cursor.execute(insert_query, (name_data, number_data, gender_data, remember_me_data))
    db_connection.commit()
    print("Data successfully saved into the database!")
    
    # Close the cursor and connection
    cursor.close()
    db_connection.close()

# Heading
Label(root, text="Registration Form", font="ar 15 bold").grid(row=0, column=3)

# Field names
name = Label(root, text="Name")
number = Label(root, text="Number")
gender = Label(root, text="Gender")

# Packing fields
name.grid(row=1, column=2)
number.grid(row=2, column=2)
gender.grid(row=3, column=2)

# Variable for storing data
nameval = StringVar()
numberval = StringVar()
genderval = StringVar()

Checkval = IntVar()

# Creating entry fields
nameentry = Entry(root, textvariable=nameval)
numberentry = Entry(root, textvariable=numberval)
genderentry = Entry(root, textvariable=genderval)

# Packing entry fields
nameentry.grid(row=1, column=3)
numberentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)

# Check button for "Remember Me"
checkbtn = Checkbutton(root, text="Remember me", variable=Checkval)
checkbtn.grid(row=4, column=3)

# Button to submit
Button(root, text="Submit", command=getvals).grid(row=5, column=3)

root.mainloop()
