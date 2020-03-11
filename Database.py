import sqlite3

def create_item_table():
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Create table as per requirement
    sql_table = """CREATE TABLE IF NOT EXISTS INVENTORY_ITEM (
             ITEM_ID  CHAR(30) NOT NULL PRIMARY KEY, 
             DESCRIPTION  CHAR(50) NOT NULL,
             TYPE CHAR(20),
             QTY INT NOT NULL,  
             COST FLOAT NOT NULL)"""

    try:
        # Execute the SQL command
        cursor.execute(sql_table)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

def create_customer_table():
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Create table as per requirement
    sql_table = """CREATE TABLE IF NOT EXISTS CUSTOMER (CUSTOMER_ID CHAR(30) NOT NULL PRIMARY KEY,
                CUSTOMER_NAME CHAR(30) NOT NULL,
                CUSTOMER_ADD CHAR(50))"""

    try:
        # Execute the SQL command
        cursor.execute(sql_table)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def add_customer(id, name, address):
    db = sqlite3.connect("Inventory_System.db")

    cursor = db.cursor()

    # Prepare SQL query to INSERT a record into the database.
    sql = "INSERT INTO CUSTOMER(CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_ADD) " \
          "VALUES ('%s', '%s', '%s')" % (id, name, address)

    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def add_item(id, name, type, qty, cost):
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    retrieve = "SELECT DISTINCT ITEM_ID, QTY FROM INVENTORY_ITEM"
    cursor.execute(retrieve)
    item = cursor.fetchall()

    if id in item:
        update_quantity = data[3] + qty
        print(update_quantity)
        oql = "UPDATE INVENTORY_ITEM" \
                  "SET QTY = '%d'" \
                  "WHERE ITEM_ID = '%s'" % (update_quantity, id)
        try:
            # Execute the SQL command
            cursor.execute(oql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

    else:
        print("Not Found")
        sql = "INSERT INTO INVENTORY_ITEM(ITEM_ID, DESCRIPTION, TYPE, QTY, COST)" \
              "VALUES ('%s', '%s', '%s', '%d', '%f')" % (id, name, type, qty, cost)
        try:
            # Execute the SQL command
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()

    # disconnect from server
    db.close()

def get_item_list():
    # Open database connection
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    #sql = "SELECT DISTINCT ITEM_ID, DESCRIPTION, TYPE, QTY FROM INVENTORY_ITEM"
    sql = "SELECT * FROM INVENTORY_ITEM"
    cursor.execute(sql)
    get = cursor.fetchall()
    # disconnect from server
    db.close()
    return get

print(get_item_list())

def get_customer_list():
    # Open database connection
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT DISTINCT CUSTOMER_ID, CUSTOMER_NAME, CUSTOMER_ADD FROM CUSTOMER"
    cursor.execute(sql)
    get = cursor.fetchall()
    # disconnect from server
    db.close()
    return get


def item_count(item_name):
    # Open database connection
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT COUNT(DESCRIPTION)" \
          "FROM INVENTORY_ITEM" \
          "WHERE DESCRIPTION = '%s'" % (item_name)

    cursor.execute(sql)
    get = cursor.fetchall()
    db.close()
    return get




def get_available_items():
    # Open database connection
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "SELECT DISTINCT DESCRIPTION  FROM INVENTORY_ITEM WHERE QTY > 0"
    cursor.execute(sql)
    get = cursor.fetchall()
    # disconnect from server
    db.close()
    return get


def delete_item(item_id):
    # Open database connection
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM INVENTORY_ITEM WHERE ITEM_ID = '%s'" % item_id
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def add_costumer_order(costumer, qty_order, item_description):
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "UPDATE INVENTORY SET COSTUMER = '%s'," \
          "COSTUMER_ORDER = '%s', ORDER_QTY = '%d' " \
          "WHERE DESCRIPTION = '%s'" % (costumer, item_description, qty_order, item_description)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


def delete_customer(customer_id):
    # Open database connection
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM CUSTOMER WHERE CUSTOMER_ID = '%s'" % customer_id
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

def empty():
    # Open database connection
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # Prepare SQL query to DELETE required records
    sql = "DELETE FROM INVENTORY"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

def update_qty(qty, description):
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()


    sql = "UPDATE INVENTORY SET QTY = '%d' WHERE DESCRIPTION = '%s'" % (qty, description)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()

def update_costumer_order_qty(qty, costumer_name):
    db = sqlite3.connect("Inventory_System.db")

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    sql = "UPDATE INVENTORY SET ORDER_QTY = '%d' WHERE COSTUMER = '%s'" % (qty, costumer_name)
    try:
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()

    # disconnect from server
    db.close()


