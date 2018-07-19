from operator import is_not
from functools import partial
import requests
from flask_mysqldb import MySQL
import random
from flask import Flask,render_template,url_for,request,redirect,session,flash,abort
import os
from forms import Robotform,MusicSearchForm, AlbumForm
from flask import flash, render_template, redirect,request
from flask import request
from datetime import date
global str
from django.template.defaulttags import register
...
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

import uuid

app=Flask(__name__)
app.config['MYSQL_HOST']='192.168.5.124'
app.config['MYSQL_USER']='eigyou_kikaku'
app.config['MYSQL_PASSWORD']='As6hV2K!k'
app.config['MYSQL_DB']='eigyou_kikaku'
mysql = MySQL(app)
##HOME PAGE
# row and column majors for defining source stuffff

def html_table(lol):
  yield '<table>'
  for sublist in lol:
    yield '  <tr><td>'
    yield '    </td><td>'.join(sublist)
    yield '  </td></tr>'
  yield '</table>'
def col_major(alist, sublen):
  numrows = (len(alist)+sublen-1) // sublen
  return [alist[i::sublen] for i in range(numrows)]
def list_to_html_table(alist, sublength, column_major=True):
  lol = col_major(alist, sublength)

  return '\n'.join(html_table(lol))

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
#TAB1
    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="SK"''')
    data1 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
    FROM robotkanri WHERE 部署="顧問"''')
    data2 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
    FROM robotkanri WHERE 部署="レイサス"''')
    data3 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="mode"''')
    data4 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="SC"''')
    data5 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="システム課"''')
    data6 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="業推全体"''')
    data7 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="PDM"''')
    data8 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="経理"''')
    data9 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="グレコミ"''')
    data10 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="ロンザン"''')
    data11 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="レイサスプロモ"''')
    data12 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="社長名鑑"''')
    data13 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="ダウンロード"''')
    data14 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="その他"''')
    data15 = cur.fetchall()

    cur=mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
FROM robotkanri WHERE 部署="リストアップ"''')
    data16 = cur.fetchall()
#TAB 2
    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
    FROM robotkanri WHERE 作成者="松本" AND 完成="完成"''')
    k1 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
        FROM robotkanri WHERE 作成者="井上" AND 完成="完成"''')
    k2 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
    FROM robotkanri WHERE 作成者="李そ" AND 完成="完成"''')
    k3 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
    FROM robotkanri WHERE 作成者="廣瀬" AND 完成="完成"''')
    k4= cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
        FROM robotkanri WHERE 作成者="ピチュカ" AND 完成="完成"''')
    k5 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
        FROM robotkanri WHERE 作成者="澤山" AND 完成="完成"''')
    k6 = cur.fetchall()
