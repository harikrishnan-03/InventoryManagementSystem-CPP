from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings

# Create your models here.

#Login
class ManageUser(BaseUserManager):
    def createUser(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError('Invalid email address')
        email=self.normalize_email(email)
        user=self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

#Extra Fields
class UserData(AbstractBaseUser,PermissionsMixin):
    name=models.CharField(max_length=30,blank=True)
    email=models.EmailField(unique=True)
    mobileNumber=models.IntegerField()

    objects= ManageUser()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ ]

    def str(self):
        return self.email
        

# Stock
class StockDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    itemName=models.CharField(max_length=120)
    amount=models.IntegerField()
    quantity=models.IntegerField()
    dateAdded=models.DateField()
    supplier=models.CharField(max_length=120)
    supplierNo=models.IntegerField()
    supplierEmail=models.EmailField()
    image = models.ImageField(upload_to='stock/')
    class Meta:
        db_table = "StockDetails" 
    



#Supplier
class SupplierDetails(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    supplierName=models.CharField(max_length=120)
    item=models.CharField(max_length=120)
    dateAdded=models.DateField()
    email=models.EmailField()
    phoneNumber=models.IntegerField()