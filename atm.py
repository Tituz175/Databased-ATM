# this line is be use to import mysql connector with an alias of con in other to link up this whole program to the data base.
import mysql.connector as con
# this line imports the date and time module to this program with an alias of dt.
import datetime as dt

# this lines links to the database.
db = con.connect(host="localhost",database="db_atm",username="root",password="")
cursor = db.cursor()

def my_time():
    global thyme
    global my_date
    gen_time = dt.datetime.now()
    thyme = gen_time.strftime("%I") + ":" + gen_time.strftime("%M") + gen_time.strftime("%p")
    my_date = gen_time.strftime("%d") + "-" + gen_time.strftime("%m") + "-" + gen_time.strftime("%Y")

# this function is responsible for option selection throughout this program.
def my_select():
    global select
    select = input("Make a selection: ")

# this function is responsible for the promting of the user for another transaction.
def another_option():
    print("Do you want to perform another transaction?\n1.Yes\n2.No")
    my_select()

def money_out(i):
    my_time()
    query = "select Balance, First_Name, Last_Name from users where User_id = %s"
    value = (user_id)
    cursor.execute(query,(value,))
    result = cursor.fetchone()
    balance_before = result[0]
    balance_after = result[0] - i
    query = "update users set Balance = %s where User_id = %s"
    values = (balance_after,user_id)
    cursor.execute(query,values)
    db.commit()
    query = "insert into transactions(User_id, Date, Time, Balance_Before, Debit, Balance_After, Remark, Status)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    values = (user_id,my_date,thyme,balance_before,i,balance_after," withdrawn #" + str(i),"Successful")
    cursor.execute(query,values)
    db.commit()
    print("\n" + result[1] + " " + result[2] + ", your transaction was successful.")

def proceed_transaction():
    print("\nDo you want to proceed with this transaction?\n1. Yes\n2. No")
    my_select()
    if select == "1":
        money_out(amount)
    elif select == "2":
        print("Your transaction terminated.")
        my_withdraw()
    else:
        print("Sorry, your selection is invalid.")
        user_dashboard()

def my_check(i):
    global amount
    global checkResult
    amount = i
    query = "select Balance from users where User_id = %s"
    value = (user_id)
    cursor.execute(query,(value,))
    result = cursor.fetchone()
    print(result[0])
    checkResult = result[0] >= i
    print (checkResult)

def my_withdraw():
    query = "select First_Name from users where User_id = %s"
    value = (user_id)
    cursor.execute(query,(value,))
    result = cursor.fetchone()
    print("\n" + result[0] + ", how much do you want to withdraw?\n1. #10000\n2. #5000\n3. #2000\n4. #1000\n5. #500\n6. Others\n7. Back")
    my_select()
    if select == "1":
        my_check(10000)
        if checkResult == True:
            proceed_transaction()
            another_option()
            if select == "1":
                my_withdraw()
            elif select == "2":
                user_dashboard()
            else:
                return print("Sorry, Invalid selection.")
        else:
            print("Sorry, You do not have sufficient fund.")
    elif select == "2":
        my_check(5000)
        another_option()
        if select == "1":
            my_withdraw()
        elif select == "2":
            user_dashboard()
        else:
            return print("Sorry, Invalid selection.")
    elif select == "3":
        my_check(2000)
        another_option()
        if select == "1":
            my_withdraw()
        elif select == "2":
            user_dashboard()
        else:
            return print("Sorry, Invalid selection.")
    elif select == "4":
        my_check(1000)
        another_option()
        if select == "1":
            my_withdraw()
        elif select == "2":
            user_dashboard()
        else:
            return print("Sorry, Invalid selection.")
    elif select == "5":
        my_check(500)
        another_option()
        if select == "1":
            my_withdraw()
        elif select == "2":
            user_dashboard()
        else:
            return print("Sorry, Invalid selection.")
    elif select == "6":
        pass
        # my_other()
        # my_check(otherMoney)
        # another_option()
        # if select == "1":
        #     my_withdraw()
        # elif select == "2":
        #     user_dashboard()
        # else:
        #     return print("Sorry, Invalid selection.")
    elif select == "7":
        user_dashboard()
    else:
        print("Sorry, Invalid selection.")
        user_dashboard()

# function is charge of checking and displaying user's balance.
def my_balance():
    query = "select First_Name, Last_Name, Balance from users where User_id = %s"
    value = (user_id)
    cursor.execute(query,(value,))
    result = cursor.fetchone()
    print(result[0] + " " + result[1] + ", your current balance is #" + str(result[2]) + ".")
    another_option()
    if select == "1":
        user_dashboard()
    elif select == "2":
        log_out()
    else:
        return print("Sorry, Invalid selection.")

# function log out the user.
def log_out():
    query = "select First_Name, Last_Name from users where User_id = %s"
    value = (user_id)
    cursor.execute(query,(value,))
    result = cursor.fetchone()
    print("\nThank you, " + result[0] +" "+ result[1] + " for banking with us. Have a nice day.\n")

# this function print out the user dashboard environment.
def user_dashboard():
    query = "select First_Name, Last_Name from users where User_id = %s"
    value = (user_id)
    cursor.execute(query,(value,))
    result = cursor.fetchone()
    print("\nWelcome " + result[0] +" "+ result[1] + ".\n1. Withdraw Fund\n2. Transfer Fund\n3. Mobile Top-up\n4. Balance\n5. Histroy\n6. Log Out")
    my_select()
    if select == "1":
        my_withdraw()
    elif select == "2":
        pass
        # my_transfer()
    elif select == "3":
        pass
        # my_ask()
    elif select == "4":
        my_balance()
    elif select == "5":
        pass
        # my_histroy()
    elif select == "6":
        log_out()

# function check whether the supplied log in details are in the database.
def db_check():
    global user_id
    global phone
    query = "select User_id, Phone from users where Email = %s and Pin = %s"
    values = (login_email,login_pin)
    cursor.execute(query,values)
    result = cursor.fetchone()
    if result == None:
        print("Sorry, Your login details are invalid.\n")
        welcome()
    else:
        user_id = result[0]
        phone = result[1]
        user_dashboard()

# function is in charge of user's signing in.
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

# welcome is the starting point of this program.
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