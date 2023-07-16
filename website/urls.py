from django.urls import path
from website.views import *
app_name='website'
urlpatterns = [
path('',Index_page,name='index'),
]


