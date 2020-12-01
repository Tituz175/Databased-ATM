# this line is be use to import mysql connector with an alias of con in other to link up this whole program to the data base.
import mysql.connector as con
# this line imports the date and time module to this program with an alias of dt.
import datetime as dt

# this lines links to the database.
db = con.connect(host="localhost",database="db_atm",username="root",password="")
cursor = db.cursor()

# this function is responsible for option selection throughout this program.
def my_select():
    global select
    select = input("Make a selection: ")

def db_check():
    global user_id
    global phone
    query = "select User_id, Phone from users where Email = %s and Pin = %s"
    values = (login_email,login_pin)
    cursor.execute(query,values)
    result = cursor.fetchone()
    if result == None:
        print("Sorry, Your login details are invalid.")
        print("\n")
        welcome()
    else:
        user_id = result[0]
        phone = result[1]
        print("Welcome")
        #user_dashboard()

def login():
    global login_email
    global login_pin
    print("Welcome, we are glad to have you here.")
    login_email = input("Please input your E-mail: ")
    login_pin = input("Please input your Password: ")
    db_check()

# this function updates the database with the newly created user's details.
def db_update():
    query = "insert into users(First_Name,Last_Name,Email,Phone,Pin)values(%s,%s,%s,%s,%s)"
    values = (first_name,last_name,email,phone,pin)
    cursor.execute(query,values)
    db.commit()

# this function is responsible for user's registration. email must be unique. 
def registration():
    global first_name
    global last_name
    global email
    global phone
    global pin
    print("\nWelcome, we are glad to have you here.\nPlease give answers to the following questions.")
    first_name = input("What is your First Name? ")
    last_name = input("What is your Last Name? ")
    email = input("Please enter your E-mail ")
    phone = input("Please enter your Phone number ")
    pin = input("Input desire Pin ")
    confirm = input("Please confirm your Pin ")
    query = "select * from users where Email = %s"
    value = (email)
    cursor.execute(query,(value,))
    result = cursor.fetchone()
    if result == None:
        if pin == confirm:
            db_update()
            print("\nAccount created sucessfully.\nDo you want to login?\n1. Yes\n2. No")
            my_select()
            if select == "1":
                login()
            # elif select == "2":
            #     log_out()
        else:
            print("\nYou input unmatchable passwords.\nPlease restart the registration again.\n")
            registration()
    else:
        print("Used Email! Please input a unused Email.")
        print(" ")
        welcome()

# welcome is the starting point of this program
def welcome():
    print("Welcome to First Bank.\n 1.Create an account. \n 2.Log in to your account.")
    my_select()
    if select == "1":
        registration()
    elif select == "2":
        login()
    else:
        print("Sorry, Invalid selection.")

welcome()