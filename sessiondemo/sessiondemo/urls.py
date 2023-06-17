from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show/', views.showsession),
    path('add/', views.addsession),
    path('counter/',views.sessioncounter),
    path('mcq/',views.mcq),
    path('counterquestion/',views.question),
    # path('scoreresult/',views.scoreresult),
    path('boot/',views.boot),
path('', views.home)
]
