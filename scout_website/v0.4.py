from operator import is_not
from functools import partial
import requests
from flask_mysqldb import MySQL
import random
from flask import flash, render_template, redirect,request,make_response
from datetime import datetime
from flask import Flask,render_template,url_for,request,redirect,session,flash,abort,jsonify
import os
from scforms import HomeForm,twomonthplusform,homon_kai
from flask import flash, render_template, redirect,request
from flask import request
from datetime import date
from time import gmtime, strftime
global str
from django.template.defaulttags import register
import json
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
@app.route('/')
def index():
   print("pl")
   return render_template('login.html')

@app.route('/home', methods=['POST', 'GET'])
def home():
  #  if request.cookies.get('username'):
    username = request.cookies.get('username')
  #  if request.cookies.get('password'):
    password = request.cookies.get('password')
    form=request.form

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    if form:
        if request.form["username"] == "" or request.form["password"] == "":

            return render_template('login.html', username=username)

    print(username+password)
    cur = mysql.connection.cursor()
    query=("SELECT c.company_name,c.tsr_code,p.id,p.contract_date,p.accompany_date FROM spms_users_test u  "
    " LEFT JOIN spms_salesmans_test s "
    "  INNER JOIN _live_spms__sk_projects p ON  p.id=s.sk_project_id"
    "   INNER JOIN _live_spms__clients c ON c.id=p.client_id"
    "   ON s.salesman=u.id "
    "   WHERE account='%s'" % (username))

    cur.execute(query)
    data=cur.fetchall()
    print(str(len(data)))
    # add 連絡対象
   # data = [("asd",)+ l for l in data]
    index=0
    for l in data:
        data=list(data)
       # print(l[0])
        cur = mysql.connection.cursor()
        query="SELECT taisho FROM sk_system_renrakutaishou where tsr=%s"%(l[1])
        cur.execute(query)
        print(query)
        tais=cur.fetchall()
        if tais==():
            tais=""
            tuple(tais)
            print(tais)
        else:
            tais=tais[0][0]

            # 前回接触方法	以降
        cur = mysql.connection.cursor()
        query="SELECT 接触日,接触方法,やりとり内容,入力ステータス FROM sk_system_setsuzoku_history where tsr_code=%s ORDER  BY id DESC"%(l[1])
        cur.execute(query)
        print(query)
        zenkai=cur.fetchall()
        if zenkai==():
            zen=("","","","")
        else:
            zen=(zenkai[0][0],zenkai[0][1],zenkai[0][2],zenkai[0][3])
        data[index]= (tais,)+l+zen
        index = index + 1



    resp = make_response(render_template('schome.html',username=username,data=data))
    resp.set_cookie('username', username)
    resp.set_cookie('password', password)
    return resp
@app.route('/kaseki', methods=['POST', 'GET'])
def kaseki():
    asd=""
@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
        username = request.cookies.get('username')
        password= request.cookies.get('password')
        cur = mysql.connection.cursor()
        query=("SELect company_name FROM _live_spms__clients WHERE tsr_code='%s'" % (id))
        cur.execute(query)
        compn=cur.fetchall()[0][0]
        print(compn)
        print(username)

        form1=twomonthplusform(request.form)
        form1.contdate.data=datetime.now().strftime("%Y-%m-%d")
        form1.compname.data=compn
        print(form1.contdate.data)
        form2=homon_kai(request.form)
        form2.contdate.data=datetime.now().strftime("%Y-%m-%d")
        form2.compname.data=compn
        cond=4
        #「前回の連絡から2ヶ月以上経過」の場合
        if cond ==1:
                if request.method == 'POST':
                    if request.form.get('editform') == 'editform':
                          input(id, form1)
                          flash('Robot updated successfully!')
                          return redirect(url_for('home'))
                return render_template('input_2monthplus.html', form=form1)
        #「PKMから6ヶ月目」の場合

        elif cond ==2:
                if request.method == 'POST':

                    if request.form.get('editdayes') == 'editdayes':
                      input(id, form1)
                      flash('Robot updated successfully!')
                      return redirect(url_for('home'))
                    elif request.form.get('editdano') == 'editdano':
                      input2(id, form1)
                      flash('Robot updated successfully!')
                      return redirect(url_for('home'))
                return render_template('pkm_6months.html', form=form1)
        #「案件終了」の場合
        elif cond ==3:
                if request.method == 'POST':

                    if request.form.get('editdayes') == 'editdayes':
                      input(id, form1)
                      flash('Robot updated successfully!')
                      return redirect(url_for('home'))
                    elif request.form.get('editdano') == 'editdano':
                      input2(id, form1)
                      flash('Robot updated successfully!')
                      return redirect(url_for('home'))
                return render_template('anken_shuuryo.html', form=form1)
        elif cond == 4:

            if request.method == 'POST':

                if request.form.get('editform') == 'editform':

                    input3(id, form2)
                    flash('Robot updated successfully!')
                    return redirect(url_for('home'))
            return render_template('houmon_kai.html', form=form2)
