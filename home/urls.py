from django.contrib import admin
from django.urls import path,include
from home import views

admin.site.site_header = "Admin Panel"
admin.site.site_title = "Admin Dashboard"
admin.site.index_title = "Welcome to portal"


urlpatterns = [
    
    path('', views.index, name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('projects/',views.projects,name='projects'),
    path('support/',views.support,name='support'),

]