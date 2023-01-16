from django.shortcuts import render
from django.http import HttpResponse
import pymysql
# Create your views here.
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
    mysql="SELECT * FROM staff"
    mycursor.excute(mysql)
    print(mycursor.rowcount)