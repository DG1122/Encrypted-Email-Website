from django.urls import path,include
from User import views
app_name="User"
urlpatterns = [
    path('Homepage/',views.Homepage,name='Homepage'),
    path('Myprofile/',views.Myprofile,name='Myprofile'),
    path('Editprofile/',views.Editprofile,name='Editprofile'),
    path('Changepassword/',views.Changepassword,name='Changepassword'),
    path('starred/',views.starred,name='starred'),
    path('send/',views.send,name='send'),
    path('deletemail/<int:id>',views.deletemail,name='deletemail'),
    path('deletedmail/',views.deletedmail,name='deletedmail'),
    path('deletetrashmail/<int:id>',views.deletetrashmail,name='deletetrashmail'),
    path('viewmail/<int:id>',views.viewmail,name='viewmail'),


    path('ajaxmessage/',views.ajaxmessage,name='ajaxmessage'),
    path('ajaxaddfav/',views.ajaxaddfav,name='ajaxaddfav'),
    path('logout/',views.logout,name='logout'),


]