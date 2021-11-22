from .serializers import UserProfile , UserBoard , SavedPins , Saved_Pins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from accounts.models import User
from pins.models import Board , Save , Pin

@api_view(['GET'])
def list_user(request,id):
    users=User.objects.filter(id=id)
    Serialzed_data = UserProfile(instance=users,many=True)
    return Response(data=Serialzed_data.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def list_board(request,id):
    boards = Board.objects.all()
    Serialzed_data = UserBoard(boards,many=True)
    return Response(data=Serialzed_data.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def list_pin(request,id):
    saved_pins = Pin.objects.filter(id=id)
    Serialzed_data = SavedPins(saved_pins,many=True)
    return Response(data=Serialzed_data.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def list_savedpin(request,id):
    saved_pins = User.objects.filter(id=id)
    Serialzed_data = Saved_Pins(saved_pins,many=True)
    return Response(data=Serialzed_data.data,status=status.HTTP_200_OK)


# @api_view(['GET'])
# #@authentication_classes([TokenAuthentication]) already defined in setting in default authentication type
# def logout(request):
#     request.user.auth_token.delete()
#     return Response({"message":"logout done successfully"})






#sign in
# request has username, password 
# respond with token


#sing up


