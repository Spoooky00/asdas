import os.path

import pymysql.cursors
from datetime import datetime
from app import app
from config import mysql
from flask import Flask, render_template, request, redirect, jsonify, session


# Route to render the login page
@app.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute('SELECT * FROM account_management WHERE AM_User_name = %s AND AM_password = %s AND AM_Status=1',
                       (username, password))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['AM_User_name']
            # Redirect to home page
            print("TEST LOGIN")
            return redirect('/clinic_admin')
        else:
            msg = 'INCORRECT CREDENTIALS!'
    return render_template('login/login.html')


# Route ro render the log out
##LOGOUT ROUTE
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
    session.pop('loggedin', None)
    session.pop('id', None)
    # Redirect to login page
    return redirect('/')


# Route to render the clinic_admin page
@app.route('/clinic_admin', methods=['GET'])
def dashboard():
    if 'loggedin' in session:
        return render_template('clinic_admin.html')
    else:
        return redirect('/')


# Route to render the events page
@app.route('/events', methods=['GET'])
def events():
    if 'loggedin' in session:
        print("TEST EVENTS")
        return render_template('events_appointments.html')
    else:
        return redirect('/')


# Route to render the account_management page
@app.route('/account_management', methods=['GET', 'POST'])
def account_management():
    if 'loggedin' in session:
        if request.method == 'GET':
            try:
                conn = mysql.connect()
                cursor = conn.cursor(pymysql.cursors.DictCursor)
                cursor.execute("SELECT* from `account_management`")
                accountmanagement = cursor.fetchall()
                print(accountmanagement)
                return render_template('account_management/account_management2.html', data=accountmanagement)
            except Exception as e:
                print(e)
            finally:
                cursor.close()
                conn.close()
    if request.method == 'POST':
        print("hello")


# update
@app.route('/updateAM/<path:id>', methods=['GET', 'POST'])
def updateAM(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT* from `account_management` where AM_User_name = %s", id)
        accountmanagement = cursor.fetchall()
        print(accountmanagement)
        return render_template('account_management/updateAM.html', data=accountmanagement)
    if request.method == 'POST':
        _Username = request.form['Username']
        _Password = request.form['Password']
        _Email = request.form['Email']
        _Role = request.form['Role']

        if request.form:
            query = "update account_management set AM_User_name=%s , AM_Email=%s, AM_Password=%s, AM_Role=%s where AM_User_name=%s"
            bindData = (_Username, _Email, _Password, _Role, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query, bindData)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/account_management')


# add
@app.route('/addAM', methods=['GET', 'POST'])
def addAM():
    if request.method == 'POST':
        print("result : " + str(request.json))
        # ETO UNG DATA GALING SA JS REQUEST
        _name = request.json['username']
        _Email = request.json['email']
        _Role = request.json['role']
        _PW = request.json['password']
        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            # ETO UNG DATABASE COLS NAME
            query = "insert into account_management(AM_User_name,AM_Email,AM_Role,AM_Password) values(%s,%s,%s,%s)"
            bindData = (_name, _Email, _Role, _PW)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/account_management')
    else:
        return render_template('account_management/addAM.html')


# Route to render the patient_masters_record page
@app.route('/pmr', methods=['GET', 'POST'])
def pmr():
    if request.method == 'GET':
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * from `pmr2`")
            pmr = cursor.fetchall()
            print("TEST PMR")  # //lol eto ung error
            return render_template('pmr/Pmr.html', data=pmr)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    if request.method == 'POST':
        print("hello")


# update
@app.route('/updatePmr/<int:id>', methods=['GET', 'POST'])
def updatePmr(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT* from `pmr2` where User_NFC_ID = %s", id)
        pmr = cursor.fetchall()
        print("TEST PMR UPDATE")
        return render_template('pmr/updatePmr.html', data=pmr)
    if request.method == 'POST':
        _NFC = str(request.form['NFC'])
        _Fname = str(request.form['PMR_Fname'])
        _Lname = str(request.form['PMR_Lname'])
        _Section = str(request.form['PMR_Section'])
        _Lvl = str(request.form['PMR_Yr_lvl'])
        _DB = str(request.form['PMR_DB'])
        _Address = str(request.form['PMR_Address'])
        _Gender = str(request.form['PMR_Gender'])
        _BT = str(request.form['PMR_BT'])
        _LUD = str(request.form['PMR_LUD'])
        _ECN = str(request.form['PMR_ECN'])
        _RTTP = str(request.form['PMR_RTTP'])
        _ECNO = str(request.form['PMR_ECNO'])
        _HI = str(request.form['PMR_HI'])

        # dump(request.form)
        if request.form:
            query = "update pmr2 set PMR_Fname=%s , PMR_Lname=%s, PMR_Section=%s, PMR_Yr_Lvl=%s , PMR_DB=%s, PMR_Address=%s, PMR_Gender=%s, PMR_BT=%s, PMR_LUD=%s, PMR_ECN=%s, PMR_RTTP=%s, PMR_ECNO=%s, PMR_HI=%s where User_NFC_ID=%s"
            bindData = (
            _Fname, _Lname, _Section, _Lvl, _DB, _Address, _Gender, _BT, _LUD, _ECN, _RTTP, _ECNO, _HI, _NFC)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query, bindData)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/pmr')


# add
@app.route('/addPMR', methods=['GET', 'POST'])
def addPmr():
    if request.method == 'POST':
        #ung str(request.json) dito para makita ko lang kung ano ung laman
        print("result : " + str(request.json))
        #eto naman lahat ng galing sa json ilipat mo kay data para maccess as array
        data = request.json
        #dito nag test lang ako  kung nakikita talaga, so oo
        print(data['nfc_tag'])
        current_time = datetime.now()
        lud = current_time.strftime('%m/%d/%Y')
        #last update date is curdate ng pag add, from system un

        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "INSERT INTO `pmr2` (`User_NFC_ID`, `PMR_Fname`, `PMR_Lname`, `PMR_Section`, `PMR_Yr_lvl`, `PMR_DB`, `PMR_Address`, `PMR_Gender`, `PMR_BT`, `PMR_LUD`, `PMR_ECN`, `PMR_RTTP`, `PMR_ECNO`, `PMR_HI`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
        #    query = "insert into pmr2(Username,Email,Role) values(%s,%s,%s)"
            #since kita ung data sa json as array, hndi na ako gumamit ng _var kasi hahaba lang code ko
            #ung nasa loob ng [' '] ay ung name ng var na pinsa mo mula sa js
            bindData = (data['nfc_tag'],data['fname'],data['lname'],data['section'],data['yr'],data['db'],data['address'],data['gender'],data['bt'],lud,data['ecn'],data['rttp'],data['ecno'],data['hi'])
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/pmr')
    else:
        return render_template('pmr/addPmr.html')


#########################DAILY LOGS ROUTES
# Route to render the daily_logs page
@app.route('/daily_logs', methods=['GET', 'POST'])
def daily_logs():
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT* from `pmr2` JOIN `daily_logs` on `pmr2`.`User_NFC_ID` = `daily_logs`.`User_NFC_ID`;")
        daily_logs = cursor.fetchall()
        print("DL"+str(daily_logs))
        conn2 = mysql.connect()
        cursor2 = conn2.cursor(pymysql.cursors.DictCursor)
        cursor2.execute("SELECT * from `pmr2`")
        pmr_data = cursor2.fetchall()
        print("PMR"+str(pmr_data))
        return render_template('daily_logs/daily_logs.html', data=zip(daily_logs,pmr_data))

    if request.method == 'POST':
        print("hello")


# update
@app.route('/updateDL/<int:id>', methods=['GET', 'POST'])
def updateDL(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT* from `pmr2` JOIN `daily_logs` on `pmr2`.`User_NFC_ID` = `daily_logs`.`User_NFC_ID` where `DL_ID`=%s;",
            id)
        dailylogs = cursor.fetchall()
        print(dailylogs)
        return render_template('daily_logs/updateDl.html', data=dailylogs)
    if request.method == 'POST':
        _NFC = request.form['NFC']
        _Concern = request.form['DL_Concern']
        _TI = request.form['DL_TI']
        _TO = request.form['DL_TO']
        if request.form:
            query = "update daily_logs set DL_Concerm=%s, DL_Timein=%s, DL_Timeout=%s where DL_ID=%s"
            bindData = (_Concern, _TI, _TO, _NFC)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query, bindData)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/daily_logs')


