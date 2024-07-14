from django.shortcuts import render,redirect
from .models import * 

# Create your views here.
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
    context = {'allreceipes': allreceipes}
        
    return render(request,"receipes.html",context)
def delete_receipes(request,id):

    Receipe.objects.get(id=id).delete()
    return redirect("/receipes")

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