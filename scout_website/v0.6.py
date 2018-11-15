# - coding: utf-8 --
from operator import is_not
from functools import partial
import requests
from flask_mysqldb import MySQL
import random
from flask import flash, render_template, redirect,request,make_response
import datetime
from flask import Flask,render_template,url_for,request,redirect,session,flash,abort,jsonify
import os
from scforms import twomonthplusform,homon_kai
from flask import flash, render_template, redirect,request
from flask import request
from datetime import date
from time import gmtime, strftime
global str
from django.template.defaulttags import register
import json
import pymysql

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
#db = pymysql.connect(host="192.168.5.124", user="eigyou_kikaku",password= "As6hV2K",db= "eigyou_kikaku", charset='utf8', port=3306)

##HOME PAGE
# row and column majors for defining source stuffff

@app.route('/')
def index():
   print("Login attempt")
   return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
   print("Logout attempt")
   username=""
   resp=redirect(url_for('index'))
   resp.set_cookie('username', '', expires=0)
   return resp
@app.route('/home', methods=['POST', 'GET'])
def home():
  #  if request.cookies.get('username'):
    print(2)
    username = request.cookies.get('username')
  #  if request.cookies.get('password'):
    password = request.cookies.get('password')
    form=request.form


    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    print(1)


    if not form:
        return redirect(url_for('index'))
    if form:
        if request.form["username"] == "" or request.form["password"] == "":

            return render_template('login.html', username=username)
    cur = mysql.connection.cursor()
    query=("SELECT code from _live_company__syain WHERE user_id='%s'" % (username))
    cur.execute(query)
    pw=cur.fetchall()[0][0]
  #  print(pw)
    cur = mysql.connection.cursor()
    query=("SELECT CONCAT(sei,mei) from _live_company__syain WHERE user_id='%s'" % (username))
    cur.execute(query)
    sm=cur.fetchall()[0][0]

    if form:
        if str(pw)!=str(password):
            return render_template('login.html', username=username)

   # print(username+password)
    cur = mysql.connection.cursor()
    query=("SELECT c.company_name,c.tsr_code,p.id,p.contract_date,COALESCE(p.accompany_date, '') AS accompany_date FROM spms_users_test u  "
    " LEFT JOIN spms_salesmans_test s "
    "  INNER JOIN _live_spms__sk_projects p ON  p.id=s.sk_project_id"
    "   INNER JOIN _live_spms__clients c ON c.id=p.client_id"
    "   ON s.salesman=u.id "
    "   WHERE account='%s' GROUP BY c.tsr_code ORDER BY p.contract_date DESC" % (username))


    cur.execute(query)
    data=cur.fetchall()
  #  print(str(len(data)))
    cur = mysql.connection.cursor()

#case when address2 is null then 'None Provided' else address2 end as address2,
    query = ("SELECT  t.訪問打診した→日程,c.company_name,c.tsr_code,p.id,p.contract_date,COALESCE(p.accompany_date, '') AS accompany_date,t.`接触日`,t.`接触方法`,t.`やりとり内容`,t.`入力ステータス`"
             " FROM sk_system_setsuzoku_history t  "
             "LEFT JOIN spms_users_test u "
             " LEFT JOIN spms_salesmans_test s "
             "  INNER JOIN _live_spms__sk_projects p ON  p.id=s.sk_project_id"
             "   INNER JOIN _live_spms__clients c ON c.id=p.client_id"
             "   ON s.salesman=u.id ON t.tsr_code=c.tsr_code "
             "   WHERE account='%s' AND t.`接触日`IS NOT NULL ORDER BY t.ID DESC" % (username))
    cur.execute(query)
    data2 = cur.fetchall()
