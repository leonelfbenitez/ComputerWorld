# https://www.pythontutorial.net/python-basics/python-check-if-file-exists/

import sqlite3
import os.path

if not os.path.exists("data/database.db"):

# customer table
	conn = sqlite3.connect("data/database.db")
	cursor = conn.cursor()

	SQL_STATEMENT = """CREATE TABLE customer (
		cust_id INTEGER PRIMARY KEY AUTOINCREMENT,
		login VARCHAR(30),
		pass VARCHAR(30),
		fname VARCHAR(30),
		lname VARCHAR(30),
		email VARCHAR(50),
		phone VARCHAR(40),
		sign_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);"""

	cursor.execute(SQL_STATEMENT)

# service table 
	cursor = None
	conn = None
	
	conn = sqlite3.connect("data/database.db")
	cursor = conn.cursor()
	
	SQL_STATEMENT = """CREATE TABLE service (
		serv_id INTEGER PRIMARY KEY AUTOINCREMENT,
		dtype VARCHAR(20),
		dbrand VARCHAR(20),
		dmodel VARCHAR(20),
		dserial VARCHAR(20),
		idescript VARCHAR(255),
		repair BOOLEAN,
		data BOOLEAN,
		virus BOOLEAN,
		diagn BOOLEAN,
		software BOOLEAN,
		install BOOLEAN,
		serv_dt  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		cust_id INTEGER NOT NULL,
		FOREIGN KEY (cust_id) REFERENCES customer(cust_id)
	);"""

	cursor.execute(SQL_STATEMENT)

# shipping table
	cursor = None
	conn = None
	
	conn = sqlite3.connect("data/database.db")
	cursor = conn.cursor()

	SQL_STATEMENT = """CREATE TABLE shipping (
		ship_id INTEGER PRIMARY KEY AUTOINCREMENT,
		address TEXT,
		state CHAR(2),
		zip INTEGER,
		apt_num VARCHAR(30),
		in_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		cust_id INTEGER NOT NULL,
		FOREIGN KEY (cust_id) REFERENCES customer(cust_id)
	);"""

	cursor.execute(SQL_STATEMENT)

# recycle table
	cursor = None
	conn = None
	
	conn = sqlite3.connect("data/database.db")
	cursor = conn.cursor()

	SQL_STATEMENT = """CREATE TABLE recycle (
		recyc_id INTEGER PRIMARY KEY AUTOINCREMENT,
		recyc_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		cust_id INTEGER NOT NULL,
		FOREIGN KEY (cust_id) REFERENCES customer(cust_id)
	);"""

	cursor.execute(SQL_STATEMENT)

# inventory table

	cursor = None
	conn = None
	
	conn = sqlite3.connect("data/database.db")
	cursor = conn.cursor()

	SQL_STATEMENT = """CREATE TABLE inventory (
		item_id INTEGER PRIMARY KEY AUTOINCREMENT,
		item VARCHAR(50),
		url VARCHAR(100),
		price DECIMAL(10, 2),
		inventory INTEGER,
		in_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
	);"""

	cursor.execute(SQL_STATEMENT)

# cart table

	cursor = None
	conn = None
	
	conn = sqlite3.connect("data/database.db")
	cursor = conn.cursor()

	SQL_STATEMENT = """CREATE TABLE cart (
		cart_id INTEGER PRIMARY KEY AUTOINCREMENT,
		quantity INTEGER,
		cart_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		cust_id INTEGER NOT NULL,
		item_id INTEGER NOT NULL,
		serv_id INTEGER NOT NULL,
		recyc_id INTEGER NOT NULL,
		FOREIGN KEY (cust_id) REFERENCES customer(cust_id),
		FOREIGN KEY (item_id) REFERENCES inventory(item_id),
		FOREIGN KEY (serv_id) REFERENCES service(serv_id),
		FOREIGN KEY (recyc_id) REFERENCES recycle(recyc_id)
	);"""

	cursor.execute(SQL_STATEMENT)

# order/history table

	cursor = None
	conn = None
	
	conn = sqlite3.connect("data/database.db")
	cursor = conn.cursor()

	SQL_STATEMENT = """CREATE TABLE orders (
		or_id INTEGER PRIMARY KEY AUTOINCREMENT,
		total DECIMAL(10, 2),
		or_dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		cust_id INTEGER NOT NULL,
		ship_id INTEGER NOT NULL,
		FOREIGN KEY (cust_id) REFERENCES customer(cust_id),
		FOREIGN KEY (ship_id) REFERENCES shipping(ship_id)
	);"""
	
	cursor.execute(SQL_STATEMENT)

# item/history table

	cursor = None
	conn = None
	
	conn = sqlite3.connect("data/database.db")
	cursor = conn.cursor()

	SQL_STATEMENT = """CREATE TABLE item (
		it_id INTEGER PRIMARY KEY AUTOINCREMENT,
		quantity INTEGER,
		price DECIMAL(10, 2),
		dt TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
		or_id  INTEGER NOT NULL,
		item_id  INTEGER NOT NULL,
		FOREIGN KEY (or_id) REFERENCES orders(or_id),
		FOREIGN KEY (item_id) REFERENCES inventory(item_id)
	);"""

	cursor.execute(SQL_STATEMENT)

	# Remember to save + close
	conn.commit()
	conn.close()

else:
	conn = sqlite3.connect("data/database.db")
	conn.close()
