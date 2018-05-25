from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    gender = serializers.ChoiceField(choices=Profile.GENDER,source='get_gender_display')
    class Meta:
        model = Profile
        fields = ('url','gender','date_of_birth')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(required=True,read_only=False)
    class Meta:
        model = User
        fields = ('url','username','email','profile')


class UserCreateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('email','username','password')

    def create(self, validated_data):
        user = User(
            email = validated_data.get('email'),
            #password= validated_data.get('password'),
            username = validated_data.get('username')
            )
        user.set_password(validated_data.get('password'))
        user.save()
        return user

