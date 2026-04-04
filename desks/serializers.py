from django.contrib.auth import authenticate, login, logout
from rest_framework import serializers
from .models import CustomUser, Cards, City

class CardsSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cards
        fields ='__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id','username','password','email']
        extra_kwargs = {
            'password': {'write_only': True} 
        }
    

    def create(self, validated_data):
        user:CustomUser = super().create(validated_data)
        password = validated_data.get('password')
        user.set_password(password)
        user.save()
        return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True,write_only=True)

    def validate(self, attrs):
        request = self.context['request']
        username = attrs.get('username')
        password = attrs.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            attrs['user']=user
            return attrs
        else :
            raise serializers.ValidationError({"detail":"Login or password invalid"})



class HotDesksSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'