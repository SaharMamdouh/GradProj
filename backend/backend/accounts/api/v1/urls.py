#task n121

from django.urls import path
from .views import list_user , list_board , list_pin , list_savedpin

urlpatterns = [
path('list/<int:id>',list_user,name='get-data'),
path('board/<int:id>',list_board,name='get-board'),
path('pin/<int:id>',list_pin,name='get-pin'),
path('save/<int:id>',list_savedpin,name='get-savedpin'),
]



#task #
