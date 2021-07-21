import sqlite3
from sqlite3 import Error
#
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    dbPath = ".\\db\\" + db_file + ".db"
    global DATABASE_PATH
    try:
        conn = sqlite3.connect(dbPath)
        #print(sqlite3.version)
    except Error as e:
        print(e)

    return conn
#
## Resistors Table
resistorsTableStr = """CREATE TABLE IF NOT EXISTS resistors (
                        id integer PRIMARY KEY UNIQUE NOT NULL,
                        name text NOT NULL UNIQUE,
                        count integer NOT NULL
                    );"""
#
## Capacitors Table
capacitorsTableStr = """CREATE TABLE IF NOT EXISTS capacitors (
                        id integer PRIMARY KEY UNIQUE NOT NULL,
                        name text NOT NULL UNIQUE,
                        count integer NOT NULL
                    );"""
#
def create_table(conn, create_table_str):
    """ create a table from the create_table_str statement
        conn:               Connection object
        create_table_str:   CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(create_table_str)
    except Error as e:
        print(e)
#
#
def insert_resistor(conn, resistor):
    """ 
        insert new resistor into the resistor data table
        conn : database connection
        resistor : new resistor exp: resistor = ('20kR-1/4W', 20)
        return : resistor ID
    """
    sql = ''' INSERT INTO resistors(name, count) VALUES(?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql, resistor)
        conn.commit()
    except Error as e:
        print("WARNING ! : ", e)
    
#
def insert_capacitor(conn, capacitor):
    """ 
        insert new capacitor into the capacitor data table
        conn : database connection
        capacitor : new capacitor exp: capacitor = ('10uF-20V', 10)
        return : capacitor ID
    """
    sql = ''' INSERT INTO capacitors(name, count) VALUES(?,?) '''
    cur = conn.cursor()
    try:
        cur.execute(sql, capacitor)
        conn.commit()
    except Error as e:
        print("WARNING ! : ", e)
#
def update_resistor(conn, resistor):
    """
        update resistor count according to name
        conn: database connection
        resistor : resistor to be updated
        return: resistor id
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        The sql_values array needs to be in the same order as the @variables in the statement.
        For Example : 
            if   : sql = '''UPDATE reistors SET count = ? WHERE name = ?'''
            then : resistor = (49, '20kR-1/4W')
            not  : resistor = ('20kR-1/4W', 49)
    """
    sql = ''' UPDATE resistors SET count = ? WHERE name = ?;'''
    #
    cur = conn.cursor()
    cur.execute(sql, resistor)
    conn.commit()
#
def update_capacitor(conn, capacitor):
    """
        update capacitor count according to name
        conn: database connection
        capacitor : capacitor to be updated
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        The sql_values array needs to be in the same order as the @variables in the statement.
        For Example : 
            if   : sql = '''UPDATE capacitors SET count = ? WHERE name = ?'''
            then : capacitor = (66, '22pF-63V')
            not  : capacitor = ('22pF-63V', 66)
    """
    sql = """UPDATE capacitors SET count = ? WHERE name = ?"""
    #
    cur = conn.cursor()
    cur.execute(sql, capacitor)
    conn.commit()
    print("Capacitor Updated ! ")
#
def select_all_resistors(conn):
    """
        Query all rows in the tasks table
        conn: the Connection object
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM resistors")

    rows = cur.fetchall()

    print()
    print("Resistors : ")
    for row in rows:
        print(row)
#
def select_all_capacitors(conn):
    """
        Query all rows in the tasks table
        conn: the Connection object
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM capacitors")

    rows = cur.fetchall()

    print()
    print("Capacitors : ")
    for row in rows:
        print(row)
#
def select_resistor_by_name(conn, name):
    """
    Query tasks by priority
    conn : the Connection object
    name : name of the resistor to select
    return : nothing
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM resistors WHERE name=?", (name,))

    rows = cur.fetchall()

    print()
    print("Resistor by name : ")
    for row in rows:
        print(row)
#
def select_capacitor_by_name(conn, name):
    """
    Query tasks by priority
    conn : the Connection object
    name : name of the capacitor to select
    return : nothing
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM capacitors WHERE name=?", (name,))

    rows = cur.fetchall()

    print()
    print("Capacitorr by name : ")
    for row in rows:
        print(row)
#
def delete_resistor_by_name(conn, name):
    """
    Delete a task by task id
    conn :  Connection to the SQLite database
    name : name of the resistor
    return : nothing
    """
    sql = 'DELETE FROM resistors WHERE name=?'
    cur = conn.cursor()
    cur.execute(sql, (name,))
    conn.commit()
    print()
    print(name, " deleted.")
#
def delete_all_resistors(conn):
    """
    Delete all rows in the tasks table
    conn : Connection to the SQLite database
    return : nothing
    """
    sql = 'DELETE FROM resistors'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print()
    print("All resistors are deleted.")
#
#
if __name__ == '__main__':
    #
    databaseName = "electronicComponents"
    dbConn = create_connection(databaseName)
    
    if dbConn is not None:
        # create resistors table
        create_table(dbConn, resistorsTableStr)
        #create capacitors table
        create_table(dbConn, capacitorsTableStr)
    else:
        print("Error! cannot create the database connection.")

    with dbConn:
        # create a new resistor
        resistor1 = ('10kR-1/4W', 50);
        insert_resistor(dbConn, resistor1)
        # create a new resistor
        resistor2 = ('20kR-1/4W', 40);
        insert_resistor(dbConn, resistor2)
        # create a new resistor
        resistor3 = ('30kR-1/4W', 60);
        insert_resistor(dbConn, resistor3)
        #
        # create a new capacitor
        capacitor1 = ('1uF-16V', 50);
        insert_capacitor(dbConn, capacitor1)
        # create a new capacitor
        capacitor2 = ('100uF-35V', 40);
        insert_capacitor(dbConn, capacitor2)
        # create a new capacitor
        capacitor3 = ('22pF-63V', 600);
        insert_capacitor(dbConn, capacitor3) 
        #
        dbConn.commit()
        # update a capacitor
        capacitor3New = (61, '22pF-63V');
        update_capacitor(dbConn, capacitor3New) 
        dbConn.commit()
        # create a new capacitor
        capacitor4 = ('22pF-100V', 30);
        insert_capacitor(dbConn, capacitor4) 
        #
        # select all resistors
        select_all_resistors(dbConn)
        # select all capacitors
        select_all_capacitors(dbConn)
        #
        #
        select_resistor_by_name(dbConn, '30kR-1/4W')
        select_capacitor_by_name(dbConn, '22pF-100V')
        #
        #
        delete_resistor_by_name(dbConn, '30kR-1/4W')
        select_all_resistors(dbConn)
        #
        #
        delete_all_resistors(dbConn)
        select_all_resistors(dbConn)
