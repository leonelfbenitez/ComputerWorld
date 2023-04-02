import sqlite3
from flask import Flask, flash, redirect, request, url_for, render_template
import datetime
from flask_login import (
    current_user,
    LoginManager,
    login_required,
    login_user,
    logout_user,
)

app = Flask(__name__)

conn = sqlite3.connect("data/database.db")
c = conn.cursor()

# Create the table, read the article below if you
# are unsure of what they mean
# https://www.w3schools.com/sql/sql_datatypes.asp
# SQL_STATEMENT = """CREATE TABLE emp (
# 	staff_number INTEGER PRIMARY KEY,
# 	fname VARCHAR(20),
# 	lname VARCHAR(30),
# 	gender CHAR(1),
# 	joining DATE
# );"""

# c.execute(SQL_STATEMENT)

# Insert some users into our database
# c.execute("""INSERT INTO emp VALUES (23, "Rishabh", "Bansal", "M", "2014-03-28");""")
# c.execute("""INSERT INTO emp VALUES (1, "Bill", "Gates", "M", "1980-10-28");""")

# Fetch the data 
# c.execute("SELECT fname FROM emp")

# Store + print the fetched data
# result = c.fetchall()
# for i in result:
#     print(i)

""" Printed:
(1, 'Bill', 'Gates', 'M', '1980-10-28')
(23, 'Rishabh', 'Bansal', 'M', '2014-03-28')
"""

# Remember to save + close
# conn.commit()
# conn.close()

@app.route("/", methods=["GET", "POST"])
def index():
    """Renders index page"""
    if request.method == "POST":

        if request.form.get("login") == "login":
            return render_template("a_login.html")
        if request.form.get("myacct") == "myacct":
            return render_template("myacct.html")
        if request.form.get("cart") == "cart":
            return render_template("cart.html")
    return render_template("service_home.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3000', debug=True)
    