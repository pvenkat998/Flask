from flask_mysqldb import MySQL
import random
from flask import Flask,render_template,url_for,request,redirect,session,flash,abort
import os
from forms import Robotform,MusicSearchForm, AlbumForm
from flask import flash, render_template, request, redirect
import uuid
global str
str = str(id)

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

## HOME PAGE WHERE YOU CAN SEE THE DETAILS OF EACH EMPLOYEE
@app.route("/home/")
def home():
    cur=mysql.connection.cursor()
    cur.execute('''SELECT ロボット名,依頼者,部署,作成者,日,備考
FROM robotkanri''')
    data = cur.fetchall()
    return render_template('home.html', data=data)


@app.route('/home/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.connection.cursor()
    query_string="""SELECT ロボット名,依頼者,部署,作成者,日,備考
    FROM robotkanri WHERE ロボット名='{id}' LIMIT 1""".format(id=id)
    cur.execute(query_string)
    robot = cur.fetchall()

    if robot:
        form = Robotform(formdata=request.form, obj=robot)

        if request.method == 'POST' and form.validate():
            # save edits

            edit_changes(id, form)

            flash('Robot updated successfully!')
            return redirect('/home')
        return render_template('edit_robot.html', form=form)
    else:
        return 'Error loading #{id}'.format(id=id)
def edit_changes(id,form, new=True):


    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    cur = mysql.connection.cursor()
    robotname = form.robotname.data
    iraisha = form.iraisha.data
    busho=form.busho.data
    developer = form.developer.data
    last_mod = form.last_mod.data
    remark = form.remark.data

    if new:
        # Add the new album to the database
        cur.execute("""DELETE
    FROM robotkanri WHERE ロボット名='{id}'""".format(id=id))
        cur.execute(
            """
    INSERT INTO robotkanri(ID,ロボット名,依頼者,部署,作成者,日,備考)
            VALUES (%s,%s,%s,%s,%s,%s,%s)""",
            (uuid.uuid4(),robotname, iraisha, busho, developer ,last_mod, remark))
        mysql.connection.commit()
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
#adding files
@app.route('/new_robot', methods=['GET', 'POST'])
def new_robot():
    """
    Add a new album
    """
    form = Robotform(request.form)
    if request.method == 'POST' and form.validate():
        # save the album
        robot =Robotform()
        save_changes(robot, form, new=True)
        flash('ロボットが追加されました!')
        return redirect('/home')

    return render_template('newrobot.html', form=form)


def save_changes(robot, form, new=False):


    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    cur = mysql.connection.cursor()
    robotname = form.robotname.data
    iraisha = form.iraisha.data
    busho=form.busho.data
    developer = form.developer.data
    last_mod = form.last_mod.data
    remark = form.remark.data

    if new:
        # Add the new album to the database
        cur.execute(
            """INSERT INTO 
                robotkanri(ID,ロボット名,依頼者,部署,作成者,日,備考)
            VALUES (%s,%s,%s,%s,%s,%s,%s)""",
            (uuid.uuid4(),robotname, iraisha, busho, developer ,last_mod, remark))
        mysql.connection.commit()
if __name__ == "__main__":
        app.secret_key = os.urandom(12)
        app.run(debug=True)