@app.route('/input', methods=['POST', 'GET'])
#FOｒ　First form and 2nd form (a) 打診する
def input(id,form1,new=True):
    """
    Add a new album
    """
    concont1date=concont1name=concont2date=concont2name=concont3date=concont3name=""
    print(id)
    form=form1
    cur = mysql.connection.cursor()
    compname=form.compname.data
    contdate=form.contdate.data
    inputstatus=form.houmondashin.data
    contactmeth=form.contactmeth.data
    contactcontent1=form.contactcontent1.data
    concont1date=form.concont1date.data
    concont1name=form.concont1name.data
    contactcontent2=form.contactcontent2.data
    concont2date=form.concont2date.data
    concont2name=form.concont2name.data
    contactcontent3=form.contactcontent3.data
    concont3date=form.concont3date.data          #受領した紹介先
    concont3name=form.concont3name.data
    yaritoricont=form.yaritoricont.data
    q1=form.q1.data
    q2=form.q2.data

    memo=""
    print(contactcontent1)
    if new:
        cur.execute("""INSERT INTO sk_system_setsuzoku_history(tsr_code,接触日,接触方法,接触時メモ,連絡内容①,会食打診した→日程,会食打診した→断られた「理由」,連絡内容②, 訪問打診した→日程, 訪問打診した→断られた「理由」, 連絡内容③, 受領した紹介先, 紹介打診した→断られた「理由」,やりとり内容,自分とのリレーションレベル,スカウトサービスへの満足度,入力ステータス) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (id,contdate,contactmeth,memo,contactcontent1,concont1date,concont1name,contactcontent2,concont2date,concont2name,contactcontent3,concont3date,concont3name,yaritoricont,q1,q2,inputstatus))
        mysql.connection.commit()
# this is for 2nd form 打診しない
def input2(id,form1,new=True):
    """
    Add a new album
    """
    print(id)

    concont1date=concont1name=concont2date=concont2name=concont3date=concont3name=""
    form=form1
    cur = mysql.connection.cursor()
    compname=form.compname.data
    contdate=form.contdate.data
    contactmeth=form.contactmeth.data                                            # MAKING IT NULLLLLLLLLLLLLLLLLLLLLLLLL
    contactcontent1=form.contactcontent1.data
    concont1date=form.concont1date.data
    concont1name=form.concont1name.data
    contactcontent2=form.contactcontent2.data
    concont2date=form.concont2date.data
    concont2name=form.concont2name.data
    contactcontent3=form.contactcontent3.data
    concont3date=form.concont3date.data          #受領した紹介先
    concont3name=form.concont3name.data
    yaritoricont=form.yaritoricont.data
    q1=form.q1.data
    q2=form.q2.data
    inputstatus=form.houmondashin.data
    contactcontent1=""
    contactcontent2=""
    contactcontent3=""
    contactmeth=""
    riyuu=""
    riyuu1=form.dashinshinai.data
    riyuu2 = form.dashinshinai_comp.data
    if len(riyuu1)>len(riyuu2):
        riyuu=riyuu1
    else:
        riyuu=riyuu2
    memo="理由:"+riyuu
    print(contactcontent1)
    if new:
        cur.execute("""INSERT INTO sk_system_setsuzoku_history(tsr_code,接触日,接触方法,接触時メモ,連絡内容①,会食打診した→日程,会食打診した→断られた「理由」,連絡内容②, 訪問打診した→日程, 訪問打診した→断られた「理由」, 連絡内容③, 受領した紹介先, 紹介打診した→断られた「理由」,やりとり内容,自分とのリレーションレベル,スカウトサービスへの満足度,入力ステータス) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (id,contdate,contactmeth,memo,contactcontent1,concont1date,concont1name,contactcontent2,concont2date,concont2name,contactcontent3,concont3date,concont3name,yaritoricont,q1,q2,inputstatus))
        mysql.connection.commit()
def input3(id,form2,new=True):
    """
    Add a new album
    """
    print(id)

    concont1date=concont1name=concont2date=concont2name=concont3date=concont3name=""
    form=form2
    cur = mysql.connection.cursor()
    compname=form.compname.data
    contdate=form.contdate.data
    contactmeth=form.contactmeth.data
    clients=form.clients.data
    raynos=form.raynos.data
    recieved=form.recieved.data
    yaritoricont=form.yaritoricont.data
    q1=form.q1.data
    q2=form.q2.data
    inputstatus=request.form.getlist('recieved')
    inputstatus= ''.join(inputstatus)

    print(inputstatus)
    print(recieved)
    if new:
        cur.execute(
            """INSERT INTO sk_system_setsuzoku_history(tsr_code,接触日,接触方法,接触時メモ,連絡内容①,会食打診した→日程,会食打診した→断られた「理由」,連絡内容②, 訪問打診した→日程, 訪問打診した→断られた「理由」, 連絡内容③, 受領した紹介先, 紹介打診した→断られた「理由」,やりとり内容,自分とのリレーションレベル,スカウトサービスへの満足度,頂いたもの) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (id, contdate, contactmeth, concont1date, concont1date, concont1date, concont1name, concont1date, concont2date,
            concont2name, concont1date, concont3date, concont3name, yaritoricont, q1, q2, inputstatus))
    mysql.connection.commit()
@app.route('/comp/<id>', methods=['POST'])
def comp():
    data = request.get_json()
    print(data)
@app.route('/get_post_json/', methods=['POST'])
def get_post_json():
    data = request.get_json()
    print(data)
def save_changes(form, new=True):


    """
    Save the changes to the database
    """
    # Get data from form and assign it to the correct attributes
    # of the SQLAlchemy table object
    lograw=""
    cur = mysql.connection.cursor()
  #  iraisha = form.iraisha.data
  #  busho = form.busho.data
    today = strftime("%Y-%m-%d %H:%M:%S")
    today = today[:16]

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0',port=5004)