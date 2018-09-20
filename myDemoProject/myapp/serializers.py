from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import post

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url','name')
        
class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'
