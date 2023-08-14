"""octapin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from octapinapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'',views.LandingPage),
    re_path(r'^api/contactuspage',views.ContactPage),
    re_path(r'^api/contactuspage',views.ContactPage),
    re_path(r'^api/contactusdetails',views.SaveContactusdetails),
    re_path(r'^api/loginSignup',views.Signuppage),
    re_path(r'^api/Sigupinfo',views.Signupinfo),
    re_path(r'^api/datainsession',views.session),
    re_path(r'^api/checkuserlogin',views.CheckUserlogin),
    re_path(r'^api/aboutuspage',views.AboutUsPage),
    re_path(r'^api/testimonialspage',views.TestimonialsPage),
    re_path(r'^api/resultspage',views.ResultsPage),
    re_path(r'^api/showadminpage',views.AdminPage),
    re_path(r'^api/registeredstudents',views.ShowRegisteredStudents),
    re_path(r'^api/unregisteredstudents',views.ShowUnRegisteredStudents),
    re_path(r'^api/batchdetails',views.Batchdetails),
    re_path(r'^api/showbatchdetails',views.batch),
    re_path(r'^api/showeventdetails',views.Events),
    re_path(r'^api/editregisteredentry',views.Editregistered),
    re_path(r'^api/EEeditregistered',views.EDITRegistered),
    re_path(r'^api/batchedit',views.BatchEdit),
    re_path(r'^api/batchsave',views.BatchEditSave),
    re_path(r'^api/eventedit',views.EventEdit),
    re_path(r'^api/qsaveeventedit',views.EventEditSave),
    re_path(r'^api/showtermsandconditions',views.ShowTnC),
    re_path(r'^api/showprivacypolicy',views.PrivacyPolicy),
    re_path(r'^api/showtestseries',views.TestSeriesPage),
    re_path(r'^api/contactmessages',views.ContactMessages),
    re_path(r'^api/contactedit',views.ContactEdit),


]
