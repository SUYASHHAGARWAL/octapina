from rest_framework import serializers
from octapinapp.models import Contact
from octapinapp.models import NewUserData

class contactserialiser(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id','username','email','mobile','message')
    
class Newuserserialiser(serializers.ModelSerializer):
    class Meta:
        model = NewUserData
        fields = ('id','username','useremail','usermobile','usercity','userdob','usergender','guardiansname','guardiansphone','userschool','userclass','userpassword')