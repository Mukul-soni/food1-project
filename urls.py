from food1 import views
from django.urls import path
app_name = 'food1'
urlpatterns=[
        
    path('Mukul/',views.MukulClassView.as_view(),name='Mukul'),#Main web page and we use class instead of function as [classname.as_view()]
    path('<int:pk>/',views.FoodDetail.as_view(),name='detail'),#Enter in particular food Item by number(Itm.id)
    path('add/',views.CreateItm.as_view(),name="create_Itm"),
    #path('update/<int:id>/',views.update_Itm,name="update_Itm"),#for edit a particular Item by Itm.id
    #path('delete/<int:id>/',views.delete_Itm,name="delete_Itm"),#for delete a particular Item by Itm.id
    ]