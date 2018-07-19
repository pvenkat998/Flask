from flask_mysqldb import MySQL
import random
from flask import Flask,render_template,url_for,request,redirect,session,flash,abort
import os
from forms import Robotform,MusicSearchForm, AlbumForm
from flask import flash, render_template, redirect,request
from datetime import date
global str



app=Flask(__name__)
app.config['MYSQL_HOST']='192.168.5.124'
app.config['MYSQL_USER']='eigyou_kikaku'
app.config['MYSQL_PASSWORD']='As6hV2K!k'
app.config['MYSQL_DB']='eigyou_kikaku'
mysql = MySQL(app)
## HOME PAGE WHERE YOU CAN SEE THE DETAILS OF EACH EMPLOYEE
@app.route("/home/")
def home():
#TAB1
    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="SK"''')
    data1 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
    FROM robotkanri WHERE 部署="顧問"''')
    data2 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
    FROM robotkanri WHERE 部署="レイサス"''')
    data3 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="mode"''')
    data4 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="SC"''')
    data5 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="システム課"''')
    data6 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="業推全体"''')
    data7 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="PDM"''')
    data8 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="経理"''')
    data9 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="グレコミ"''')
    data10 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="ロンザン"''')
    data11 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="レイサスプロモ"''')
    data12 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="社長名鑑"''')
    data13 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="ダウンロード"''')
    data14 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
FROM robotkanri WHERE 部署="その他"''')
    data15 = cur.fetchall()
#TAB 2
    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
    FROM robotkanri WHERE 作成者="松本" AND 完成="完成"''')
    k1 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
        FROM robotkanri WHERE 作成者="井上" AND 完成="完成"''')
    k2 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
    FROM robotkanri WHERE 作成者="李そ" AND 完成="完成"''')
    k3 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
    FROM robotkanri WHERE 作成者="廣瀬" AND 完成="完成"''')
    k4= cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
        FROM robotkanri WHERE 作成者="ピチュカ" AND 完成="完成"''')
    k5 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
        FROM robotkanri WHERE 作成者="澤山" AND 完成="完成"''')
    k6 = cur.fetchall()
#TAB 3
    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
    FROM robotkanri WHERE 作成者="松本" AND 完成="未完成"''')
    m1 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
        FROM robotkanri WHERE 作成者="井上" AND 完成="未完成"''')
    m2 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
    FROM robotkanri WHERE 作成者="李そ" AND 完成="未完成"''')
    m3 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
    FROM robotkanri WHERE 作成者="廣瀬" AND 完成="未完成"''')
    m4= cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
        FROM robotkanri WHERE 作成者="ピチュカ" AND 完成="未完成"''')
    m5 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,備考,完成,削減時間
        FROM robotkanri WHERE 作成者="澤山" AND 完成="未完成"''')
    m6 = cur.fetchall()

    return render_template('home.html', data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,dat6=data6,data7=data7,data8=data8,data9=data9,data10=data10,data11=data11,data12=data12,data13=data13,data14=data14,data15=data15,k1=k1,k2=k2,k3=k3,k4=k4,k5=k5,k6=k6,m1=m1,m2=m2,m3=m3,m4=m4,m5=m5,m6=m6)

#edit page!
@app.route('/home/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.connection.cursor()
    query_string = ("""SELECT ロボット名,依頼者,部署,作成者,日,備考,ログ,目的,概要,完成,削減時間,削減時間ノート
        FROM robotkanri WHERE ID='{id}' LIMIT 1""".format(id=id))
    cur.execute(query_string)
    data = cur.fetchall()
    if data:

        lst = list(data[0])
        lograw=lst[6]
        log=lst[6]
        log =log.split('@!')
        form = Robotform(formdata=request.form,robotname=lst[0],iraisha=lst[1],busho=lst[2],developer=lst[3], last_mod=lst[4],remark=lst[5],obje=lst[7],gaiyo=lst[8],kansei=lst[9],sakujikan=lst[10],sakujikannote=lst[11])
        if request.method == 'POST' and form.validate():
            edit_changes(id, form,lograw)
            flash('Robot updated successfully!')
            return redirect('/home')
        return render_template('edit_robot.html', form=form,data=data,log=log)
    else:
        return 'Error loading #{id}'.format(id=id)

#edit(func)
def edit_changes(id,form,lograw, new=True):


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
    obje=form.obje.data
    gaiyo=form.gaiyo.data
    logn=form.log.data
    sakuji=form.sakujikan.data
    sakujin=form.sakujikannote.data
    today = str(date.today())
    logs=str(lograw)
    kansei=form.kansei.data
    if logn=="":
       logr=logs
    else:
       logr="".join((logs,'@!',today," ", logn))

    if new:
        # Add the new album to the database
        cur.execute("""DELETE
    FROM robotkanri WHERE ID='{id}'""".format(id=id))
        cur.execute(
            """
    INSERT INTO robotkanri (ID,ロボット名,依頼者,部署,作成者,日,備考,ログ,目的,概要,完成,削減時間,削減時間ノート)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (id,robotname, iraisha, busho, developer ,last_mod, remark,logr,obje,gaiyo,kansei,sakuji,sakujin))
        mysql.connection.commit()

#adding new robot (the page)
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

    return render_template('new_robot.html', form=form)

#adding new robot(funct)
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
    kansei=form.kansei.data
    sakuji=form.sakujikan.data
    logr=""
    if new:
        # Add the new album to the database
        cur.execute(
            """INSERT INTO 
                robotkanri(ロボット名,依頼者,部署,作成者,日,備考,ログ,完成,削減時間)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (robotname, iraisha, busho, developer ,last_mod, remark,logr,kansei,sakuji))
        mysql.connection.commit()
if __name__ == "__main__":
        app.secret_key = os.urandom(12)
        app.run(debug=True)