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
    mycursor=conn.cursor()
    mysql="SELECT * FROM student"
    mycursor.execute(mysql)
    # print(mycursor.rowcount)
    print(mycursor.fetchall())
    return render(request,"list.html")