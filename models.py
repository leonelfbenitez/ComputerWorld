# https://www.sqlitetutorial.net/sqlite-create-table/
# https://www.sqlite.org/foreignkeys.html

"""SQlite models"""
import sqlite3

conn = sqlite3.connect("data/database.db")
c = conn.cursor()

# Create the table, read the article below if you
# are unsure of what they mean
# https://www.w3schools.com/sql/sql_datatypes.asp
SQL_STATEMENT = """CREATE TABLE Customer (
	cust_id INTEGER PRIMARY KEY,
	fname VARCHAR(20),
	lname VARCHAR(30),
	email VARCHAR(50),
	join_dt DATE
);"""

SQL_STATEMENT = """CREATE TABLE Service_Order (
	order_id INTEGER PRIMARY KEY,
	dev_type VARCHAR(40),
	brand VARCHAR(30),
	model VARCHAR(30),
    serial_num VARCHAR(50),
    issue VARCHAR(255),
    cust_id INTEGER,
    FOREIGN KEY (cust_id) REFERENCES Customer(cust_id)
        ON DELETE CASCADE 
        ON UPDATE NO ACTION
);"""

SQL_STATEMENT = """CREATE TABLE Service (
	serv_id INTEGER PRIMARY KEY,
	service VARCHAR(40),
    hours VARCHAR(40),
    order_id INTEGER,
    FOREIGN KEY (order_id) REFERENCES Service_Order(order_id)
        ON DELETE CASCADE 
        ON UPDATE NO ACTION
);"""