import sqlite3

conn = sqlite3.connect('test.db')
conn.execute('''CREATE TABLE IF NOT EXISTS todo(
    id INTEGER PRIMARY KEY,
    task TEXT NOT NULL
);''')
#The above code creates a Table in database with name "todo", incase table of this name is already present in databse it won't create it again.
#ID will be use for fetching the data in cli.
#task holds the value entered by the user.
def show():
    query = "SELECT * FROM todo;"
    return conn.execute(query)
#Above function created, shows all the data entered till now as output. 


def insertdata(task):
    query = "INSERT INTO todo(task) VALUES(?);"
    conn.execute(query, (task,))
    conn.commit()
#This function inserts the data entered by the user in database.


def deletebyid(taskid):
    query = "DELETE FROM todo WHERE id =?;"
    conn.execute(query, (taskid,))
    conn.commit()
#This funcion is used for calling the data by ID as we know database we created has primary keys and delete it accordingly.
#We use "?" in the second line for the function, the purpose for this is we don't know what user will enter it is not definite, so for that we will take
#input from the user for which data to be deleted, the input part is taken care of in cli and this function is called in cli to delete the specific id.


def deletebytask(taskval):
    query = "DELETE FROM todo WHERE task =?;"
    conn.execute(query, (taskval,))
    conn.commit()
#This is the value of the id entered which will be deleted if selected.

def updatedata(taskid, newtask):
    query = "UPDATE todo SET task = ? WHERE id = ?;"
    conn.execute(query, (newtask, taskid))
    conn.commit()
#This fumction will update the data is added, basically it will add the new data entered by the user in our database.
