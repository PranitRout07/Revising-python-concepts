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