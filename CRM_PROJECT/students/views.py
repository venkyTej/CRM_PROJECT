from django.shortcuts import render, redirect
from .models import Student

# Create your views here.


def student_list(request):
    students = Student.objects.all()
    return render(request, "index1.html", {"allstudents":students})

def add_student(request):
    if request.method == "POST":
        roll_number = request.POST.get('roll_number')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        enroll_course = request.POST.get('enroll_course')
        contact = request.POST.get('contact')
        education = request.POST.get('education')
        email = request.POST.get('email')
        parent_name = request.POST.get('parent_name')
        Dob = request.POST.get('dob')  
        fees_paid = request.POST.get('fees_paid')
        date_of_joining = request.POST.get('date_of_joining')  
        image = request.FILES.get('image')

        student = Student(
            roll_number=roll_number,
            name=name,
            gender=gender,
            enroll_course=enroll_course,
            contact=contact,
            education=education,
            email=email,
            parent_name=parent_name,
            Dob=Dob,
            fees_paid=fees_paid,
            date_of_joining=date_of_joining,
            image=image if image else None
        )
        student.save()
        return redirect("all-students") 

    return render(request, "index1.html")  

def update_student(request, id):
    # student = Student.objects.get(id = id)
    if request.method == "POST":
        
        roll_number = request.POST.get('roll_number')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        enroll_course = request.POST.get('enroll_course')
        contact = request.POST.get('contact')
        education = request.POST.get('education')
        email = request.POST.get('email')
        parent_name = request.POST.get('parent_name')
        Dob = request.POST.get('dob')  
        fees_paid = request.POST.get('fees_paid')
        date_of_joining = request.POST.get('date_of_joining')  
        image = request.FILES.get('image')

        student = student (
            roll_number=roll_number,
            name=name,
            gender=gender,
            enroll_course=enroll_course,
            contact=contact,
            education=education,
            email=email,
            parent_name=parent_name,
            Dob=Dob,
            fees_paid=fees_paid,
            date_of_joining=date_of_joining,
            image=image if image else None
        )
        student.save()
        return redirect("all-students")
    return render(request, 'index1.html',{'student':'student'} )

def delete_student(request, id):
    student = Student.objects.filter(id=id)
    student.delete()

    return redirect("all-students")