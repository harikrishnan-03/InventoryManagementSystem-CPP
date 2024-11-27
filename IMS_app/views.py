from django.shortcuts import render,redirect
from .forms import UserForm, LoginAuthentication
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from . models import *

# Create your views here.
def logIn(request):
    if request.method=='POST':
        form=LoginAuthentication(request,request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                print("login ayi")
                return redirect('dashboard')
    else:
        form=LoginAuthentication()
    return render(request,'Login.html',{'form':form})

def signUp(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('validate?')
            form.save()
            return redirect('logIn')
    else:
        form=UserForm()
    return render(request,'SignUp.html',{'form':form})

@login_required(login_url="logIn")
def logOut(request):
    logout(request)
    return redirect('homePage')
    
    
def homePage(request):
    return render(request,"HomePage.html")

def dashboard(request):
    return render(request,"Dashboard.html")
    
@login_required(login_url="logIn")
def stockAdd(request):
    return render(request,'StockAdd.html')

def profile(request):
    return render(request,"Profile.html")
    
def lowStockList(request):
    return render(request,"LowStockList.html")
    
def stockList(request):
    return render(request,"StockList.html")
    
def stockDashboard(request):
    return render(request,"StockDashboard.html")
    
def stockModify(request):
    action = request.GET.get('action')
    return render(request, 'StockModify.html', {'action': action})
    
def stockUpdate(request):
    return render(request,"StockUpdate.html")

def supplierList(request):
    currentUser=request.user
    supplierList=SupplierDetails.objects.filter(user=currentUser)
    print(supplierList)
    print(currentUser)
    return render(request,"SupplierList.html",{'supplierList':supplierList}) 

def supplierDashboard(request):
    return render(request,"SupplierDashboard.html")

def supplierModify(request):
    action = request.GET.get('action')
    
    currentUser=request.user
    supplierList=SupplierDetails.objects.filter(user=currentUser)
    print(supplierList)
    print(currentUser)
    return render(request,"SupplierModify.html",{'supplierList':supplierList,'action': action}) 

@login_required(login_url="logIn")
def supplierAdd(request):
    return render(request, 'SupplierAdd.html')
    
@login_required(login_url="logIn")
def supplierAddForm(request):
    if request.method=='POST':
        print("Form Enter")
        currentUser=request.user
        supplierName=request.POST['supplierName']
        item=request.POST['item']
        dateAdded=request.POST['dateAdded']
        email=request.POST['email']
        phoneNumber=request.POST['phoneNumber']
        saveSupplier=SupplierDetails(user=currentUser,supplierName=supplierName,item=item,dateAdded=dateAdded,email=email,phoneNumber=phoneNumber)
        saveSupplier.save()
        return redirect('supplierDashboard')
        
@login_required(login_url="logIn")
def supplierUpdate(request,id):
    supplierToUpdate=SupplierDetails.objects.get(id=id)
    dateAdded = supplierToUpdate.dateAdded
    return render(request,"SupplierUpdate.html",{'id':supplierToUpdate,'dateAdded':dateAdded})

@login_required(login_url="logIn")
def supplierUpdateForm(request,id):
        if request.method=='POST':
            supplierToUpdate=SupplierDetails.objects.get(id=id)
            supplierToUpdate.user=request.user
            supplierToUpdate.supplierName=request.POST['supplierName']
            supplierToUpdate.item=request.POST['item']
            supplierToUpdate.dateAdded=request.POST['dateAdded']
            supplierToUpdate.email=request.POST['email']
            supplierToUpdate.phoneNumber=request.POST['phoneNumber']
            supplierToUpdate.save()
        return redirect('supplierDashboard')
        
@login_required(login_url="logIn")
def supplierDelete(request,id):
        supplierToDelete=SupplierDetails.objects.get(id=id)
        supplierToDelete.delete()
        return redirect('supplierDashboard')