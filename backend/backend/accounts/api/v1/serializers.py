from rest_framework import serializers
from accounts.models import User
from pins.models import Board , Pin , Save
class UserProfile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','avatar','following','saved_img')

class UserBoardPin(serializers.ModelSerializer):
    class Meta:
        model = Pin
        fields = ('image',)

class UserBoard(serializers.ModelSerializer):
    pins=UserBoardPin(many=True)
    class Meta:
        model = Board
        fields = '__all__'

class SavedPins(serializers.ModelSerializer):
    # pin = UserBoardPin(many=True)
    class Meta:
        model = Pin
        fields = ('image','description','created_at','creator')

class Saved_Pins(serializers.ModelSerializer):
     saved_img=SavedPins(many=True)
     class Meta:
        model = User
        fields = ('saved_img',)

