from django.urls import path
from .views import *

urlpatterns = [
    path('',home_view,name='home'),
    path('login_actress',login_view,name='login'),
    path('signup_actress',signup_view,name='signup'),
    path('logout_actress',logout_view,name='logout'),    
    path('aish',aish_view,name='aish'),
    path('emma',emma_view,name='emma'),
    path('ananya',ananya_view,name='ananya'),
    path('krish',krish_view,name='krish'),
    path('addemma',add_emma_pic,name='addemma'),
    path('addkrish',add_krish_pic,name='addkrish'),
    path('addaish',add_aish_pic,name='addaish'),
    path('addananya',add_ananya_pic,name='addananya'),
    
]
