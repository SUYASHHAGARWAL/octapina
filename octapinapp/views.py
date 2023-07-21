from django.shortcuts import render
from rest_framework.decorators import api_view
from octapinapp.models import NewUserData
from octapinapp.models import BatchInfo
from octapinapp.models import Contact
from octapinapp.serializers import Newuserserialiser
from . import tuple_to_dict
from octapinapp.serializers import contactserialiser
from django.db import connection
from django.http.response import JsonResponse
from django.shortcuts import redirect
from rest_framework.response import Response
from octapinapp.models import Events as evs

# Create your views here.
@api_view(['GET','POST','DELETE']) 
def LandingPage(req):
    
    return render ( req, 'index.html')

@api_view(['GET','POST','DELETE']) 
def batch(req):
    q = "select * from octapinapp_batchinfo"
    cursor = connection.cursor()
    cursor.execute(q)
    record = tuple_to_dict.ParseDictMultipleRecord(cursor)
    print(record)
    return JsonResponse(record,safe=False)

@api_view(['GET','POST','DELETE']) 
def Events(req):
    q = "select * from octapinapp_Events"
    cursor = connection.cursor()
    cursor.execute(q)
    record = tuple_to_dict.ParseDictMultipleRecord(cursor)
    print(record)
    return JsonResponse(record,safe=False)

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
def Signupinfo(req):
    try:
        if req.method == 'POST':
            userdata = req.session.get('USERDATA',{})
            # batch = req.GET.get('batchname','')
            # print(userdata['batchname'])
            data = req.data.copy()
            l = data['username'].split(' ')
            d = data['userdob'].split('-')
            psw = l[0] + '@' + d[0]
            print(psw)
        
            # btc = userdata['batchname']
            # print(userdata['batchname'])
            # if(userdata['batchname']):
            if (userdata):
                data['batch_purchased'] = 'yes'
            else:
                data['batch_purchased'] = 'No'
            data['userpassword'] = psw
            # data['userbatch '] = btc
            user = Newuserserialiser(data=data)
            if user.is_valid():
                user.save()
                print(user)
                print(user['userpassword'])
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
                batchname = str(record[0]['userbatch'])
                l = len(batchname)
                batchff = batchname[11:l-14]
                record[0]['userbatch'] = batchff
                return render(req, 'Dashboard.html', {'record': record[0]})
            else:
                return render(req,'login.html',{'message':'invalid mobile or password'})
    except Exception as e:
        print("error", e)
        return redirect('/api/loginSignup',{'message':'No data found'})


@api_view(['GET','POST','DELETE'])
def AboutUsPage(req):
    return render(req,'about.html')


@api_view(['GET','POST','DELETE'])
def TestimonialsPage(req):
    return render(req,'feedback.html')


@api_view(['GET','POST','DELETE'])
def ResultsPage(req):
    return render(req,'result.html')

@api_view(['GET','POST','DELETE'])
def AdminPage(req):
    return render(req,'Admin.html')

@api_view(['GET','POST','DELETE'])
def ShowRegisteredStudents(req):
    try:
        if req.method == 'GET':
            print("\n\n\nNEW INTERFACE")
            q = " select * from octapinapp_newuserdata where batch_purchased = 'yes'"    
            print("this is new interface")
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("xxxxxxxxxx",records)
            if(records):
                return JsonResponse(records,safe=False)
            else:
                return render(req,"Dashboard.html")
    except Exception as e:
        print("Error" ,e)


@api_view(['GET','POST','DELETE'])
def Batchdetails(req):
    try:
        userdata = {'batchname':req.GET['batchname']}
        req.session["USERDATA"] = userdata
        print("Session",userdata)
        return JsonResponse(userdata, safe=False)
    except Exception as e:
        print("Error" ,  e)

@api_view(['GET','POST','DELETE'])
def ShowUnRegisteredStudents(req):
    try:
        if req.method == 'GET':
            q = "select * from octapinapp_newuserdata where batch_purchased = 'no' "    
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("xxxxxxxxxx",records)
            if(records):
                return JsonResponse(records,safe=False)
            else:
                return render(req,"Dashboard.html")
    except Exception as e:
        print("Error" ,e)

@api_view(['GET','POST','DELETE'])
def Editregistered(request):
    try:
        if request.method =='GET':
            print(request.GET['id'])
            q="select * from octapinapp_newuserdata where id={0}".format(request.GET['id'])
            cursor=connection.cursor()
            cursor.execute(q)
            record=tuple_to_dict.ParseDictSingleRecord(cursor)
            return render(request,'DisplayById.html',{'data':record})
    except Exception as e:
        print("Error:",e)
        # return render(request,'DisplayById.html',{'data':{}})

