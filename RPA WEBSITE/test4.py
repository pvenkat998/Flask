from flask_mysqldb import MySQL
from flask import Flask,render_template,url_for,request,redirect,session,flash,abort
import os

app=Flask(__name__)
app.config['MYSQL_HOST']='192.168.5.124'
app.config['MYSQL_USER']='eigyou_kikaku'
app.config['MYSQL_PASSWORD']='As6hV2K!k'
app.config['MYSQL_DB']='eigyou_kikaku'
mysql = MySQL(app)
##HOME PAGE
@app.route('/')
def index():
    return render_template('index.html')
##LOGIN PAGE
@app.route('/login/',methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

##LOGIN CREDENTIAL CHECK
@app.route("/check/", methods=['GET', 'POST'])
def check():
  error = None
  if request.method == 'POST':
    username = str(request.form["username"])
    password = str(request.form["password"])
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT user_id FROM _live_company__syain WHERE user_id ='" + username + "' AND user_id='" + password + "' "  )
    user = cursor.fetchone()

    if len(user) is 1:
        return redirect(url_for("home"))
    else:
        error = 'Invalid Credentials. Please try again.'
  return render_template('login.html', error=error)
## HOME PAGE WHERE YOU CAN SEE THE DETAILS OF EACH EMPLOYEE
@app.route("/home/")
def home():
    cur=mysql.connection.cursor()
    cur.execute('''SELECT `month`,BANGO,`name`,point,siemple_crosssell.ka
FROM siemple_crosssell
LEFT JOIN _live_company__syain ON siemple_crosssell.`name`=CONCAT(sei,mei)
WHERE _live_company__syain.user_id="'''+username+'''"''')
    data = cur.fetchall()
    return render_template('home.html', data=data)


@app.route("/profile/")
def profile():
    cur=mysql.connection.cursor()
    cur.execute('''SELECT * FROM test''')
    rv=cur.fetchall()
    return str(rv)
@app.route("/getall/")
def getall():
    cur=mysql.connection.cursor()
    cur.execute('''SELECT * FROM test''')
    data = cur.fetchall()
    return render_template('db.html', data=data)
@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()
if __name__ == "__main__":
        app.secret_key = os.urandom(12)
        app.run(debug=True)