#data2 reaady
  # add 連絡対象
  # data = [("asd",)+ l for l in data]
    index=0
    for l in data:
        data=list(data)
        cur = mysql.connection.cursor()
        query="SELECT taisho FROM sk_system_renrakutaishou where tsr=%s"%(l[1])
        cur.execute(query)
        tais=cur.fetchall()
        if tais==():
            tais=""
            tuple(tais)
        else:
            tais=tais[0][0]

            # 前回接触方法	以降
        cur = mysql.connection.cursor()
        query="SELECT 接触日,接触方法,やりとり内容,入力ステータス FROM sk_system_setsuzoku_history where tsr_code=%s ORDER  BY id DESC LIMIT 1"%(l[1])
        cur.execute(query)
        zenkai=cur.fetchall()
        if zenkai==():
            zen=("","","","")
        else:
            zen=(zenkai[0][0],zenkai[0][1],zenkai[0][2],zenkai[0][3])
        data[index]= (tais,)+l+zen
        index = index + 1







    #kaseki tab      -----------------------------------kaseki----------------------------------------------------------------------





    cur = mysql.connection.cursor()
    query1=("SELECT r.taisho,c.company_name,concat(u.last_name,u.first_name),c.tsr_code,p.id,p.contract_date, COALESCE(p.accompany_date, '') AS accompany_date FROM sk_system_renrakutaishou r LEFT JOIN _live_spms__clients c ON c.tsr_code=r.tsr LEFT JOIN _live_spms__sk_projects p ON p.client_id=c.id LEFT JOIN spms_salesmans_test s ON s.sk_project_id=p.id LEFT JOIN spms_users_test u ON u.id=s.salesman WHERE r.kaseki='%s' GROUP BY c.tsr_code ORDER BY p.contract_date DESC" % (username))
    print(query1)
    cur.execute(query1)
    datak1 = cur.fetchall()
   # datak1=()


    index=0
    for l in datak1:
        datak1 = list(datak1)
      # 前回接触方法	以降
        cur = mysql.connection.cursor()
        query = "SELECT 接触日,接触方法,やりとり内容,入力ステータス FROM sk_system_setsuzoku_history where tsr_code='%s' ORDER  BY id DESC LIMIT 100" % (
        l[3])
        print(query)
        cur.execute(query)
        zenkai = cur.fetchall()
        print(zenkai)
        if zenkai == ():
            zen = ("", "", "", "")
        else:
            zen = (zenkai[0][0], zenkai[0][1], zenkai[0][2], zenkai[0][3])
        datak1[index] =  l + zen
        index = index + 1
  #hard one
    cur.close()
    cur = mysql.connection.cursor()
   # curs= db.cursor()
    #query1 = ("SELECT * FROM (SELECT a.* ,IF(@temp_cp = a.company_name, IF(@temp_cp_date = CONCAT(a.company_name,a.contract_date), @flag, @flag := @flag + 1), @flag := 1) as count, @temp_cp := a.company_name as temp1, @temp_cp_date := concat(a.company_name, a.contract_date) as temp2 FROM (( SELECT t.訪問打診した→日程, c.company_name, c.tsr_code, p.id, p.contract_date, COALESCE(p.accompany_date, '') AS accompany_date, t.`接触日`, t.`接触方法`, t.`やりとり内容`, t.`入力ステータス` FROM sk_system_renrakutaishou as r LEFT JOIN _live_spms__clients c ON c.tsr_code=r.tsr LEFT JOIN _live_spms__sk_projects p ON p.client_id=c.id LEFT JOIN sk_system_setsuzoku_history t ON t.tsr_code=r.tsr WHERE r.kaseki='%s' and t.接触日 is not null ORDER BY company_name DESC, p.contract_date DESC )) as a, (SELECT @temp_cp := NULL, @temp_cp_date = NULL, @flag := 0) as aa) as awrv WHERE count=1 " % (username))
   # query1 = ("SELECT a.* ,IF(@temp_cp = a.company_name, IF(@temp_cp_date = CONCAT(a.company_name,a.contract_date), @flag, @flag := @flag + 1), @flag := 1) as count, @temp_cp := a.company_name as temp1, @temp_cp_date := concat(a.company_name, a.contract_date) as temp2 FROM (( SELECT t.訪問打診した→日程, c.company_name, c.tsr_code, p.id, p.contract_date, COALESCE(p.accompany_date, '') AS accompany_date, t.`接触日`, t.`接触方法`, t.`やりとり内容`, t.`入力ステータス` FROM sk_system_renrakutaishou as r LEFT JOIN _live_spms__clients c ON c.tsr_code=r.tsr LEFT JOIN _live_spms__sk_projects p ON p.client_id=c.id LEFT JOIN sk_system_setsuzoku_history t ON t.tsr_code=r.tsr WHERE r.kaseki='%s' and t.接触日 is not null ORDER BY company_name DESC, p.contract_date DESC )) as a, (SELECT @temp_cp := NULL, @temp_cp_date = NULL, @flag := 0) as aa " % (username))
