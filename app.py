import os
# Flask から importしてflaskを使えるようにする
import sqlite3, datetime as dt
from flask import Flask, render_template, request, redirect, session
import mysql.connector 
# from mysql.connector import errorcode

# appの名前でFlaskアプリを作っていく
app = Flask(__name__)
# ここまでおまじない
app.secret_key="sunabaco"

# @app.route("/")
# def init():
#     return render_template('init.html')

@app.route("/")
def helloWorld():
    return render_template('index.html')

# DBへの接続
@app.route("/index")
def index():
    conn = mysql.connector.connect(
        user='HajimeFujii',  # ユーザー名
        password='04fujkan11',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database='MyOutdoorNote'  # データベース名
    )
    c = conn.cursor()
    c.close()
    return render_template("index.html")

#追加の処理/イベント
@app.route("/add/event",methods=["POST"])
def add_post_event():
    date = request.form.get("date")
    event = request.form.get("event")
    photo = request.form.get("photo")
    memo = request.form.get("memo")

    conn = mysql.connector.connect(
        user='HajimeFujii',  # ユーザー名
        password='04fujkan11',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database='MyOutdoorNote'  # データベース名
    )
    c = conn.cursor()

    sql = ('''
    INSERT INTO 2023_winter 
        (date, event, photo, memo)
    VALUES 
        (%s, %s, %s, %s)
    ''')
    data = [
        (date, event, photo, memo),
    ]
    c.executemany(sql, data)
    conn.commit()

    c.close()
    return redirect("/list")

# DBに保存されているものを表示してみよう
@app.route("/list")
def item_list():
    conn = mysql.connector.connect(
        user='HajimeFujii',  # ユーザー名
        password='04fujkan11',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database='MyOutdoorNote'  # データベース名
    )
    c = conn.cursor()

    c.execute('select * from 2023_winter order by date DESC')
    # リスト型にする
    item_list=[]
    # print(c.fetchall())
    for row in c.fetchall():
        #rowの要素を連想配列に記述
        item_list.append({"event_id":row[0],"date":row[1],"event":row[2],"photo":row[3],"memo":row[4]})
    c.close()
    return render_template("eventitem_list.html",eventitem_list = item_list)

# イベントの編集
@app.route("/edit/event/<int:event_id>")
def edit_event(event_id):
    conn = mysql.connector.connect(
        user='HajimeFujii',  # ユーザー名
        password='04fujkan11',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database='MyOutdoorNote'  # データベース名
    )
    c = conn.cursor()
    c.execute("select date from 2023_winter where event_id = %s", (event_id,))
    date = c.fetchone()[0]
    c.execute("select event from 2023_winter where event_id = %s", (event_id,))
    event = c.fetchone()[0]
    c.execute("select photo from 2023_winter where event_id = %s", (event_id,))
    photo = c.fetchone()[0]
    c.execute("select memo from 2023_winter where event_id = %s", (event_id,))
    memo = c.fetchone()[0]
    print(event_id)
    print(memo)
    c.close()
    item = {"date":date, "event":event, "photo":photo, "memo":memo}
    print(item)
    print(event_id)
    return render_template("edit_event.html" , item = item, event_id = event_id)
    
# 変更したデータでイベント更新
@app.route("/edit/event", methods = ["POST"])
def update_event():
    event_id = request.form.get("event_id")
    date = request.form.get("date")
    event = request.form.get("event")
    photo = request.form.get("photo")
    memo = request.form.get("memo")
    conn = mysql.connector.connect(
        user='HajimeFujii',  # ユーザー名
        password='04fujkan11',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database='MyOutdoorNote'  # データベース名
    )
    c = conn.cursor()

    sql = "UPDATE 2023_winter SET date = %s, event = %s, photo = %s, memo = %s where event_id = %s"
    data = (date, event, photo, memo, event_id)
    c.execute(sql, data)
    conn.commit()
    c.close()
    return redirect("/list")

# イベントの削除
@app.route("/del/event/<int:event_id>")
def del_event(event_id):
    conn = mysql.connector.connect(
        user='HajimeFujii',  # ユーザー名
        password='04fujkan11',  # パスワード
        host='localhost',  # ホスト名(IPアドレス）
        database='MyOutdoorNote'  # データベース名
    )
    c = conn.cursor()
    c.execute("delete from 2023_winter where event_id = %s", (event_id,))
    c = conn.commit()
    conn.close()
    return redirect("/list")

# 2021.6.15 ログイン機能など-----------------------------------------------------------
# 登録機能

# @app.route("/regist", methods = ["GET"])
#     # GETはHTMLを表示するだけ
# def regist_get():
#     return render_template("regist.html")

# @app.route("/regist", methods=["POST"])
# def regist_post():
#     name = request.form.get("name")
#     password = request.form.get("password")
#     # requestでHTML側からデータを受け取る
    
#     conn = sqlite3.connect("maintenance.db")
#     c = conn.cursor()
#     c.execute("insert into users values(null,?,?)",(name,password))
#     conn.commit()
#     c.close()
#     return redirect("/login")

# log in ----------------------------------------------------------

# @app.route("/login",methods=["GET"])
# def login_get():
#     if "user_id" in session:
#         return redirect("/list")
#     else:
#         return render_template("login.html")

# @app.route("/login", methods=["POST"])
# def login_post():
#     name = request.form.get("name")
#     password = request.form.get("password")
# #     # requestでHTML側からデータを受け取る
    
#     conn = sqlite3.connect("maintenance.db")
#     c = conn.cursor()
#     c.execute("select id from users where name = ? and password = ?", (name,password))
#     user_id = c.fetchone()
#     c.close()

# # id取れたかどうかで条件分岐

#     if user_id is None:
#         return render_template("login.html")
#     else:
#         session["user_id"] = user_id[0]
#     #     # クッキーをここで設定
    
    # return redirect("/list")

# ログアウト-----------------------------------------------------------------
# @app.route("/logout")
# def logout():
#     session.pop("user_id", None)
#     return redirect("/login")

#404ページ
@app.errorhandler(404)
def not_found(error):
    return "ページが見つかりません"

#おまじない
if __name__ == "__main__":
    # Flaskが持っている開発用サーバーを実行します。
    app.run(debug=False)
    # app.run(debug=True)