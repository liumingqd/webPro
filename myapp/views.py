from django.shortcuts import render
from django.http import HttpResponse
import pymysql
# Create your views here.
def first(request):
    return HttpResponse("welcome")

def list(request):
    conn=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1234',
        db='coursemanage',
        charset='utf8',
    )
    mycursor=conn.cursor(cursor=pymysql.cursors.DictCursor)
    data=[("201441100003","池小薇","1998/03/04","100"),("201441100006","张华","1998/05/04","100"),("201441100004","杨晓们","1998/04/04","100"),]
    mysql="INSERT INTO student(stuid,stuname,stubirthday,departmentid) values (%s,%s,%s,%s)"
    mycursor.executemany(mysql,data)
    # print(mycursor.rowcount)
    conn.commit()
    print(mycursor.fetchall())
    return render(request,"list.html")