#final try
    query1 = "SELECT * FROM (SELECT a.* , IF(@temp_cp = a.company_name, IF(@temp_cp_date = CONCAT(a.company_name,a.contract_date), @flag, @flag := @flag + 1), @flag := 1) as count, @temp_cp := a.company_name as temp1, @temp_cp_date := concat(a.company_name, a.contract_date) as temp2 FROM (( SELECT t.訪問打診した→日程, c.company_name,concat(u.last_name,u.first_name), c.tsr_code, p.id, p.contract_date, COALESCE(p.accompany_date, '') AS accompany_date, t.`接触日`, t.`接触方法`, t.`やりとり内容`, t.`入力ステータス` FROM sk_system_renrakutaishou as r LEFT JOIN _live_spms__clients c ON c.tsr_code=r.tsr LEFT JOIN _live_spms__sk_projects p ON p.client_id=c.id LEFT JOIN sk_system_setsuzoku_history t ON t.tsr_code=r.tsr LEFT JOIN spms_salesmans_test s ON s.sk_project_id=p.id LEFT JOIN spms_users_test u ON u.id=s.salesman  WHERE r.kaseki='kodaka' and t.接触日 is not null ORDER BY company_name DESC, p.contract_date DESC )) as a, (SELECT @temp_cp := NULL, @temp_cp_date = NULL, @flag := 0) as aa ) as awrv WHERE count=1 or id=( SELECT max(id) FROM (SELECT a.* , IF(@temp_cp = a.company_name, IF(@temp_cp_date = CONCAT(a.company_name,a.contract_date), @flag, @flag := @flag + 1), @flag := 1) as count, @temp_cp := a.company_name as temp1, @temp_cp_date := concat(a.company_name, a.contract_date) as temp2 FROM (( SELECT t.訪問打診した→日程, c.company_name, c.tsr_code, p.id, p.contract_date, COALESCE(p.accompany_date, '') AS accompany_date, t.`接触日`, t.`接触方法`, t.`やりとり内容`, t.`入力ステータス` FROM sk_system_renrakutaishou as r LEFT JOIN _live_spms__clients c ON c.tsr_code=r.tsr LEFT JOIN _live_spms__sk_projects p ON p.client_id=c.id LEFT JOIN sk_system_setsuzoku_history t ON t.tsr_code=r.tsr WHERE r.kaseki='kodaka' and t.接触日 is not null ORDER BY company_name DESC, p.contract_date DESC )) as a, (SELECT @temp_cp := NULL, @temp_cp_date = NULL, @flag := 0) as aa ) as qwe )"
    print(query1)
  #  curs.execute(query1)
    cur.execute(query1)

    datak2 = cur.fetchall()


    cur.close()
    resp = make_response(render_template('schome.html',username=sm,data=data,data2=data2,datak1=datak1,datak2=datak2))
    resp.set_cookie('sm',sm)
    resp.set_cookie('username', username)
    resp.set_cookie('password', password)
    return resp
@app.route('/kaseki', methods=['POST', 'GET'])
def kaseki():
    asd=""
@app.route('/comp/<id>', methods=['POST', 'GET'])
def comp(id):
    cur=mysql.connection.cursor()
    query=("SELECT 接触者,接触日,接触方法,やりとり内容 from sk_system_setsuzoku_history s"
           " INNER JOIN _live_spms__clients c on c.tsr_code=s.tsr_code"
           " WHERE c.company_name='%s'  ORDER BY 接触日 DESC , 接触者	"%(id))
    cur.execute(query)
    comp=cur.fetchall()
    return render_template("comp.html",id=id,comp=comp)
@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
        print(request.cookies.get("sm"))
        username = request.cookies.get('username')
        password= request.cookies.get('password')
        cur = mysql.connection.cursor()
        query=("SELect company_name FROM _live_spms__clients WHERE tsr_code='%s'" % (id))
        cur.execute(query)
        compn=cur.fetchall()[0][0]
        print(compn)
        print(username)
        today = datetime.date.today()
        mylist = []
        today = datetime.date.today()
        mylist.append(today)
        form1=twomonthplusform(request.form)
        form1.contdate.data= mylist[0]
        form1.compname.data=compn
        form2=homon_kai(request.form)
        form2.contdate.data= mylist[0]
        form2.compname.data=compn

        #decide which form   !!!!!

        cur = mysql.connection.cursor()
        query="SELECT taisho FROM sk_system_renrakutaishou where tsr=%s"%(id)
        cur.execute(query)
        tais=cur.fetchall()

        print(tais)
        if tais==():
            cond=4
        else:
            condstr=tais[0][0]
            if condstr=="案件終了":
                cond=3
            elif condstr=="前回の連絡から2ヶ月以上経過":
                cond=1
            elif condstr=="PKMから6ヶ月目":
                cond=2
            else:
                cond=4
        #「前回の連絡から2ヶ月以上経過」の場合
        if cond ==1:
                if request.method == 'POST':

                    if request.form.get('editform') == 'editform':
                          input(id, form1,cond)
                          flash('Robot updated successfully!')

                          return redirect(url_for('home'))
                return render_template('input_2monthplus.html', form=form1)
        #「PKMから6ヶ月目」の場合

        elif cond ==2:
                if request.method == 'POST':

                    if request.form.get('editdayes') == 'editdayes':
                      input(id, form1,cond)
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
                      input(id, form1,cond)
                      flash('Robot updated successfully!')
                      return redirect(url_for('home'))
                    elif request.form.get('editdano') == 'editdano':
                      input2(id, form1)
                      flash('Robot updated successfully!')
                      return redirect(url_for('home'))
                return render_template('anken_shuuryo.html', form=form1)
        elif cond == 4:
            print("ok")
            if request.method == 'POST':

                if request.form.get('editform') == 'editform':

                    input3(id, form2,cond)
                    flash('Robot updated successfully!')
                    return redirect(url_for('home'))
            return render_template('houmon_kai.html', form=form2)
