import mysql.connector as mysql

db= mysql.connect(host="localhost", user="root", password="",database="college")
command_handler = db.cursor(buffered=True)

def admin_session():
    while 1: 
        print("")
        print("Admin Menu")
        print("1. Register New Student")
        print("2. Register New Teacher")
        print("3. Delete existing student")
        print("4. Delete existing teacher")
        print("5. Logout")  

        user_option = input(str("Option:"))
        if user_option=="1":
            print("")
            print("Register New Student")
            username = input(str("Student username:"))
            password = input(str("Student password:"))
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users (User_Name, password, Account_Type) VALUES (%s,%s,'student')", query_vals)
            db.commit()
            print(username + " has been registered as a student." )
        
        elif user_option=='2':
            print("")
            print("Register New Teacher")
            username = input(str("Teacher username:"))
            password = input(str("Teacher password:"))
            query_vals = (username, password)
            command_handler.execute("INSERT INTO users (User_Name, password, Account_Type) VALUES (%s,%s,'teahcer')", query_vals)
            db.commit()
            print(username + " has been registered as a teacher." )

        elif user_option=='3':
            print("")
            print("Delete Existing Student Account")
            username=input(str("Student username: "))
            query_vals=(username,"student")
            command_handler.execute("DELETE FROM users Where User_Name=%s AND Account_Type=%s", query_vals)
            db.commit
            if command_handler.rowcount<1:
                print("User not found")
            else:
                print(username+" has been deleted")
        
        elif user_option=='4':
            print("")
            print("Delete Existing Student Account")
            username=input(str("Teahcer username: "))
            query_vals=(username,"teacher")
            command_handler.execute("DELETE FROM users Where User_Name=%s AND Account_Type=%s", query_vals)
            db.commit
            if command_handler.rowcount<1:
                print("User not found")
            else:
                print(username+" has been deleted")
        
        elif user_option=='5':
            break
        else:
            print("No valid command")

def auth_admin():
    print("")
    print("Admin Login")
    print("")
    username = input(str("Username:"))
    password = input(str("Password:"))
    if username == "admin":
        if password=="password":
            admin_session()
        else: 
            print("Incorrect Password")
    else: 
        print("Login details are not recognized")

def main():
    while 1:
        print("Welcome to the college system")
        print("")
        print("1. Login as student")
        print("2. Login as teacher")
        print("3. Login as admin")

        user_option = input(str("Option:"))
        if user_option=="1":
            print("Student login")
        elif user_option=="2":
            print("Teacher login")
        elif user_option=="3":
            auth_admin()
        else:
            print("No valid option was selected")
         
main()