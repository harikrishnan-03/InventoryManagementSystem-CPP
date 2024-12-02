from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('',views.homePage,name="homePage"),
    path('dashboard',views.dashboard,name="dashboard"),
    
    path('login',views.logIn,name="logIn"), 
    path('logout',views.logOut,name="logOut"),
    
    path('signup',views.signUp,name="signUp"),
    
    path('profile',views.profile,name="profile"),
    path('updateprofileform/<int:id>',views.updateProfileForm,name="updateProfileForm"),

    path('lowstocklist',views.lowStockList,name="lowStockList"),
    
    path('community',views.communityPage,name="communityPage"),
    path('addpost',views.addPost,name="addPost"),
    path('addpostform',views.addPostForm,name="addPostForm"),

    path('stocklist',views.stockList,name="stockList"),
    path('stockdashboard',views.stockDashboard,name="stockDashboard"),
    path('stockmodify/', views.stockModify, name='stockModify'),
    path('stockadd',views.stockAdd,name="stockAdd"),
    path('stockaddform',views.stockAddForm,name="stockAddForm"),
    path('stockupdate/<int:id>',views.stockUpdate,name="stockUpdate"),
    path('stockupdateform/<int:id>',views.stockUpdateForm,name="stockUpdateForm"),
    path('stockdelete/<int:id>',views.stockDelete,name="stockDelete"),
    
    path('supplierlist',views.supplierList,name="supplierList"),
    path('supplierdashboard',views.supplierDashboard,name="supplierDashboard"),
    path('suppliermodify/', views.supplierModify, name='supplierModify'),
    path('supplieradd',views.supplierAdd,name="supplierAdd"),
    path('supplieraddform',views.supplierAddForm,name="supplierAddForm"),
    path('supplierupdate/<int:id>',views.supplierUpdate,name="supplierUpdate"),
    path('supplierupdateform/<int:id>',views.supplierUpdateForm,name="supplierUpdateForm"),
    path('supplierdelete/<int:id>',views.supplierDelete,name="supplierDelete"),

    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('download_pdf/', views.download_pdf, name='download_pdf'),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)