from flask import Flask, render_template, request, url_for, redirect 
from flaskext.mysql import MySQL 

app = Flask(__name__) 
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'MyDB' 
mysql = MySQL(app) 
@app.route('/', methods=['GET', 'POST']) 

def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

@newApp.route("/users")
def users():
	cur = mysql.connection.cursor()
	results = cur.execute("SELECT * FROM users")
	if results > 0:
		userDetails = cur.fetchall()
		
    
	return render_template('users.html', userDetails=userDetails)



if __name__ == '__main__':
    app.run()