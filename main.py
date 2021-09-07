# Author: Lane Nash
#
# Description: create a database that allows user to create tables,
# entries as well as find them and update.
# 2 rows one for username and one for notes. (Using SQLite3 Library)
#
# libraries
import sqlite3

#

#
con = sqlite3.connect('abc.db')
c = con.cursor()


#
#
def remove(column, value1):
    """This function allows the user to delete a row from within a DB"""
    with con:  # with context manager
        # delete row where column specified contains this value
        con.execute(f'DELETE FROM test WHERE {column}="{value1}"')


def create():  # Create Function
    """This function creates a singular SQL Table with 2 columns; Username & Notes."""
    with con:  # with context manager
        con.execute(f"CREATE TABLE IF NOT EXISTS test (Username, Notes);")  # creating table


# insert entry function
def insert(value1, value2):
    """This function allows user to input into the existing table
    Example:
    value 1 = David
    Value 2 = testing.
    There would be a row in the Database that contains Username of David
    with one other column for notes that contains Testing"""
    # with context manager
    with con:
        # execute sql statement to insert entries
        con.execute(f'INSERT INTO test VALUES("{value1}","{value2}");')
    return {"username added": value1, "note added": value2}


# find table in database function
def find_table():
    """This function will fetch our table from the hardcoded DB
    and print its entire contents."""
    # with context manager
    with con:
        # execute SQL syntax to show table contents
        c.execute(f"SELECT * FROM test")
        # display table contents
        print(c.fetchall())


# update entry within database
def update(col, old, new):
    """This function allows the user to update an existing entry within the table
    Example:
        Col = Username
        OldEntry = test
        NewEntry = Testing123
        The updated entry for where the old entry is will be Testing123"""
    # with context manager
    with con:
        con.execute(f'UPDATE test SET {col}="{new}" WHERE {col}="{old}";')


# this is the main code
def main():
    """This is a basic menu which provides the user with a choice that spans from 1 to 5.
            If the users input is not an integer it will throw a value error code"""
    # try this
    try:
        print('Database Connection Successful')
        # users choice selection
        choice = int(input("1. Create Table: \n2. Insert Value: \n3. Display Contents: \n4. Update Entry: \n5. "
                           "Disconnect: \nEnter your selection: "))
        # if user choice is 1 go to create function
        if choice == 1:
            create()
        # if user choice is 2 go to find table function
        elif choice == 2:
            username = str(input("Enter First Value: "))
            password = str(input("Enter Second Value: "))
            insert(username, password)
        # if choice is 3 go to find table
        elif choice == 3:
            find_table()
        # if choice is 4 go to update table
        elif choice == 4:
            column = input("Which Column: ")
            old_entry = input("Enter Old Value: ")
            new_entry = input("Enter New Value: ")
            update(column, old_entry, new_entry)
        # if user choice is 5 disconnect from DB
        elif choice == 5:
            con.close()
            print("Database Disconnected")
            exit()
        elif choice == 6:
            col = input("Column")
            entry = input("Where")
            remove(col, entry)
        # if that did not work do this
    except ValueError:
        print("Got an Exception: Enter Integer Only")


main()
