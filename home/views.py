from django.shortcuts import render,redirect
from home.models import Hrproject
from mussu.forms import studentforms
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth

def index(request):
    return render(request,'index.html')

# def shop(request):
#     return render(request,'shop.html')

def product(request):
    return render(request,'product.html')


def place(request):
    return render(request,'place.html')

def place2(request):
    return render(request,'place2.html')

def top(request):
    return render(request,'top.html')

def campus(request):
    return render(request,'campus.html')

def checkout(request):
    return render(request,'checkout.html')

def contact(request):
    return render(request,'contact.html')
    

def user_login(request):
    if request.method=="POST":
        username = request.POST['user']
        password = request.POST['password']
        # email = request.POST['email']
        user = authenticate(request,username=username,password=password)
        # print(username)
        # print(password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request,'You are sign in')
            return redirect('/')
            
        else:
            messages.success(request,'login unsuccessful')
            return render(request,"login.html")
    else:

        return render(request,"login.html")

def user_login(request):
    if request.method=="POST":
        username = request.POST['user']
        password = request.POST['password']

        user = auth.authenticate(request,username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            request.session['userid']= username
            messages.success(request,'You are signed in')
            return redirect('profile2')
            
        else:
            messages.success(request,'login unsuccessful')
            return render(request,"login.html")
    else:
        return render(request,"login.html")
        
        
def register(request):
    if request.method=="POST":
        if request.POST.get('fullname') and request.POST.get('number') and request.POST.get('email') and request.POST.get('skills') and request.POST.get('img'):
            if User.objects.filter(username=request.POST.get('fullname')).exists():
                messages.success(request, 'you have already login')
                return render(request,'login.html')
            else:
                    saverecord = Hrproject()
                    saverecord.fullname=request.POST.get('fullname')
                    saverecord.number=request.POST.get('number')
                    saverecord.email=request.POST.get('email')
                    saverecord.skills=request.POST.get('skills')
                    saverecord.img=request.POST.get('img')
                    saverecord.save()
                    user = User.objects.create_user(username=request.POST.get('fullname'),email=request.POST.get('email'),password=request.POST.get('password'))
                    messages.success(request,'save messages successfully!!')
                    return redirect('/')
     
    else:
        return render(request,'register.html')


def logout(request):
    auth.logout(request)
    del request.session
    return render(request,'index.html')

def dashboard(request):
    dashboard=Hrproject.objects.all()
    return render(request,'dashboard.html',{'Hrproject': dashboard})

def editstudentdetails(request,id):
    displaystudent = Hrproject.objects.get(id=id)
    return render(request,'edit.html',{"Hrproject":displaystudent})

def updatestudentdetails(request,id):
    updatestudent=Hrproject.objects.get(id=id)
    form=studentforms(request.POST,request.FILES,instance=updatestudent)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Updated Successfully...')
        return render(request,'edit.html',{'Hrproject':updatestudent})
    

def delstudent(request,id):
    deletestudent= Hrproject.objects.get(id=id)
    deletestudent.delete()
    dashboard=Hrproject.objects.all()
    return render(request,'dashboard.html',{'Hrproject': dashboard})

def profile(request):
    data= Hrproject.objects.all()
    return render(request,'profile.html',{'studentdata': data})


def cdclogin(request):
    if request.method=="POST":
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if username=='CDC_GMIT':
            if user is not None:
                login(request, user)
                request.session['userid']=username
                messages.success(request,'You are sign in')
                return redirect('profile')    
            else:
                messages.success(request,'login unsuccessful')
                return render(request,"cdclogin.html")
        else:
            messages.warning(request,'invalid username')
            return render(request,"cdclogin.html")
    else:
        return render(request,"cdclogin.html")


def profile2(request):
    name=request.session.get('userid')
    studentprofile= Hrproject.objects.get(fullname=name)
    return render(request,'profile2.html',{'displaystudent':studentprofile})


def verified(request):
    if request.method=='POST':
        id=request.POST.get('id')
        student= Hrproject.objects.get(id=id)
        student.verified=request.POST.get('verified')
        student.save()
        return redirect('profile')


def verify(request,id):
    student= Hrproject.objects.get(id=id)
    return render(request,'verification.html',{'Hrproject':student})
    


