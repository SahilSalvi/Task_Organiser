from sqlite3.dbapi2 import DatabaseError
import tmDB
import os

os.system("cls")

data = int(input("Choose What You Want ?\n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4. QUIT\n\t>"))

while data != 4:
#Until and unless the entered value is not 4 it will display the below options and once it is equal it will go to the last else condtion. 
    if(data == 1):
        os.system("cls")
        print("ID" + "\t" + "TASK\n\n")
        for rows in tmDB.show():
            print(str(rows[0]) + "\t" + rows[1])
        data = int(input("Choose What You Want ?\n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4. QUIT\n\t>"))
#If entered value is 1 which is "View task" will display all the entered task and here we are calling the funtion show() from Database for fetching the entered data.
  
    
    elif(data == 2):
        task = input("Enter A Task : ")
        if(len(task) != 0):
            tmDB.insertdata(task)
        data = int(input("Choose What You Want ?\n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4. QUIT\n\t>"))
#If entered value is 2 the user will be able to able to enter data which will be stored in database through "insert data "  
 
    
    elif(data == 3):
        os.system("cls")
        print("ID" + "\t" + "TASK\n\n")
        for rows in tmDB.show():
            print(str(rows[0]) + "\t" + rows[1])
        id = int(input("Choose A Task ID To Delete : "))
        tmDB.deletebyid(id)
        data = int(input("Choose What You Want ?\n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4. QUIT\n\t>"))
#The conditione will delete the data as per their ID     
    
    else:
        print("Choose A Correct Option")
        data = int(input("Choose What You Want ?\n\t1. View Task\n\t2. Add A Task\n\t3. Delete A Task\n\t4. QUIT\n\t>"))
#If the user enters an incorrect option this, user will be again displayed with the option to choose from.
else:
    print("Thank You for using the Application!")
