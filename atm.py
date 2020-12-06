# this line is be use to import mysql connector with an alias of con in other to link up this whole program to the data base.
import mysql.connector as con
# this line imports the date and time module to this program with an alias of dt.
import datetime as dt

# this lines links to the database.
db = con.connect(host="localhost",database="db_atm",username="root",password="")
cursor = db.cursor()

# this funtion generate time and date for transactions.
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

# this is the function in charge reduction in the user's account.
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

# this function update the database once the balance is not sufficient for the transaction. 
def money_nout(i):
    my_time()
    query = "select Balance, First_Name, Last_Name from users where User_id = %s"
    value = (user_id)
    cursor.execute(query,(value,))
    result = cursor.fetchone()
    balance_before = result[0]
    balance_after = result[0]
    query = "insert into transactions(User_id, Date, Time, Balance_Before, Balance_After, Remark, Status)values(%s,%s,%s,%s,%s,%s,%s)"
    values = (user_id,my_date,thyme,balance_before,balance_after,"withdrawal of #" + str(i),"Unsuccessful")
    cursor.execute(query,values)
    db.commit()
    print(str(result[1]) + " " + str(result[2]) + ", your transaction was unsuccessful due to insufficient fund.")

# this funtion promt the user to continue the transaction.
def proceed_transaction():
    print("\nDo you want to proceed with this transaction?\n1. Yes\n2. No")
    my_select()

# this check whether the user's balance is sufficient for the transaction.
def my_check(i):
    global amount
    global checkResult
    amount = i
    query = "select Balance from users where User_id = %s"
    value = (user_id)
    cursor.execute(query,(value,))
    result = cursor.fetchone()
    checkResult = result[0] >= i

# function is in charge of other withdraw option.
def my_other():
    global otherMoney
    query = "select First_Name from users where User_id = %s"
    value = (user_id)
    cursor.execute(query,(value,))
    result = cursor.fetchone()
    print(result[0] + ", Please input the amount you want to withdraw.")
    otherMoney = int(input("Right here: "))

# this function print out the options in withdraw.
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
            if select == "1":
                money_out(amount)
            elif select == "2":
                print("Your transaction terminated.")
                my_withdraw()
            else:
                print("Sorry, your selection is invalid.")
                user_dashboard()
            another_option()
            if select == "1":
                my_withdraw()
            elif select == "2":
                user_dashboard()
            else:
                return print("Sorry, Invalid selection.")
        else:
            money_nout(10000)
            print("Sorry, You do not have sufficient fund.")
    elif select == "2":
        my_check(5000)
        if checkResult == True:
            proceed_transaction()
            if select == "1":
                money_out(amount)
            elif select == "2":
                print("Your transaction terminated.")
                my_withdraw()
            else:
                print("Sorry, your selection is invalid.")
                user_dashboard()
            another_option()
            if select == "1":
                my_withdraw()
            elif select == "2":
                user_dashboard()
            else:
                return print("Sorry, Invalid selection.")
        else:
            money_nout(5000)
            print("Sorry, You do not have sufficient fund.")
    elif select == "3":
        my_check(2000)
        if checkResult == True:
            proceed_transaction()
            if select == "1":
                money_out(amount)
            elif select == "2":
                print("Your transaction terminated.")
                my_withdraw()
            else:
                print("Sorry, your selection is invalid.")
                user_dashboard()
            another_option()
            if select == "1":
                my_withdraw()
            elif select == "2":
                user_dashboard()
            else:
                return print("Sorry, Invalid selection.")
        else:
            money_nout(2000)
            print("Sorry, You do not have sufficient fund.")
    elif select == "4":
        my_check(1000)
        if checkResult == True:
            proceed_transaction()
            if select == "1":
                money_out(amount)
            elif select == "2":
                print("Your transaction terminated.")
                my_withdraw()
            else:
                print("Sorry, your selection is invalid.")
                user_dashboard()
            another_option()
            if select == "1":
                my_withdraw()
            elif select == "2":
                user_dashboard()
            else:
                return print("Sorry, Invalid selection.")
        else:
            money_nout(1000)
            print("Sorry, You do not have sufficient fund.")
    elif select == "5":
        my_check(500)
        if checkResult == True:
            proceed_transaction()
            if select == "1":
                money_out(amount)
            elif select == "2":
                print("Your transaction terminated.")
                my_withdraw()
            else:
                print("Sorry, your selection is invalid.")
                user_dashboard()
            another_option()
            if select == "1":
                my_withdraw()
            elif select == "2":
                user_dashboard()
            else:
                return print("Sorry, Invalid selection.")
        else:
            money_nout(500)
            print("Sorry, You do not have sufficient fund.")
    elif select == "6":
        my_other()
        my_check(otherMoney)
        if checkResult == True:
            proceed_transaction()
            if select == "1":
                money_out(amount)
            elif select == "2":
                print("Your transaction terminated.")
                my_withdraw()
            else:
                print("Sorry, your selection is invalid.")
                user_dashboard()
            another_option()
            if select == "1":
                my_withdraw()
            elif select == "2":
                user_dashboard()
            else:
                return print("Sorry, Invalid selection.")
        else:
            money_nout(amount)
            print("Sorry, You do not have sufficient fund.")
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

# this function is responsible for displaying of user transaction history.
def my_histroy():
    name = "select First_Name, Last_Name from users where User_id = %s"
    value = (user_id)
    cursor.execute(name,(value,))
    output = cursor.fetchone()
    query = "select users.User_id,users.First_Name,users.Last_Name,transactions.Tran_id,transactions.Date,transactions.Time,transactions.Balance_After,transactions.Remark,transactions.Status From transactions inner join users on transactions.User_id=users.User_id where users.User_id = %s"
    value = (user_id)
    cursor.execute(query,(value,))
    result = cursor.fetchall()
    if len(result) == 0:
        print(str(output[0]) + " " + str(output[1]) + ", you do not have any transaction histroy.")
    else:
        for details in result:
            print("\n" + "On " + str(details[4]) + " exactly " + str(details[5]) + ", you " + str(details[1]) + " " + str(details[2])  + str(details[-2]) + " which was " + str(details[-1]) + ".")
    print(" ")
    another_option()
    if select == "1":
        user_dashboard()
    else:
        return log_out()

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
        my_histroy()
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