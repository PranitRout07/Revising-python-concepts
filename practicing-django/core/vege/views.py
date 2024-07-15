from django.shortcuts import render,redirect
from .models import * 
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login/")
def receipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("name")
        receipe_description = data.get("description")
        receipe_image = request.FILES.get('image')

        # print(receipe_name,receipe_description,receipe_image)
        Receipe.objects.create(
            name = receipe_name,
            description = receipe_description,
            image=receipe_image
        )

        return redirect("/receipes")
    

    allreceipes = Receipe.objects.all()
    if request.GET.get('search'):
        print(request.GET.get('search'))
        allreceipes = allreceipes.filter(name__icontains = request.GET.get('search'))
    context = {'allreceipes': allreceipes}
        
    return render(request,"receipes.html",context)
@login_required(login_url="/login/")
def delete_receipes(request,id):

    Receipe.objects.get(id=id).delete()
    return redirect("/receipes")
@login_required(login_url="/login/")
def update_receipes(request,id):
    querryResult = Receipe.objects.get(id=id)
    
    context = {'receipe': querryResult}
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get("name")
        receipe_description = data.get("description")
        receipe_image = request.FILES.get('image')

        # print(receipe_name,receipe_description,receipe_image)
        querryResult.name = receipe_name
        querryResult.description = receipe_description
        if receipe_image:
            querryResult.image = receipe_image
        querryResult.save()
        return redirect("/receipes")
    return render(request,"update_receipe.html",context)


# LOGIN AND REGISTER

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password,"details of login")
        if not User.objects.filter(username = username).exists():
            messages.info(request,"Username doesn't exists!")
            return redirect('/login/')
        user = authenticate(username=username,password=password)
        if user is None:
            messages.info(request,'Invalid credentials!')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/receipes/')
    return render(request,"login.html")
def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,'Username is taken!')
            return redirect('/register/')
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)  #if directly passed then it will not encrypt so thats why it is formed like this outside of the User block
        user.save()
        messages.info(request,"Account created successfully!")
        return redirect("/register/")
    return render(request,"register.html")
def logout_page(request):
    logout(request)
    return redirect("/login/")