from .serializers import UserProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Board


@api_view(['GET'])
def list_board(request, id):
    boards = Board.objects.filter(id=id)
    Serialzed_data = UserProfile(instance=boards, many=True)
    return Response(data=Serialzed_data.data, status=status.HTTP_200_OK)


from django.shortcuts import render

# Create your views here.
