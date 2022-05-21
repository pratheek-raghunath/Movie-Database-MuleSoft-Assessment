import sqlite3

# Create Entries to the database
def add():
    ch='yes'
    while(ch=='yes'):
        print("Enter the following details:")
        mov_name = input("Movie name:")
        act_name = input("Actor Name:")
        actress_name = input("Actress Name:")
        dir_name = input("Director Name:")
        year = input("Year of release:")
        cur = conn.cursor()
        cur.execute("INSERT INTO Movies (NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE) \
                            VALUES (?, ?, ?, ?,?)",(mov_name,act_name,actress_name,dir_name,year))
        conn.commit()
        cur.close()
        ch = input("Do you want to add more entries(yes/no):")
    print ("Records created successfully")
    conn.close()

    

# Printing all rows from the table
def select():
    cursor = conn.execute("SELECT MOV_ID, NAME, ACTOR, ACTRESS,DIRECTOR,YEAR_OF_RELEASE from Movies")
    for row in cursor:
        print ("ID = ", row[0])
        print ("NAME = ", row[1])
        print ("ACTOR = ", row[2])
        print ("ACTRESS = ", row[3])
        print ("DIRECTOR = ", row[4])
        print ("YEAR = ", row[5], "\n")

    print ("Printed successfully")
    conn.close()

# Querying based on actor name
def query(act_name):
    cursor = conn.execute("SELECT * from Movies where ACTOR=?",([act_name]))
    for row in cursor:
        print ("ID = ", row[0])
        print ("NAME = ", row[1])
        print ("ACTOR = ", row[2])
        print ("ACTRESS = ", row[3])
        print ("DIRECTOR = ", row[4])
        print ("YEAR = ", row[5], "\n")
    conn.close()
    

# Establishing Connection with database and handling the errors
try:
    conn = sqlite3.connect('movies_db.db')
    print("Database Opened Successfully")
except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)

# Menu driven operations
inp = input("MENU\n1.Create Table\n2.Add entries\n3.View all data\n4.Query with parameters\n")


if (inp == '1'):
    # Check if the table already exist
    cur = conn.cursor()
    cur.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='Movies' ''')
    if cur.fetchone()[0]==1 : {
        print('Table Already exists...')
    }
    else:
        # Table Creation
        conn.execute('''CREATE TABLE Movies
             (MOV_ID INTEGER PRIMARY KEY,
             NAME VARCHAR2(25),
             ACTOR VARCHAR2(25),
             ACTRESS VARCHAR2(25),
             DIRECTOR VARCHAR2(25),
             YEAR_OF_RELEASE NUMBER(4));''')
        print ("Table created successfully")

elif (inp == '2'):
    add()
elif (inp == '3'):
    select()
else:
    act_name = input("Enter the actor name whose movie has to be queried:")
    query(act_name)

print("The SQLite connection is closed")