from django.shortcuts import render,redirect
from .forms import UserForm, LoginAuthentication
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from . models import *
from django.db.models import Q

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
    
@login_required(login_url="logIn")
def dashboard(request):
    return render(request,"Dashboard.html")
    
@login_required(login_url="logIn")
def stockAdd(request):
    return render(request,'StockAdd.html')
    
    
@login_required(login_url="logIn")
def stockAddForm(request):
    if request.method=='POST':
        print("Form Enter")
        currentUser=request.user
        itemName=request.POST['itemName']
        amount=request.POST['amount']
        quantity=request.POST['quantity']
        dateAdded=request.POST['dateAdded']
        supplier=request.POST['supplier']
        supplierNo=request.POST['supplierNo']
        supplierEmail=request.POST['supplierEmail']
        image = request.FILES.get('image')  
        saveStock=StockDetails(user=currentUser,itemName=itemName,amount=amount,quantity=quantity,dateAdded=dateAdded,supplier=supplier,supplierNo=supplierNo,supplierEmail=supplierEmail,image=image)
        saveStock.save()
        return redirect('stockDashboard')
        
@login_required(login_url="logIn")
def profile(request):
    return render(request,"Profile.html")
 
@login_required(login_url="logIn")    
def lowStockList(request):
    currentUser=request.user
    lowStockList=StockDetails.objects.filter(Q(user=currentUser) & Q(quantity__lt=100))
    return render(request, 'LowStockList.html', {'lowStockList': lowStockList})

@login_required(login_url="logIn")    
def stockList(request):
    currentUser=request.user
    stockList=StockDetails.objects.filter(user=currentUser)
    print(stockList)
    print(currentUser)
    return render(request,"StockList.html",{'stockList':stockList}) 

@login_required(login_url="logIn")
def stockDashboard(request):
    return render(request,"StockDashboard.html")
 
@login_required(login_url="logIn")   
def stockModify(request):
    action = request.GET.get('action')
    
    currentUser=request.user
    stockList=StockDetails.objects.filter(user=currentUser)
    print(stockList)
    print(currentUser)
    return render(request,"StockModify.html",{'stockList':stockList,'action': action}) 

@login_required(login_url="logIn")
def stockUpdate(request,id):
    stockToUpdate=StockDetails.objects.get(id=id)
    dateAdded = stockToUpdate.dateAdded
    return render(request,"StockUpdate.html",{'id':stockToUpdate,'dateAdded':dateAdded})

@login_required(login_url="logIn")
def stockUpdateForm(request,id):
        if request.method=='POST':
            stockToUpdate=StockDetails.objects.get(id=id)
            stockToUpdate.user=request.user
            stockToUpdate.itemName=request.POST['itemName']
            stockToUpdate.amount=request.POST['amount']
            stockToUpdate.quantity=request.POST['quantity']
            stockToUpdate.dateAdded=request.POST['dateAdded']
            stockToUpdate.supplier=request.POST['supplier']
            stockToUpdate.supplierNo=request.POST['supplierNo']
            stockToUpdate.supplierEmail=request.POST['supplierEmail']
            stockToUpdate.image=request.FILES['image']
            stockToUpdate.save()
        return redirect('stockDashboard')
        
@login_required(login_url="logIn")
def stockDelete(request,id):
    stockToDelete=StockDetails.objects.get(id=id)
    stockToDelete.delete()
    return redirect('stockDashboard')

@login_required(login_url="logIn")
def supplierList(request):
    currentUser=request.user
    supplierList=SupplierDetails.objects.filter(user=currentUser)
    print(supplierList)
    print(currentUser)
    return render(request,"SupplierList.html",{'supplierList':supplierList}) 

@login_required(login_url="logIn")
def supplierDashboard(request):
    return render(request,"SupplierDashboard.html")

@login_required(login_url="logIn")
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