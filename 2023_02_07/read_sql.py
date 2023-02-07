import sqlite3

def select_all_from_table(conn,table):
    """
    Query all rows in the properties table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM " + table + "_table")

    rows = cur.fetchall()

    for row in rows:
        print(row)

con = sqlite3.connect('2023_02_07\\data.db')

with con:
    select_all_from_table(con,"material")
    select_all_from_table(con,"properties")