# add
@app.route('/addDL', methods=['POST'])
def addDL():
    if request.method == 'POST':
        print("result : " + str(request.json))
        _nfc = request.json['nfc']
        _concern = request.json['concern']
        _ti = request.json['ti']
        _to = request.json['to']
        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            query = "insert into daily_logs(USER_NFC_ID,DL_Concerm,DL_Timein,DL_Timeout) values(%s,%s,%s,%s)"
            bindData = (_nfc, _concern, _ti, _to)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/daily_logs')
    # render_template('addDL.html')


#########################INVENTORY ROUTES
# Route to render the inventory page
@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'GET':
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT* from `inventory`")
            inventory = cursor.fetchall()
            print(inventory)
            return render_template('Inventory/Inventory.html', data=inventory)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    if request.method == 'POST':
        print("hello")


# update
@app.route('/updateinventory/<int:id>', methods=['GET', 'POST'])
def updateinventory(id):
    if request.method == 'GET':
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(
            "SELECT* from `inventory` where Item_ID = %s", id)
        inventory = cursor.fetchall()
        print(inventory)
        return render_template('inventory/updateInventory.html', data=inventory)
    if request.method == 'POST':
        _itemname = request.form['Item_name']
        _quantity = request.form['Quantity']
        _manufacturer = request.form['Manufacturer']
        _description = request.form['Description']
        _code = request.form['Item_code']
        _expiry = request.form['Item_expiry']
        _type = request.form['Item_type']

        if request.form:
            query = "update inventory set Item_name=%s, Quantity=%s ,Manufacturer=%s , Description=%s , Item_code=%s , Item_expiry=%s , Item_type=%s  where Item_ID = %s"
            bindData = (_itemname, _quantity, _manufacturer, _description, _code, _expiry, _type, id)
            conn = mysql.connect()
            cursor = conn.cursor()
            print(query, bindData)
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/inventory')


# add
@app.route('/addinventory', methods=['GET', 'POST'])
def addinventory():
    if request.method == 'POST':
        print("result : " + str(request.json))
        # ETO UNG DATA GALING SA JS REQUEST
        data = request.json
        if request.json:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            # ETO UNG DATABASE COLS NAME
            query = "INSERT INTO `inventory` (`Item_ID`, `Item_name`, `Quantity`, `Manufacturer`, `Description`, `Item_code`, `Item_expiry`, `Item_type`) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s);"
            bindData = (data['itemname'],data['quantity'],data['manufacturer'],data['description'],data['code'],data['expiry'],data['type'])
            cursor.execute(query, bindData)
            conn.commit()
            return redirect('/inventory')
    else:
        return render_template('Inventory/addinventory.html')


if __name__ == '__main__':
    app.run(debug=True)