#TAB 3
    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
    FROM robotkanri WHERE 作成者="松本" AND 完成="未完成"''')
    m1 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
        FROM robotkanri WHERE 作成者="井上" AND 完成="未完成"''')
    m2 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
    FROM robotkanri WHERE 作成者="李そ" AND 完成="未完成"''')
    m3 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
    FROM robotkanri WHERE 作成者="廣瀬" AND 完成="未完成"''')
    m4= cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
        FROM robotkanri WHERE 作成者="ピチュカ" AND 完成="未完成"''')
    m5 = cur.fetchall()

    cur = mysql.connection.cursor()
    cur.execute('''SELECT ID,ロボット名,依頼者,部署,作成者,日,完成,削減時間
        FROM robotkanri WHERE 作成者="澤山" AND 完成="未完成"''')
    m6 = cur.fetchall()

    return render_template('home.html', data1=data1,data2=data2,data3=data3,data4=data4,data5=data5,dat6=data6,data7=data7,data8=data8,data9=data9,data10=data10,data11=data11,data12=data12,data13=data13,data14=data14,data15=data15,data16=data16,k1=k1,k2=k2,k3=k3,k4=k4,k5=k5,k6=k6,m1=m1,m2=m2,m3=m3,m4=m4,m5=m5,m6=m6)


@app.route("/testlim1/<id>")
def testtttt(id):
    cur=mysql.connection.cursor()
    query_string=("""SELECT ロボット名,依頼者,部署,作成者,日,備考
    FROM robotkanri WHERE ID='{id}' LIMIT 1""".format(id=id))
    cur.execute(query_string)
    data = cur.fetchall()
    return render_template('testhome.html', data=data)
##TEST
@app.route('/home/edit/sour/<id>', methods=['GET', 'POST'])
def soured(id):
    sidid = id
    cur = mysql.connection.cursor()
    ab=sidid.split("_")
    id=int(ab[0])
    sid=int(ab[1])
    cur.execute("""SELECT
                   shurui_details_%s,shurui_id_%s,inout_%s FROM robotkanri WHERE ID=%s""",(sid,sid,sid,id))

    # cur.execute("""SELECT
    #                shurui_details_%s,shurui_id_%s,inout_%s FROM robotkanri""",(id,id,id))

    d = cur.fetchall()
    d=d[0]
    form = Robotform(formdata=request.form, sourcetype=d[1], sourceinfo=d[0], inout=d[2],sidid=sidid)
    test = "222222222222222222222"
    if request.method == 'POST':
        if request.form.get('delete') == 'delete':
                delete_sour(sid, id, form)
                mysql.connection.commit()
                flash('Robot updated successfully!')
                return redirect('/home/edit/' + str(id))
        elif request.form.get('editform') == 'editform':

                source_edit(sid, id, form)
                mysql.connection.commit()
                flash('Robot updated successfully!')
                return redirect('/home/edit/' + str(id))

    return render_template('source_edit.html', d=d, form=form,test=test)
def delete_sour(sid, id, form):
    cur = mysql.connection.cursor()

    cur.execute("""UPDATE
              robotkanri SET shurui_id_%s=NULL,shurui_details_%s=NULL,inout_%s=NULL WHERE ID=(%s)""", (sid, sid, sid, id))
def source_edit(sid,id,form):

    cur = mysql.connection.cursor()

    shu_id=form.sourcetype.data
    shuinfo=form.sourceinfo.data
    inout=form.inout.data

    cur.execute("""UPDATE
              robotkanri SET shurui_id_%s=(%s),shurui_details_%s=(%s),inout_%s=(%s) WHERE ID=(%s)""", (sid, shu_id, sid, shuinfo, sid, inout, id))


@app.route('/home/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    cur = mysql.connection.cursor()
    query_string = ("""SELECT ロボット名,依頼者,部署,作成者,日,スケジュール,ログ,IFNULL(目的,''),IFNULL(概要,''),完成,削減時間,削減時間ノート
    ,shurui_id_1,shurui_id_2,shurui_id_3,shurui_id_4,shurui_id_5,shurui_id_6,shurui_id_7,shurui_id_8,shurui_id_9,shurui_id_10,shurui_details_1,shurui_details_2,shurui_details_3,shurui_details_4,shurui_details_5,shurui_details_6,shurui_details_7,shurui_details_8,shurui_details_9,shurui_details_10,inout_1,inout_2,inout_3,inout_4,inout_5,inout_6,inout_7,inout_8,inout_9,inout_10
        FROM robotkanri WHERE ID='{id}' LIMIT 1""".format(id=id))
    cur.execute(query_string)
    data = cur.fetchall()
    if data:
        lst = list(data[0])
        lograw=lst[6]
        log=lst[6]
        log =log.split('@!')
        sour1=lst[12:22]
        sour2=lst[22:32]
        sour3=lst[32:42]
        sour1=list(filter(None.__ne__, sour1))
        sour2=list(filter(None.__ne__, sour2))
        sour3=list(filter(None.__ne__, sour3))
        sourid=[]

        for i in range(1,11):

             sourid.append(str(id)+"_"+str(i))
        zips=zip(sour1,sour2,sour3,sourid)
 #       sourt=list_to_html_table(sourt,1,column_major=True)
        form = Robotform(formdata=request.form,robotname=lst[0],iraisha=lst[1],busho=lst[2],developer=lst[3], last_mod=lst[4],schedule=lst[5],obje=lst[7],gaiyo=lst[8],kansei=lst[9],sakujikan=lst[10],sakujikannote=lst[11])
        if request.method == 'POST' and form.validate():

            if request.form.get('editform') == 'editform':
                  edit_changes(id, form,lograw)
                  flash('Robot updated successfully!')
                  return redirect('/home')
            elif request.form.get('addsource') == 'addsource':

                add_source(form,id)

                mysql.connection.commit()
                return redirect('/home/edit/'+id)
        return render_template('edit_robot.html', zips=zips,sour1=sour1,sour2=sour2,sour3=sour3,form=form,data=data,log=log)
    else:
        return 'Error loading #{id}'.format(id=id)

def add_source(form,id):
    cur = mysql.connection.cursor()

    cur.execute("""SELECT shurui_id_1,shurui_id_2,shurui_id_3,shurui_id_4,shurui_id_5,shurui_id_6,shurui_id_7,shurui_id_8,shurui_id_9,shurui_id_10 FROM robotkanri WHERE id=(%s)""",([id]))

    de=(cur.fetchall())

    cd=de[0]
    ed=cd[1]
    for i in range(0,10):
       if cd[i]==None:
           index=i+1
           break
    sid=form.sourcetype.data
    details=form.sourceinfo.data
    inout=form.inout.data
    #index=1
   # cur.execute("""UPDATE
   #            robotkanri SET shurui_id_'{index}'='{sid}',shurui_details_'{index}'='{details}',inout_'{index}'='{inout}' WHERE ID='{id}'""".format(id=id,index=index,sid=sid,details=details,inout=inout))
    cur.execute("""UPDATE
             robotkanri SET shurui_id_%s=%s,shurui_details_%s=%s,inout_%s=%s WHERE ID=%s""",(index,sid,index,details,index,inout,id))
    #if shurui_id_1=="":
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
    schedule = form.schedule.data
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
       logr="".join((logs,'@!',today," ",logn))

    if new:
        # Add the new album to the database
        cur.execute(
            """
    UPDATE robotkanri SET ロボット名=(%s),依頼者=(%s),部署=(%s),作成者=(%s),日=(%s),ログ=(%s),目的=(%s),概要=(%s),完成=(%s),削減時間=(%s),削減時間ノート=(%s),スケジュール=(%s) WHERE ID=(%s)""",
            (robotname, iraisha, busho, developer ,last_mod,logr,obje,gaiyo,kansei,sakuji,sakujin,schedule,id))
        mysql.connection.commit()

def add_shu(id,form):
    cur = mysql.connection.cursor()
    cur.execute("""SELECT inout__1,inout__2,inout__3,inout__4,inout__5,inout__6,inout__7,inout__8,inout__9,inout__10""")
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
@app.route('/new_robot', methods=['GET','POST'])
def new_robot():
    """
    Add a new album
    """
    form = Robotform(request.form)
    ## originally ->    if request.method == 'POST' and form.validate():
    if request.method == 'POST':
          # save the album
            save_changes(form)
            flash('ロボットが追加されました!')
            return redirect('/home')

    form.gaiyo.data=""
    form.obje.data=""
    return render_template('newrobot.html', form=form)


def save_changes(form, new=True):


    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    lograw=""
    cur = mysql.connection.cursor()
    robotname = form.robotname.data
    iraisha = form.iraisha.data
    busho = form.busho.data
    developer = form.developer.data
    last_mod = form.last_mod.data
    schedule = form.schedule.data
    obje = form.obje.data
    gaiyo = form.gaiyo.data
    logn = form.log.data
    sakuji = form.sakujikan.data
    sakujin = form.sakujikannote.data
    today = str(date.today())
    logs = str(lograw)
    kansei = form.kansei.data
    if logn == "":
        logr = logs
    else:
        logr = "".join((logs, '@!', today, " ", logn))
    if new:
        # Add the new album to the database
        cur.execute(
            """INSERT INTO 
                robotkanri(ロボット名,依頼者,部署,作成者,日,ログ,目的,概要,完成,削減時間,削減時間ノート,スケジュール)
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (robotname, iraisha, busho, developer ,last_mod,logr,obje,gaiyo,kansei,sakuji,sakujin,schedule))
        mysql.connection.commit()

@app.route('/home/edit/2t1qhq1hq1', methods=['GET', 'POST'])
def souredold(sidid):
    sidid=str(sidid)
    id=sidid[0]
    sid=sidid[2]
    cur = mysql.connection.cursor()
    cur.execute("""SELECT
                   shurui_details_1,shurui_id_1,inout_1 FROM robotkanri where ID=(%s)""",(id))
   # cur.execute("""SELECT
#                shurui_details_%s,shurui_id_%s,inout_%s FROM robotkanri""",(id,id,id))

    d=cur.fetchall()
    form = Robotform(formdata=request.form,sourcetype=d[0],sourceinfo=d[1],inout=d[2])

    return render_template('source_edit.html', d=d,form=form)
#to edit source

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0')