import mysql.connector
from data.user import User

def opendb():
  mydb = mysql.connector.connect(
    host="52.17.234.15",
    user="root",
    passwd="4",
    database="chatbot"
  )
  return mydb

def getuserid(phoneno):
  mydb = opendb()
  mycursor = mydb.cursor()
  mycursor.execute("SELECT id,is_validated FROM whatsapp_users where phoneno='" + phoneno + "'")
  myresult = mycursor.fetchall()
  u = User(-1,0)
  userid =-1
  for x in myresult:  
     print(x[0])
     u.id = x[0]
     u.isvalidated = x[1]
     userid=x
  mydb.close()
  return u

def updateuserasvalid(val):
  mydb = opendb()
  mycursor = mydb.cursor()
  sql = "update whatsapp_users set is_validated=1 where  phoneno='" + val + "'"
  print(val)
  mycursor.execute(sql)
  #val = ("John", "Highway 21")
  mydb.commit()
  cnt = mycursor.rowcount
  print(mycursor.rowcount, "record commited.")
  mydb.close()
  return cnt

def insertuser(val):
  mydb = opendb()
  mycursor = mydb.cursor()
  sql = "INSERT INTO whatsapp_users (first_name, last_name,phoneno) VALUES (%s, %s, %s)"
  print(val)
  mycursor.execute(sql, val)
  #val = ("John", "Highway 21")
  mydb.commit()
  cnt = mycursor.rowcount
  print(mycursor.rowcount, "record inserted.")
  mydb.close()
  return cnt
