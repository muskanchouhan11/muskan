from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    
    path("",views.index,name='index'),
    # path("shop",views.shop,name='shop'),
    path("product",views.product,name='product'),
    path("checkout",views.checkout,name='checkout'),
    path("contact",views.contact,name='contact'),
    path("login",views.user_login,name='login'),
    path("logout",views.logout,name='logout'),
    path("register",views.register),
    path("dashboard",views.dashboard,name='dashboard'),
    path('edit/<int:id>',views.editstudentdetails),
    path('update/<int:id>',views.updatestudentdetails,name='updatestudentdetails'),
    path('delete/<int:id>',views.delstudent,name='delstudent'),
    path('profile',views.profile,name='profile'),
    path('cdclogin',views.cdclogin,name='cdclogin'),
    path('profile2',views.profile2,name='profile2'),
    path('place',views.place,name='place'),
    path('place2',views.place2,name='place2'),
    path('top',views.top,name='top'),
    path('campus',views.campus,name='campus'),
    path('verification',views.verified),
    path('verify/<int:id>',views.verify,name='verify'),
]

