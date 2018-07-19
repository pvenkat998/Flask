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
        resp = make_response(render_template('home.html',form=form,userid=user,data=data,data1=data1,data2=data2,data3=data3,data4=data4))
        resp.set_cookie('userID', user)
        resp.set_cookie('busho',busho)
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
    busho.strip('"\'')
    cur = mysql.connection.cursor()
    cur = mysql.connection.cursor()
    query=   "SELECT Q FROM %s_action_result_update WHERE user_id='%s'"% (busho,user)

    cur.execute(query)
    quadata = cur.fetchall()
    max_year=0
    max_Q=0
    for i in quadata:
        l = [int(''.join(i)) for is_digit, i in groupby(i[0], str.isdigit) if is_digit]
        if l[0]>max_year:
            max_year=l[0]
    for i in quadata:
        l = [int(''.join(i)) for is_digit, i in groupby(i[0], str.isdigit) if is_digit]
        if l[0]==max_year and l[1]>max_Q:
            max_Q=l[1]
    print(max_year)
    print(max_Q)
    qua=str(max_year)+"-"+str(max_Q)+"Q"
   # qua="21-3Q"
    query=   "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s'"% (busho,user,qua)

    cur.execute(query)
    data1 = cur.fetchall()

    # the data for each week
    #week1
    query=   "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s' AND 営業日 BETWEEN 1 and 7"% (busho,user,qua)

    cur.execute(query)
    week1 = cur.fetchall()
    #week2
    query=   "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s' AND 営業日 BETWEEN 8 and 14"% (busho,user,qua)

    cur.execute(query)
    week2 = cur.fetchall()
    #week3
    query=   "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s' AND 営業日 BETWEEN 15 and 21"% (busho,user,qua)

    cur.execute(query)
    week3 = cur.fetchall()
    # week4
    query = "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s' AND 営業日 BETWEEN 22 and 28" % (
    busho, user, qua)

    cur.execute(query)
    week4 = cur.fetchall()
    # week3
    query = "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s' AND 営業日 BETWEEN 29 and 35" % (
    busho, user, qua)

    cur.execute(query)
    week5 = cur.fetchall()
    # week3
    query = "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s' AND 営業日 BETWEEN 36 and 42" % (
    busho, user, qua)

    cur.execute(query)
    week6 = cur.fetchall()
    # week3
    query = "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s' AND 営業日 BETWEEN 43 and 49" % (
    busho, user, qua)

    cur.execute(query)
    week7 = cur.fetchall()
    # week3
    query = "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s' AND 営業日 BETWEEN 50 and 56" % (
    busho, user, qua)

    cur.execute(query)
    week8 = cur.fetchall()
    # week3
    query = "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s' AND 営業日 BETWEEN 57 and 63" % (
    busho, user, qua)

    cur.execute(query)
    week9 = cur.fetchall()
    # week3
    query = "SELECT * FROM %s_action_result_update WHERE user_id='%s' AND Q='%s' AND 営業日 BETWEEN 63 and 70" % (
    busho, user, qua)
    cur.execute(query)
    week10 = cur.fetchall()
    query = "SELECT * FROM pointsystem_yotei"
    cur.execute(query)
    yotei = cur.fetchall()
    count=0
    weekn1 = ()
    for d in week1:
        i = ['0' if v is None else v for v in week1[count]]
        counter=0
        print(i)
        for e in yotei:
            print(e)
            if e[0]==i[0]:
                print("YES")
                counter=1
                i.insert(10, e[1])
                i.insert(12, e[2])
                i.insert(14, e[3])
                i.insert(16, e[4])
                i.insert(18, e[5])
                i.insert(20, e[6])
                i.insert(22, e[7])
                i.insert(24, e[8])
                i.insert(26, e[9])
        if counter==0:
            i.insert(10, 2009)
            i.insert(12, 2009)
            i.insert(14, 2009)
            i.insert(16, 2009)
            i.insert(18, 2009)
            i.insert(20, 2009)
            i.insert(22, 2009)
            i.insert(24, 2009)
            i.insert(26, 2009)
        i = tuple(i)
        weekn1 = weekn1 + (i,)
        count = count + 1
    return render_template('quarbyweek.html', userid=user,yoteiform=yoteiform,form=form,week1=weekn1,week2=week2,week3=week3,week4=week4,week5=week5,week6=week6,week7=week7,week8=week8,week9=week9,week10=week10)
@app.route('/datesel', methods=['POST', 'GET'])
def datesel():
    user = request.cookies.get('userID')
    busho = request.cookies.get('busho')

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

    if data:
        data=data["hello"]
        data=data.split("\t\t\t\t\t\t\t\t\t\t\t\t")
        data = [elem for elem in data if elem.strip()]
        id=data[0]
        denwa=data[10]
        tsuna=data[12]
        apo=data[14]
        shokai=data[16]
        saihou=data[18]
        mendans=data[20]
        mendanj=data[22]
        juchu=data[24]
        point=data[26]
        today = strftime("%Y-%m-%d %H:%M:%S")
        cur = mysql.connection.cursor()
        todaydate="".join(today)
        cur.execute("""INSERT INTO pointsystem_yotei (ID,電話数,つな数,アポ,初回営業,再訪設定,面談設定,面談実地,受注,ポイント,timestamp) 
        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
        timestamp=%s,電話数=%s,つな数=%s,アポ=%s,初回営業=%s,再訪設定=%s,面談設定=%s,面談実地=%s,受注=%s,ポイント=%s""",
                    (id,denwa,tsuna,apo,shokai,saihou,mendans,mendanj,juchu,point,todaydate,todaydate,denwa,tsuna,apo,shokai,saihou,mendans,mendanj,juchu,point))
        mysql.connection.commit()
        cur.close()
        print("yay/?")
    print(data)
    print(denwa)
    return redirect(url_for('quar'))
#if __name__ == "__main__":
    #app.secret_key = 'super secret key'
  #  app.config['SESSION_TYPE'] = 'filesystem'
    #app.debug = True
   # app.run(host='0.0.0.0',port=5001)
if __name__ == "__main__":
        app.secret_key = '\x0cw1\xd4\xd5\x80%O?q \xcfQrrk\xa3H\xc0[J\xae<\xc3]\xe6\x10\xc0-\xf8S\x08P4[3]PrK\xa9\xf1'
        app.run(debug=True,host='0.0.0.0',port=5001)
