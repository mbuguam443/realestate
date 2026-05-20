from django.urls import path,include
from . import views

urlpatterns = [
 
    path('',views.home,name='index'),
    path('about',views.about,name='about'),
    path('notfound',views.notfound,name='notfound'),
    path('agent_profile',views.agent_profile,name='agent_profile'),
    path('blog_post',views.blog_post,name='blog_post'),
    path('blog',views.blog,name='blog'),
    path('contact',views.contact,name='contact'),
    path('faq',views.faq,name='faq'),
    path('login',views.login,name='login'),
    path('property_details',views.property_details,name='property_details'),
    path('property',views.property,name='property'),
    path('register',views.register,name='register'),
    path('single_agent',views.single_agent,name='single_agent'),
    path('thank_you',views.thank_you,name='thank_you'),
    path('index_map',views.index_map,name='index_map'),
    path('index_parallax',views.index_parallax,name='index_parallax'),
    path('index_slideshow',views.index_slideshow,name='index_slideshow'),
    path('index_video',views.index_video,name='index_video'),
    
    
]