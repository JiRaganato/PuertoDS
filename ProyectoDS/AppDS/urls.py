from django.urls import path
from AppDS import views
urlpatterns = [
    
    path('', views.inicio), #esta era nuestra primer view
    path('packinglist', views.packinglist, name="PackingList"),
    path('informes', views.informes),
    path('choferes', views.choferes),
]