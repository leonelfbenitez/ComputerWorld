import sqlite3
from sqlite3 import Error
from flask import Flask, flash, redirect, request, url_for, render_template
import datetime
from app import conn

app = Flask(__name__)

# ************ insert data ********************************
# conn = sqlite3.connect("data/database.db")
# cursor = conn.cursor()

# data = [("Michael", "Fox", "test1@email.com", "2023-04-06"),
#         ("Adam", "Miller", "test2@email.com", "2023-04-01"),
#         ("Andrew", "Peck", "test3@email.com", "2023-04-02")]

# # Insert some users into our database
# cursor.executemany('INSERT INTO customers(fname, lname, email, join_dt) VALUES (?,?,?,?)', data)

# # Remember to save + close
# conn.commit()
# conn.close()

# **************** Fetch the data ************************ 
# conn = sqlite3.connect("data/database.db")
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM customers")

# result = cursor.fetchall()
# for i in result:
#     print(i)

# conn.close()

# @app.route('/service_form', methods=['POST'])
# def service_form():
#     try:
#         id = request.form['fname']
#         username = request.form['lname']
#         email = request.form['email']
#         phone = request.form['phone']
#         dtype = request.form['dtype']
#         dbrand = request.form['dbrand']
#         dmodel = request.form['dmodel']
#         dserial = request.form['dserial']
#         idescript = request.form['idescriptdserial']


#         #MySQL connection
#         # conn = sqlite3.connect("data/database.db")
#         # cur = conn.cursor()

#         if username and email and phone:
            
#             sql = "UPDATE user SET username = %s,email = %s,phone = %s WHERE id = %s;"
#             data = (username, email, phone, id)

#             cur.execute(sql, data)
#             conn.commit()

#             message = {
#                 'status': 200,
#                 'message': 'The user was modified successfully'
#             }
#             resp = jsonify(message)
#             resp.status_code = 200
        
#         else:
#             message = {
#                 'status': 510,
#                 'message': 'Some of the fields are empty'
#             }
#             resp = jsonify(message)
#             resp.status_code = 510

#         cur.close() #The finally block was removed and its content was placed here
#         conn.close()

#         return resp
    
#     except Exception as e: #(If there is an error, it will be returned in a JSON format)
#         message = {
#         'status': 500,
#         'message': 'Error: '+str(e)
#         }
#         resp = jsonify(message)
#         resp.status_code = 500
#         return resp


# @app.route("/")
# def index():
#     """Renders index page"""
    # if request.method == "POST":

    #     if request.form.get("login") == "login":
    #         return render_template("a_login.html")
    #     if request.form.get("myacct") == "myacct":
    #         return render_template("myacct.html")
    #     if request.form.get("cart") == "cart":
    #         return render_template("cart.html")
    # return render_template("service_form.html")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='4000', debug=True)
    