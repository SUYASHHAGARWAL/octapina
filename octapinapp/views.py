from django.shortcuts import render
from rest_framework.decorators import api_view
from octapinapp.models import Contact
from . import tuple_to_dict
from octapinapp.serializers import contactserialiser, Newuserserialiser
from django.db import connection
from django.http.response import JsonResponse
from django.shortcuts import redirect
# Create your views here.
@api_view(['GET','POST','DELETE']) 
def LandingPage(req):
    return render ( req, 'home.html')

@api_view(['GET','POST','DELETE']) 
def ContactPage(req):
    return render ( req, 'contact.html')


@api_view(['GET','POST','DELETE'])
def session(req):
    try:
        userdata = {'mobile':req.GET['mobile'],'password':req.GET['password']}
        req.session["USERDATA"] = userdata
        print("Session",userdata)
        return JsonResponse(userdata, safe=False)
    except Exception as e:
        print("Error" ,  e)


@api_view(['GET','POST','DELETE']) 
def SaveContactusdetails(req):
    try:
        if req.method == 'POST':
            contactdata = contactserialiser(data=req.data)
            if contactdata.is_valid():
                contactdata.save()
                print(contactdata)
                return render(req,"contact.html",{'message':'ok'})
            else:
                print("Else")
                return render(req,"contact.html",{'message':'error'})
    except Exception as e:
        print("Error",e)
        return render(req,"home.html")
    
@api_view(['GET','POST','DELETE'])
def Signuppage(req):
    return render(req,'login.html')

@api_view(['GET','POST','DELETE'])
def Signuppage(req):
    return render(req,'login.html')

@api_view(['GET','POST','DELETE'])
def Signupinfo(req):
    try:
        if req.method == 'POST':
            data = req.data.copy()
            l = data['username'].split(' ')
            d = data['userdob'].split('-')
            psw = l[0] + '@' + d[0]
            print(psw)
            data['userpassword'] = psw
            userdata = Newuserserialiser(data=data)
            if userdata.is_valid():
                userdata.save()
                print(userdata)
                print(userdata['userpassword'])
                return redirect("/api/loginSignup")
    except Exception as e:
        print(e)
        return render(req,"contact.html",{'message':'Message did not sent'})


@api_view(['GET', 'POST', 'DELETE'])
def CheckUserlogin(req):
    try:
        if req.method == 'GET':
            userdata = req.session["USERDATA"]
            print(2)
            print(userdata)
            mobile = req.GET.get('mobile', '')
            password = req.GET.get('password', '')
            if mobile and password:
                q = "SELECT * FROM octapinapp_newuserdata WHERE (usermobile = '{0}' OR useremail = '{0}') AND userpassword = '{1}'".format(mobile, password)
                print(q)
                cursor = connection.cursor()
                cursor.execute(q)
                record = tuple_to_dict.ParseDictMultipleRecord(cursor)
                print(record)
                # print("\n\n",record[0]['id'])
                global p
                p = record[0]['id']
                return render(req, 'Dashboard.html', {'message': 'Logged in successfully', 'record': record})
            else:
                return render(req,'contact.html',{'message':'invalid mobile or password'})
    except Exception as e:
        print("error", e)
        return redirect('/api/loginSignup',{'message':'No data found'})


@api_view(['GET','POST','DELETE'])
def AboutUsPage(req):
    return render(req,'index.html')


@api_view(['GET','POST','DELETE'])
def TestimonialsPage(req):
    return render(req,'feedback.html')


@api_view(['GET','POST','DELETE'])
def ResultsPage(req):
    return render(req,'result.html')