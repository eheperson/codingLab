import sqlite3
from sqlite3 import Error
#
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def update_capacitor(conn, capacitor):
    """
        update capacitor count according to name
        conn: database connection
        capacitor : capacitor to be updated
        return: capacitor id
    """
    sql = """UPDATE capacitors SET count=? WHERE name=?;"""
    #
    cur = conn.cursor()
    cur.execute(sql, capacitor)
    conn.commit()
    print("Capacitor Updated ! ")

if __name__ == '__main__':
    #
    databaseName = r"D:\eheMachine\Workspace\codingLab\experimental\RestAPI\test\db\electronicComponents.db"
    dbConn = create_connection(databaseName)
    



# update a capacitor
    capacitor3New = (66, '22pF-63V');
    update_capacitor(dbConn, capacitor3New) 

#UPDATE capacitors SET count=66 WHERE name='22pF-63V'