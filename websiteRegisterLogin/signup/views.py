from django.shortcuts import render
import mysql.connector as sql


fn = ''
ln = ''
ge = ''
em = ''
pw = ''
# Create your views here.
def signup_func(request):
    global fn, ln, ge, em, pw
    if request.method=="POST":
        m=sql.connect(host="localhost", user="root", password="port", database="website")
        curser=m.cursor()
        d=request.POST
        for key, value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="gender":
                ge=value
            if key=="email":
                em=value
            if key=="password":
                pw=value
        c="insert into users Values('{}', '{}', '{}', '{}', '{}')".format(fn, ln, ge, em, pw)
        curser.execute(c)
        m.commit()
    
    return render(request, "signupPage.html")
