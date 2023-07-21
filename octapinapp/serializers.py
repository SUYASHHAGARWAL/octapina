from rest_framework import serializers
from octapinapp.models import Contact
from octapinapp.models import NewUserData
from octapinapp.models import BatchInfo
from octapinapp.models import admin
from octapinapp.models import Events

class contactserialiser(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','username','email','mobile','message')
    
class Newuserserialiser(serializers.ModelSerializer):
    class Meta:
        model = NewUserData
        fields = ('id','username','useremail','usermobile','usercity','userdob','usergender','guardiansname','guardiansphone','userschool','userclass','userpassword','userbatch','batch_purchased')

class Batchserialiser(serializers.ModelSerializer):
    class Meta:
        model = BatchInfo
        fields = ('id','BatchName','Batchfees','BatchDfees','duration','startdate')

class adminserialiser(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields = ('id','mobilenum','adminname','password')
    
class eventserialiser(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('id','eventdate','eventname','eventtime','organiser','eventlevel')