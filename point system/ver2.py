from operator import is_not
from functools import partial
import requests
from flask_mysqldb import MySQL
import random
from flask import Flask,render_template,url_for,request,redirect,session,flash,abort,jsonify
import os
from flask import flash, render_template, redirect,request,make_response
from flask import request
from datetime import date
from time import gmtime, strftime
global str
from django.template.defaulttags import register
import json
import sys

sys.path.insert(0, './point system')

from psforms import pointform,yoteipoints
import re
from itertools import groupby

app=Flask(__name__)
app.config['MYSQL_HOST']='192.168.5.124'
app.config['MYSQL_USER']='eigyou_kikaku'
app.config['MYSQL_PASSWORD']='As6hV2K!k'
app.config['MYSQL_DB']='eigyou_kikaku'
mysql = MySQL(app)
@app.route('/')
def index():
   return render_template('index.html')
@app.route('/home', methods=['POST', 'GET'])
def home():
    form = pointform(formdata=request.form)
    if request.cookies.get('userID'):
        user = request.cookies.get('userID')

    if request.form['nm']:
        user = request.form['nm']
    print(user)
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM komon_action_result_update WHERE user_id=%s''',[user])
    data1 = cur.fetchall()
    cur=mysql.connection.cursor()
    cur.execute('''SELECT * FROM mode_action_result_update WHERE user_id=%s''',[user])
    data2 = cur.fetchall()
    cur=mysql.connection.cursor()
    cur.execute('''SELECT * FROM sf_action_result_update WHERE user_id=%s''',[user])
    data3 = cur.fetchall()
    cur=mysql.connection.cursor()
    cur.execute('''SELECT * FROM siemple_action_result_update WHERE user_id=%s''',[user])
    data4 = cur.fetchall()
    busho="komon"
   #   data1=data4
    print(type(data1))
    print(len(data1))
    if len(data1)==0 and len(data2)==0 and len(data3)==0 and len(data4)==0:
        resp = make_response(
            render_template('home404.html', userid=user, data1=data1, data2=data2, data3=data3, data4=data4))
        resp.set_cookie('userID', user)
    else:
        if len(data2)!=0:
            data1=data2
            busho="mode"
        if len(data3)!=0:
            data1=data3
            busho="sf"
        if len(data4)!=0:
            data1=data4
            busho="siemple"
        #to remove none
        count=0
        data=()
        for d in data1:
            i=['0' if v is None else v for v in data1[count]]
            i=tuple(i)
            data=data+(i,)
            count=count+1
        print(data)
        print(data1)
        resp=redirect("/quar")
       # resp = make_response(render_template('home.html',form=form,userid=user,data=data,data1=data1,data2=data2,data3=data3,data4=data4))
        cur = mysql.connection.cursor()
        query = "SELECT Q FROM %s_action_result_update WHERE user_id='%s'" % (busho, user)
        cur.execute(query)
        quadata = cur.fetchall()
        max_year = 0
        max_Q = 0
        for i in quadata:
            l = [int(''.join(i)) for is_digit, i in groupby(i[0], str.isdigit) if is_digit]
            if l[0] > max_year:
                max_year = l[0]
        for i in quadata:
            l = [int(''.join(i)) for is_digit, i in groupby(i[0], str.isdigit) if is_digit]
            if l[0] == max_year and l[1] > max_Q:
                max_Q = l[1]
        print(max_year)
        print(max_Q)
        qua = str(max_year) + "-" + str(max_Q) + "Q"
        # qua end
        resp.set_cookie('userID', user)
        resp.set_cookie('busho',busho)
        resp.set_cookie('quar',qua)
        session['busho']=busho
        session['username']=user
        session.modified = True
    return resp
#newhome
@app.route('/home1', methods=['POST', 'GET'])
def home1():
    form = pointform(formdata=request.form)

    user = request.cookies.get('userID')
    busho = request.cookies.get('busho')
    qua=request.cookies.get('quar')
    busho.strip('"\'')
    cur = mysql.connection.cursor()
    query=   "SELECT * FROM %s_action_result_update WHERE user_id='%s'"% (busho,user)
    print(query)
    cur.execute(query)
    data1 = cur.fetchall()
    count = 0
    data = ()
    for d in data1:
        i = ['0' if v is None else v for v in data1[count]]
        i = tuple(i)
        data = data + (i,)
        count = count + 1
    return render_template('home.html', userid=user, data=data,form=form)
#thisweek
@app.route('/week', methods=['POST', 'GET'])
def week():
    form = pointform(formdata=request.form)

    user = request.cookies.get('userID')
    busho = request.cookies.get('busho')
    qua=request.cookies.get('quar')
    busho.strip('"\'')

    print(busho)
    print(type(busho))
    cur = mysql.connection.cursor()
    query=   "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND  YEARWEEK(`date`, 1) = YEARWEEK(CURDATE(), 1)"% (busho,user)
    print(query)
    cur.execute(query)
    data1 = cur.fetchall()
    count = 0
    data = ()
    for d in data1:
        i = ['0' if v is None else v for v in data1[count]]
        i = tuple(i)
        data = data + (i,)
        count = count + 1
    return render_template('home.html', userid=user, data=data,form=form)
#thisq
@app.route('/quar', methods=['POST', 'GET'])
def quar():
    form = pointform(formdata=request.form)
    yoteiform = yoteipoints(formdata=request.form)
    user = request.cookies.get('userID')
    busho = request.cookies.get('busho')
    qua=request.cookies.get('quar')
    busho.strip('"\'')


   # qua="21-3Q"
    query=   "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s'"% (busho,user,qua)

    cur = mysql.connection.cursor()
    cur.execute(query)
    data1 = cur.fetchall()
    dmformat="'%m-%d'"

    query= ("select concat(7*ceil(営業日/7)-6, '-', 7*ceil(営業日/7) ) as `range`,CONCAT(DATE_FORMAT(min(date),%s),'～',DATE_FORMAT(max(date),%s)),count(*),count(電話数),count(つな数),count(アポ),count(初回営業),count(再訪設定),count(`面談設定(初)`),count(`面談実施(初)`),count(受注),count(point)"
            " as `number of users` from ( SELECT * FROM  %s_action_result_update WHERE user_id='%s' and Q='%s') t group by 1 order by 営業日;"%
                    (dmformat,dmformat,busho,user,qua))
    print(query)
    queryl1=("select concat(7*ceil(営業日/7)-6, '-', 7*ceil(営業日/7) ) as `range`,CONCAT(DATE_FORMAT(min(date),%s),'～',DATE_FORMAT(max(date),%s)),count(*),count(電話数),count(つな数),count(アポ),count(初回営業),count(再訪設定),count(`面談設定(初)`),count(`面談実施(初)`),count(受注),count(point)"
            " as `number of users` from ( SELECT * FROM  %s_action_result_update WHERE user_id='%s' and Q='%s' and list_type='源泉') t group by 1 order by 営業日;"%
                    (dmformat,dmformat,busho,user,qua))
    queryl2=("select concat(7*ceil(営業日/7)-6, '-', 7*ceil(営業日/7) ) as `range`,CONCAT(DATE_FORMAT(min(date),%s),'～',DATE_FORMAT(max(date),%s)),count(*),count(電話数),count(つな数),count(アポ),count(初回営業),count(再訪設定),count(`面談設定(初)`),count(`面談実施(初)`),count(受注),count(point)"
            " as `number of users` from ( SELECT * FROM  %s_action_result_update WHERE user_id='%s' and Q='%s' and list_type='管S') t group by 1 order by 営業日;"%
                    (dmformat,dmformat,busho,user,qua))
    queryl3=("select concat(7*ceil(営業日/7)-6, '-', 7*ceil(営業日/7) ) as `range`,CONCAT(DATE_FORMAT(min(date),%s),'～',DATE_FORMAT(max(date),%s)),count(*),count(電話数),count(つな数),count(アポ),count(初回営業),count(再訪設定),count(`面談設定(初)`),count(`面談実施(初)`),count(受注),count(point)"
            " as `number of users` from ( SELECT * FROM  %s_action_result_update WHERE user_id='%s' and Q='%s' and list_type='その他') t group by 1 order by 営業日;"%
                    (dmformat,dmformat,busho,user,qua))
    cur.execute(query)
    week1=cur.fetchall()
    cur.execute(queryl1)
    weekl1=cur.fetchall()
    cur.execute(queryl2)
    weekl2=cur.fetchall()
    cur.execute(queryl3)
    weekl3=cur.fetchall()
    print(weekl1)
    query = ("SELECT * FROM pointsystem_yotei_week WHERE userid='%s' and Q='%s'"%(user,qua))
    cur.execute(query)
    yotei = cur.fetchall()
    count=0
    weekn1 = ()
    for d in week1:
        i = ['0' if v is None else v for v in week1[count]]
        weekname="第"+str(count+1)+"週"
        i[0]=weekname
        counter=0

        for e in yotei:
            if e[13]==str(count+1) and e[14]=="all":
                counter=1
                i.insert(3, e[1])
                i.insert(5, e[2])
                i.insert(7, e[3])
                i.insert(9, e[4])
                i.insert(11, e[5])
                i.insert(13, e[6])
                i.insert(15, e[7])
                i.insert(17, e[8])
                i.insert(19, e[9])
        if counter==0:
            i.insert(3, 111)
            i.insert(5, 222)
            i.insert(7, 333)
            i.insert(9, 444)
            i.insert(11, 555)
            i.insert(13, 666)
            i.insert(15, 777)
            i.insert(17, 888)
            i.insert(19, 999)
        i = tuple(i)
        weekn1 = weekn1 + (i,)
        count = count + 1
    count=0
    weeklo1 = ()
    for d in weekl1:
        i = ['0' if v is None else v for v in weekl1[count]]
        weekname="第"+str(count+1)+"週"
        i[0]=weekname
        counter=0

        for e in yotei:
            if e[13]==str(count+1) and e[14]=="源泉":
                counter=1
                i.insert(3, e[1])
                i.insert(5, e[2])
                i.insert(7, e[3])
                i.insert(9, e[4])
                i.insert(11, e[5])
                i.insert(13, e[6])
                i.insert(15, e[7])
                i.insert(17, e[8])
                i.insert(19, e[9])
        if counter==0:
            i.insert(3, 111)
            i.insert(5, 222)
            i.insert(7, 333)
            i.insert(9, 444)
            i.insert(11, 555)
            i.insert(13, 666)
            i.insert(15, 777)
            i.insert(17, 888)
            i.insert(19, 999)
        i = tuple(i)
        weeklo1 = weeklo1 + (i,)
        count = count + 1
    count=0
    weeklo2 = ()
    for d in weekl2:
        i = ['0' if v is None else v for v in weekl2[count]]
        weekname="第"+str(count+1)+"週"
        i[0]=weekname
        counter=0

        for e in yotei:
            if e[13]==str(count+1) and e[14]=="管S":
                counter=1
                i.insert(3, e[1])
                i.insert(5, e[2])
                i.insert(7, e[3])
                i.insert(9, e[4])
                i.insert(11, e[5])
                i.insert(13, e[6])
                i.insert(15, e[7])
                i.insert(17, e[8])
                i.insert(19, e[9])
        if counter==0:
            i.insert(3, 111)
            i.insert(5, 222)
            i.insert(7, 333)
            i.insert(9, 444)
            i.insert(11, 555)
            i.insert(13, 666)
            i.insert(15, 777)
            i.insert(17, 888)
            i.insert(19, 999)
        i = tuple(i)
        weeklo2 = weeklo2 + (i,)
        count = count + 1
    count=0
    weeklo3 = ()
    for d in weekl3:
        i = ['0' if v is None else v for v in weekl3[count]]
        weekname="第"+str(count+1)+"週"
        i[0]=weekname
        counter=0

        for e in yotei:
            if e[13]==str(count+1) and e[14]=="その他":
                counter=1
                i.insert(3, e[1])
                i.insert(5, e[2])
                i.insert(7, e[3])
                i.insert(9, e[4])
                i.insert(11, e[5])
                i.insert(13, e[6])
                i.insert(15, e[7])
                i.insert(17, e[8])
                i.insert(19, e[9])
        if counter==0:
            i.insert(3, 111)
            i.insert(5, 222)
            i.insert(7, 333)
            i.insert(9, 444)
            i.insert(11, 555)
            i.insert(13, 666)
            i.insert(15, 777)
            i.insert(17, 888)
            i.insert(19, 999)
        i = tuple(i)
        weeklo3 = weeklo3 + (i,)
        count = count + 1
    return render_template('quarbyweek_new.html', userid=user,yoteiform=yoteiform,form=form,week1=weekn1,weekl1=weeklo1,weekl2=weeklo2,weekl3=weeklo3)
@app.route('/datesel', methods=['POST', 'GET'])
def datesel():
    user = request.cookies.get('userID')
    busho = request.cookies.get('busho')
    qua=request.cookies.get('quar')

    form = pointform(formdata=request.form)
    if request.method == 'POST' and form.validate():

       # if request.form.get('datesearch') == 'datesearch':
        startdate=form.startdate.data
        enddate=form.enddate.data
    if form.data["startdate"] == None or form.data["enddate"] == None:
        return render_template('home.html', userid=user, form=form)
    else:

        busho.strip('"\'')
        cur = mysql.connection.cursor()
        query=   "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND date between '%s' and '%s' "% (busho,user,startdate,enddate)
        print(query)
        print(startdate)
        print(enddate)
        cur.execute(query)
        data1 = cur.fetchall()
        count = 0
        data = ()
        for d in data1:
            i = ['0' if v is None else v for v in data1[count]]
            i = tuple(i)
            data = data + (i,)
            count = count + 1
        return render_template('home.html', userid=user, data=data,form=form)
@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']

    resp = make_response(render_template('readcookie.html',userid=user))
    resp.set_cookie('userID', user)

    return resp
@app.route('/getcookie')
def getcookie():
   name = request.cookies.get('userID')
   busho=request.cookies.get('busho')

   qua = request.cookies.get('quar')
   return '<h1>welcome '+name+'</h1>'
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin':
            return redirect(url_for('home',_anchor='SK'))
    return render_template('login.html', error=error)
@app.route('/logout', methods=['POST', 'GET'])
def logout():
    form = pointform(formdata=request.form)


    return redirect("/")
@app.route('/_get_post_json/', methods=['POST'])
def get_post_json():
    data = request.get_json()

    user = request.cookies.get('userID')
    busho = request.cookies.get('busho')
    qua=request.cookies.get('quar')
    if data:
        data=data["hello"]
        data=data.split("\t\t\t\t\t\t\t\t\t\t\t\t")
        data = [elem for elem in data if elem.strip()]
        data = [x.strip(' ') for x in data]

        print(data)
        week=data[0][1]
        print("week")
        print(week)
        denwa=data[3]
        tsuna=data[5]
        apo=data[7]
        shokai=data[9]
        saihou=data[11]
        mendans=data[13]
        mendanj=data[15]
        juchu=data[17]
        point=data[19]
        today = strftime("%Y-%m-%d %H:%M:%S")
        cur = mysql.connection.cursor()
        todaydate="".join(today)
        query=("SELECT EXISTS(SELECT * FROM pointsystem_yotei_week WHERE userid='%s' and Q='%s' and week='%s')"%(user,qua,week))
        #checking if data alr in table
        cur.execute(query)
        check=cur.fetchall()[0][0]
        print(check)
        if check==0:
                cur = mysql.connection.cursor()
                cur.execute("""INSERT INTO pointsystem_yotei_week (電話数,つな数,アポ,初回営業,再訪設定,面談設定,面談実地,受注,ポイント,timestamp,userid,Q,week) 
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s   )""",
                            (denwa,tsuna,apo,shokai,saihou,mendans,mendanj,juchu,point,todaydate,user,qua,week))
                print("success")
                mysql.connection.commit()
                cur.close()
        elif check==1:
                cur = mysql.connection.cursor()
                query=""" UPDATE pointsystem_yotei_week SET
                timestamp='%s',電話数='%s',つな数='%s',アポ='%s',初回営業='%s',再訪設定='%s',面談設定='%s',面談実地='%s',受注='%s',ポイント='%s' WHERE userid='%s' and Q='%s' and week='%s'"""%(todaydate,denwa,tsuna,apo,shokai,saihou,mendans,mendanj,juchu,point,user,qua,week)
                print(query)
                cur.execute(query)
                print("hello")
                mysql.connection.commit()
                cur.close()
    return redirect(url_for('quar'))
#if __name__ == "__main__":
    #app.secret_key = 'super secret key'
  #  app.config['SESSION_TYPE'] = 'filesystem'
    #app.debug = True
   # app.run(host='0.0.0.0',port=5001)
if __name__ == "__main__":
        app.secret_key = '\x0cw1\xd4\xd5\x80%O?q \xcfQrrk\xa3H\xc0[J\xae<\xc3]\xe6\x10\xc0-\xf8S\x08P4[3]PrK\xa9\xf1'
        app.run(debug=True,host='0.0.0.0',port=5001)
