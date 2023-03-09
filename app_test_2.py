import mysql.connector

db = mysql.connector.connect(
    user='HajimeFujii',  # ユーザー名
    password='04fujkan11',  # パスワード
    host='localhost',  # ホスト名(IPアドレス）
    database='MyOutdoorNote'  # データベース名
)
cursor = db.cursor()

db.commit()

# データベース作成
    # cursor.execute("CREATE DATABASE MyOutdoorNote")
    # cursor.execute("SHOW DATABASES")
    # print(cursor.fetchall())

# データベース削除
    # sql = ("DROP DATABASE test_3")

# テーブル削除
    # sql = ("DROP TABLE student")

# テーブル作成
    # sql = '''
    # CREATE TABLE 2023_winter (
    #     event_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    #     date DATE NULL,
    #     event VARCHAR(50) NULL,
    #     photo VARCHAR(50) NULL,
    #     memo VARCHAR(50) NULL
    # )'''
    # cursor.execute(sql)
    # cursor.execute("SHOW TABLES")
    # print(cursor.fetchall())

# 2023_winter テーブルにデータ挿入
#     sql = ('''
#     INSERT INTO 2023_winter 
#         (date, event, photo, memo)
#     VALUES 
#         (%s, %s, %s, %s)
#     ''')
#     data = [
#         ('2023-01-07', '無意根BC', 'https://photos.app.goo.gl/R56Mk9YXKEyxBp5p9', '奈良、庄司開作、カンベ'),
#         ('2023-02-04', '円山登山', 'https://photos.app.goo.gl/Ew5i11kuspUxeUGi8', '軽アイゼン'),
#         ('2023-02-12', '円山動物園', 'https://photos.app.goo.gl/Q8tbYWdzuEmq6dXMA', 'イマコ、山本陽子')
#     ]
#     cursor.executemany(sql, data)
#     cnx.commit()

#     print(f"{cursor.rowcount} records inserted.")

#     cursor.close()

# except Exception as e:
#     print(f"Error Occurred: {e}")
# finally:
#     if cnx is not None and cnx.is_connected():
#         cnx.close()

# 2023_winter テーブルのデータをリスト
cursor.execute('select * from 2023_winter')
rows = cursor.fetchall()

for i in rows:
    print(i)

cursor.close()
db.close()