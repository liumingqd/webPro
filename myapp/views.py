from django.shortcuts import render
from django.http import HttpResponse
import pymysql
import json
# Create your views here.

#建立mysql连接
conn=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='1234',
        db='coursemanage',
        charset='utf8',
    )
mycursor=conn.cursor(cursor=pymysql.cursors.DictCursor)

def first(request):
    return HttpResponse("welcome")

def list(request):
    try:
        data=[("201441100003","池小薇","1998/03/04","100"),("201441100006","张华","1998/05/04","100"),("201441100004","杨晓们","1998/04/04","100"),]
        mysql="INSERT INTO student(stuid,stuname,stubirthday,departmentid) values (%s,%s,%s,%s)"
        mycursor.executemany(mysql,data)
        # print(mycursor.rowcount)
        conn.commit()
        print(mycursor.fetchall())
        return render(request,"list.html")
    except Exception as e:   
        return HttpResponse("错误")

#封装一个注册返回数据的函数
def Result_return(code, msg):
    '''
    code 0-正确 !=0 error
    msg 信息
    return
    '''
    data={
        "code":code,
        "msg":msg
    }
    returndata=json.dumps(data)
    return HttpResponse(returndata)

def loginHandle(request):
    username=request.POST.get("username")#接受姓名
    pwd=request.POST.get("pwd")  #接受密码
    #验证
    sql="SELECT id, password FROM user where username= %s"
    data=username
    mycursor.execute(sql,data)
    userinfo=mycursor.fetchone()
    if userinfo:
        print("存在")
        if pwd==userinfo["password"]:
            return HttpResponse("")
    else:
        print("不存在")
    
    data={
        "code": 0,
        "msg": "登录成功",
    }
    returndata=json.dumps(data)
    red=HttpResponse(returndata) 
    red.set_cookie("user","testname")
    return red  


def mytest(request):
    return HttpResponse(Result_return(1,"helllo"))