@api_view(['GET','POST','DELETE'])
def EDITRegistered(request):
    try:
        if request.method == 'GET':
            print(1111)
            if request.GET['btn'] == 'edit':
                    print(222)
                    print(request.GET['idbb'])
                    cat = NewUserData.objects.get(pk=request.GET['idbb'])
                    cat.username = request.GET['username']
                    cat.useremail = request.GET['useremail']
                    cat.usermobile = request.GET['usermobile']
                    cat.usercity = request.GET['usercity']
                    cat.userdob = request.GET['userdob']
                    cat.usergender = request.GET['usergender']
                    cat.guardiansname = request.GET['guardiansname']
                    cat.guardiansphone = request.GET['guardiansphone']
                    cat.userschool = request.GET['userschool']
                    cat.userclass = request.GET['userclass']
                    cat.userpassword = request.GET['userpassword']
                    cat.userbatch = request.GET['userbatch']
                    cat.batch_purchased = request.GET['batch_purchased']
                    cat.save()
                    print('\n\n\n Saved')
                    
            else:
                    cat = NewUserData.objects.get(pk=request.GET['id'])
                    cat.delete()

            return redirect('/api/showadminpage')
    except Exception as e:
        print("Error", e)
        # return redirect('/api/')

@api_view(['GET','POST','DELETE'])
def BatchEdit(req):
    try:
        if req.method =='GET':
            print(req.GET['id'])
            q="select * from octapinapp_batchinfo where id={0}".format(req.GET['id'])
            cursor=connection.cursor()
            cursor.execute(q)
            record=tuple_to_dict.ParseDictSingleRecord(cursor)
            return render(req,'BatchEdit.html',{'data':record})
    except Exception as e:
        print(e)

@api_view(['GET','POST','DELETE'])
def BatchEditSave(req):
    try:
        if req.method == 'GET':
            print(1111)
            if req.GET['btn'] == 'edit':
                    print(222)
                    print(req.GET['idbb'])
                    cat = BatchInfo.objects.get(pk=req.GET['idbb'])
                    cat.BatchName = req.GET['BatchName']
                    cat.Batchfees = req.GET['Batchfees']
                    cat.BatchDfees = req.GET['BatchDfees']
                    cat.duration = req.GET['duration']
                    cat.startdate = req.GET['startdate']
                    cat.save()
            else:
                    cat = BatchInfo.objects.get(pk=req.GET['idbb'])
                    cat.delete()
            return redirect('/api/showadminpage')
    except Exception as e:
        print("Error", e)

@api_view(['GET','POST','DELETE'])
def EventEdit(req):
    try:
        if req.method =='GET':
            print(req.GET['id'])
            q="select * from octapinapp_events where id={0}".format(req.GET['id'])
            cursor=connection.cursor()
            cursor.execute(q)
            record=tuple_to_dict.ParseDictSingleRecord(cursor)
            return render(req,'EventEdit.html',{'data':record})
    except Exception as e:
        print(e)


@api_view(['GET','POST','DELETE'])
def EventEditSave(request):
    try:
        if request.method == 'GET':
            print(1111)
            if request.GET['btn'] == 'edit':
                print(222)
                print(request.GET['idbb'])
                cat = evs.objects.get(pk=request.GET['idbb'])
                cat.eventdate = request.GET['eventdate']
                cat.eventname = request.GET['eventname']
                cat.eventtime = request.GET['eventtime']
                cat.organiser = request.GET['organiser']
                cat.eventlevel = request.GET['eventlevel']
                cat.save()
            else:
                    cat = Events.objects.get(pk=request.GET['idbb'])
                    cat.delete()
            return redirect('/api/showadminpage')
    except Exception as e:
        print("Error", e)

@api_view(['GET','POST','DELETE'])
def ShowTnC(req):
    return render(req,'terms.html')


@api_view(['GET','POST','DELETE'])
def PrivacyPolicy(req):
    return render(req,'privacypolicy.html')

@api_view(['GET','POST','DELETE'])
def TestSeriesPage(req):
    return render(req,'tests.html')

@api_view(['GET','POST','DELETE'])
def ContactEdit(req):
    try:
        if req.method == 'GET' :
            vehicle = Contact.objects.get(pk=req.GET['id'])
            vehicle.delete()
            return redirect('/api/showadminpage')
    except Exception as e:
        print(e)
        return redirect('/api/showadminpage')


@api_view(['GET','POST','DELETE'])
def ContactMessages(req):
    try:
        if req.method == 'GET':
            q = "select * from octapinapp_contact "    
            cursor = connection.cursor()
            cursor.execute(q)
            records = tuple_to_dict.ParseDictMultipleRecord(cursor)
            print("xxxxxxxxxx",records)
            if(records):
                return JsonResponse(records,safe=False)
            else:
                return render(req,"Admin.html")
    except Exception as e:
        print("Error" ,e)