@app.route('/input', methods=['POST', 'GET'])
#FOｒ　First form and 2nd form (a) 打診する
def input(id,form1,cond,new=True):
    """
    Add a new album
    """
    request.cookies.get("sm")
    concont1date=concont1name=concont2date=concont2name=concont3date=concont3name=""
    print(id)
    form=form1
    cur = mysql.connection.cursor()
    compname=form.compname.data
    contdate=form.contdate.data
    if cond==1:
        inputstatus =""
    else:
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
    username=request.cookies.get("sm")
    print(username)
    memo=""
    print(contactcontent1)
    if new:
        cur.execute("""INSERT INTO sk_system_setsuzoku_history(tsr_code,接触日,接触方法,接触時メモ,連絡内容①,会食打診した→日程,会食打診した→断られた「理由」,連絡内容②, 訪問打診した→日程, 訪問打診した→断られた「理由」, 連絡内容③, 受領した紹介先, 紹介打診した→断られた「理由」,やりとり内容,自分とのリレーションレベル,スカウトサービスへの満足度,入力ステータス,接触者) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (id,contdate,contactmeth,memo,contactcontent1,concont1date,concont1name,contactcontent2,concont2date,concont2name,contactcontent3,concont3date,concont3name,yaritoricont,q1,q2,inputstatus,username))
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
    username=request.cookies.get("sm")
    if len(riyuu1)>len(riyuu2):
        riyuu=riyuu1
    else:
        riyuu=riyuu2
    memo="理由:"+riyuu
    print(contactcontent1)

    if inputstatus=="打診しない":
        yaritoricont=memo
    if new:
        cur.execute("""INSERT INTO sk_system_setsuzoku_history(tsr_code,接触日,接触方法,接触時メモ,連絡内容①,会食打診した→日程,会食打診した→断られた「理由」,連絡内容②, 訪問打診した→日程, 訪問打診した→断られた「理由」, 連絡内容③, 受領した紹介先, 紹介打診した→断られた「理由」,やりとり内容,自分とのリレーションレベル,スカウトサービスへの満足度,入力ステータス,接触者) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                    (id,contdate,contactmeth,memo,contactcontent1,concont1date,concont1name,contactcontent2,concont2date,concont2name,contactcontent3,concont3date,concont3name,yaritoricont,q1,q2,inputstatus,username))
        mysql.connection.commit()
def input3(id,form2,new=True):
    """
    Add a new album
    """
    print(id)
    username=request.cookies.get("sm")

    concont1date=concont1name=concont2date=concont2name=concont3date=concont3name=""
    form=form2
    cur = mysql.connection.cursor()
    concont3date=form.clients.data
    concont3name=form.raynos.data
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
            """INSERT INTO sk_system_setsuzoku_history(tsr_code,接触日,接触方法,接触時メモ,連絡内容①,会食打診した→日程,会食打診した→断られた「理由」,連絡内容②, 訪問打診した→日程, 訪問打診した→断られた「理由」, 連絡内容③, 受領した紹介先, 紹介打診した→断られた「理由」,やりとり内容,自分とのリレーションレベル,スカウトサービスへの満足度,頂いたもの,接触者) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
            (id, contdate, contactmeth, concont1date, concont1date, concont1date, concont1name, concont1date, concont2date,
            concont2name, concont1date, concont3date, concont3name, yaritoricont, q1, q2, inputstatus,username))
    mysql.connection.commit()

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0',port=5002)