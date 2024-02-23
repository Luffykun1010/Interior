from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('landing',views.landing,name="landing"),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('services',views.services,name="services"),
    path('gallery',views.gallery,name="gallery"),
    path('blog',views.blog,name="blog"),
    path('register',views.register,name="register"),
    path('login',views.loginpage,name="login"),
    path('signup',views.signup,name="signup"),
    path('logout',views.signout,name="logout"),
    path('posts',views.posts,name="posts"),
    path('requests',views.requests,name="requests"),
    path('worker/vacancy',views.worker_vacancy,name="worker_vacancy"),
    path('worker/application',views.worker_apps,name="application"),
    path('worker/signout',views.worker_logout,name="signout"),
    path('apply',views.apply,name="apply"),
    path('payment_<int:id>',views.payment,name="payment"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
