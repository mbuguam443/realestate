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
    path('login',views.login_view,name='login'),
    path('property_details/<int:pk>/',views.property_details,name='property_details'),
    path('property',views.property,name='property'),
    path('register',views.register,name='register'),
    path('single_agent',views.single_agent,name='single_agent'),
    path('thank_you',views.thank_you,name='thank_you'),
    path('index_map',views.index_map,name='index_map'),
    path('index_parallax',views.index_parallax,name='index_parallax'),
    path('index_slideshow',views.index_slideshow,name='index_slideshow'),
    path('index_video',views.index_video,name='index_video'),
    path('postproperty',views.postproperty,name='postproperty'),
    path('messagesClient',views.messagesClient,name='messagesClient'),
    path('logout', views.logout_view, name='logout'),
    path('markread/<int:pk>/',views.markread, name='markread'),
    path('gallery',views.gallery,name='gallery'),

    path('property/delete/<int:pk>/',views.delete_property,name='delete_property'),
    path('property/edit/<int:pk>/',views.edit_property,name='edit_property'),
    path('search/',views.property_search,name='property_search')
]