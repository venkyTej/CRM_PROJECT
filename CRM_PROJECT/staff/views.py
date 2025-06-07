from django.shortcuts import render, redirect
from .models import Staff

# Create your views here.

def staff_list(request):
    staff = Staff.objects.all()
    return render(request, "index2.html", {"allstaff":staff})

def add_staff(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        position = request.POST.get('position')
        experience = request.POST.get('experience')
        date_of_joining = request.post('date-of_joining')
        contact = request.post('contact')
        email =  request.post('email')
        image = request.FILES.get('image')

        staff = Staff(
            name = name,
            grnder =gender,
            position = position,
            experience = experience,
            date_of_joining = date_of_joining,
            contact = contact,
            email = email,
            image = image if image else None
        )
        staff.save()
        return redirect("all-staff")
    return render(request, "index2.html")

def update_staff(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        position = request.POST.get('position')
        experience = request.POST.get('experience')
        date_of_joining = request.post('date-of_joining')
        contact = request.post('contact')
        email =  request.post('email')
        image = request.FILES.get('image')

        staff = Staff(
            name = name,
            grnder =gender,
            position = position,
            experience = experience,
            date_of_joining = date_of_joining,
            contact = contact,
            email = email,
            image = image if image else None
        )
       
        
        staff.save()
        return redirect("all-staff")
    return render(request, 'index2.html',{'staff': staff} )

def delete_staff(request, id):
    staff = Staff.objects.filter(id=id)
    staff.delete()

    return redirect("all-staff")