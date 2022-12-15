from django.shortcuts import render
import mysql.connector as sql


em = ''
pw = ''
# Create your views here.
def login_func(request):
    global em, pw
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", password="port", database="website")
        curser=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pw=value
        c="select * from users where email='{}' and password='{}'".format(em, pw)
        curser.execute(c)
        t=tuple(curser.fetchall())
        if t==():
            return render(request, 'error.html')
        else:
            return render(request, 'welcome.html')
    
    return render(request, "loginPage.html")
