# this line is be use to import mysql connector with an alias of con in other to link up this whole program to the data base.
import mysql.connector as con
# this line imports the date and time module to this program with an alias of dt.
import datetime as dt
# this function is responsible for option selection throughout this program.
def my_select():
    global select
    select = input("Make a selection: ")

# welcome is the starting point of this program
def welcome():
    print("Welcome to First Bank.\n 1.Create an account. \n 2.Log in to your account.")
    my_select()
    if select == "1":
        print("work")
    elif select == "2":
        print("done")
    else:
        print("Sorry, Invalid selection.")

welcome()