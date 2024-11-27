from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.homePage,name="homePage"),
    path('dashboard',views.dashboard,name="dashboard"),
    
    path('login',views.logIn,name="logIn"), 
    path('logout',views.logOut,name="logOut"),
    
    path('signup',views.signUp,name="signUp"),
    path('profile',views.profile,name="profile"),
    
    path('lowstocklist',views.lowStockList,name="lowStockList"),
    
    path('stocklist',views.stockList,name="stockList"),
    path('stockdashboard',views.stockDashboard,name="stockDashboard"),
    path('stockmodify/', views.stockModify, name='stockModify'),
    path('stockadd',views.stockAdd,name="stockAdd"),
    path('stockupdate',views.stockUpdate,name="stockUpdate"),

    path('supplierlist',views.supplierList,name="supplierList"),
    path('supplierdashboard',views.supplierDashboard,name="supplierDashboard"),
    path('suppliermodify/', views.supplierModify, name='supplierModify'),
    path('supplieradd',views.supplierAdd,name="supplierAdd"),
    path('supplieraddform',views.supplierAddForm,name="supplierAddForm"),
    path('supplierupdate/<int:id>',views.supplierUpdate,name="supplierUpdate"),
    path('supplierupdateform/<int:id>',views.supplierUpdateForm,name="supplierUpdateForm"),
    path('supplierdelete/<int:id>',views.supplierDelete,name="supplierDelete"),

]
