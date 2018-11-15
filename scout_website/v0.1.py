from operator import is_not
from functools import partial
import requests
from flask_mysqldb import MySQL
import random
from flask import flash, render_template, redirect,request,make_response

from flask import Flask,render_template,url_for,request,redirect,session,flash,abort,jsonify
import os
from scforms import HomeForm,twomonthplusform
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
  #      username = request.cookies.get('username')
  #  if request.cookies.get('password'):
   #     password = request.cookies.get('password')


    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
    if request.form["username"] == "" or request.form["password"] == "":

        return render_template('login.html', username=username)
    else:
        username = request.form['username']
        password = request.form['password']
        print(username+password)
        cur = mysql.connection.cursor()
        query=("SELECT c.company_name,c.tsr_code,p.id,p.contract_date,p.accompany_date FROM spms_users_test u  "
        " LEFT JOIN spms_salesmans_test s "
        "  INNER JOIN _live_spms__sk_projects p ON  p.id=s.sk_project_id"
        "   INNER JOIN _live_spms__clients c ON c.id=p.client_id"
        "   ON s.salesman=u.id "
        "   WHERE account='%s'" % (username))

        print(query)
        cur.execute(query)
        data=cur.fetchall()
        resp = make_response(render_template('schome.html',username=username,data=data))
        resp.set_cookie('username', username)
        resp.set_cookie('password', password)
        return resp
@app.route('/kaseki', methods=['POST', 'GET'])
def kaseki():
    asd=""
@app.route('/edit/<id>', methods=['POST', 'GET'])
def edit(id):
    if id=="株式会社山豊工建":
        form=twomonthplusform(request.form)
        print(form)
        return render_template('input_2monthplus.html', form=form)
@app.route('/input', methods=['POST', 'GET'])

def input():
    """
    Add a new album
    """
    form = twomonthplusform(formdata=request.form)
    print(form)
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
  #  iraisha = form.iraisha.data
  #  busho = form.busho.data
    today = strftime("%Y-%m-%d %H:%M:%S")
    today = today[:16]

if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True
    app.run(host='0.0.0.0',port=5002)