from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    post = works.objects.all()[:3]
    return render(request,'index.html',{'post':post})
def landing(request):
    if request.user.is_authenticated and not request.user.is_staff:
        if request.method == 'POST':
            name = request.POST['name']
            file = request.FILES['file']
            desc = request.POST['desc']
            users = request.user.username
            usernames = User.objects.get(username=users)
            work = works.objects.create(username=usernames,name=name,file=file,description=desc,status='Pending')
            work.save()
            messages.success(request,"Submitted successfully.")
            return redirect('landing')
        return render(request,'landing.html')
    else:
        return redirect('register')
def contact(request):
    return render(request,'contact.html')
def gallery(request):
    return render(request,'gallery.html')
def services(request):
    return render(request,'services.html')
def about(request):
    return render(request,'about.html')
def blog(request):
    return render(request,'blog.html')
def register(request):
    if "signup" in request.POST:
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        adhar=request.POST.get('adhar')
        username=request.POST.get('username')
        password=request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already registered. Try different username.")
        else:
            k=user(first_name=fname,last_name=lname,address=address,phone=phone,adhar=adhar,username=username,password=password)
            k.save()
            User.objects.create_user(username=username,password=password)
            if k:
                messages.success(request,"Registered successfully.")
            else:
                messages.warning(request,"Invalid Register details. Try again.")
    if 'signin' in request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        user_auth=authenticate(request,username=username,password=password)
        if user_auth:    
            login(request,user_auth)
            return redirect('landing')
        else:
            messages.warning(request,"Invalid login details. Try again.")  
    return render(request,'register.html')
def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('mobile')
        password=request.POST.get('pass')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('worker_vacancy')
        else:
            return redirect('login')
    return render(request,'login.html')
def signup(request):
    if request.method == 'POST':
        username=request.POST.get('mobile')
        address=request.POST.get('address')
        cat=request.POST.get('cat')
        name=request.POST.get('name')
        password=request.POST.get('pass')
        email=request.POST.get('email')
        if User.objects.filter(username=username).exists():
            messages.error(request, "User Already Exists")
            return redirect('signup')
        else:
            user = User.objects.create_user(username,email,password)
            user.is_staff =True
            user.first_name=name
            user.save()
            users= User.objects.get(username=username)
            worker = workers.objects.create(username=users,name=name,address=address,phone=username,category=cat)
            worker.save()
            return redirect('login')
    return render(request,'signup.html')
def signout(request):
    logout(request)                                                                                     
    return redirect('index')
def posts(request):
    if request.user.is_authenticated and not request.user.is_staff:
        user=request.user
        post = works.objects.filter(username=user)
        return render(request,'posts.html',{'post':post})
    else:
        return redirect('register')
def requests(request):
    if request.user.is_authenticated and not request.user.is_staff:  
        user=request.user
        # post = works.objects.filter(username=user)   
        if "reject" in request.POST:
            id = request.POST.get('uid')
            contracts=contract_details.objects.get(id=id)
            contracts.status = 'Reject'
            contracts.save()
            return redirect('requests')
        contract = contract_details.objects.filter(work__username=user,status='Pending')
        accepted = contract_details.objects.filter(work__username=user,status='Accept')
        return render(request,'requests.html',{'contract':contract,'accept':accepted})
    else:
        return redirect('register')
def worker_vacancy(request):
    if request.user.is_authenticated and request.user.is_staff:   
        work = works.objects.all()
        return render(request,'worker_vacancy.html',{'work':work})
    else:
        return redirect('login')
def apply(request):
    user=request.user
    worker = workers.objects.get(username=user)
    if request.method == 'POST':
        id = request.POST.get('id')
        payment = request.POST.get('payment')
        work = works.objects.get(id=id)
        contract = contract_details.objects.create(work=work,worker=worker,status='Pending',payment=payment)
        contract.save()
        return redirect('worker_vacancy')
def worker_apps(request):
    if request.user.is_authenticated and request.user.is_staff:   
        user=request.user
        work = contract_details.objects.filter(worker__username=user).order_by('status')
        return render(request,'worker_applies.html',{'work':work})
    else:
        return redirect('login')
def worker_logout(request):
    logout(request)                                                                                     
    return redirect('login')

def payment(request,id):
    ctrct=contract_details.objects.get(id=id)
    if "paybtn" in request.POST:
        contracts=contract_details.objects.get(id=id)
        contracts.status = 'Accept'
        contracts.save()
        return redirect('requests')
    return render(request,'payment.html',{'ctrct':ctrct})