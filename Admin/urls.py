from django.urls import path,include
from Admin import views
app_name="Admin"

urlpatterns = [

    path('Homepage/',views.Homepage,name='Homepage'),   
    path('main/',views.main,name='main'),   


    path('district/',views.district,name='district'),   
    path('deletedistrict/<int:did>',views.DeleteDistrict,name="DeleteDistrict"),
    path('updatedistrict/<int:uid>',views.UpdateDistrict,name="UpdateDistrict"),

    path('category/',views.category,name='category'),
    path('Deletecategory/<int:did>',views.DeleteCategory,name="DeleteCategory"),
    path('UpdateCategory/<int:uid>',views.UpdateCategory,name="UpdateCategory"),

    path('details/',views.details,name='details'),
    path('DeleteDetails/<int:did>',views.DeleteDetails,name="DeleteDetails"),
    path('UpdateDetails/<int:uid>',views.UpdateDetails,name="UpdateDetails"),


    path('Brand/',views.Brand,name='Brand'),
    path('DeleteBrand/<int:did>',views.DeleteBrand,name="DeleteBrand"),

    path('Place/',views.Place,name='Place'),
    path('Subcategory/',views.Subcategory,name='Subcategory'),





 
]

