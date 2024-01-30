from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login
from .models import Student

class loginView(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        
class JoinUsView(View):
    def get(self, request):
        user = request.user
        return render(request, "join_us.html", {'user': user})
    

    def post(self, request, *args, **kwargs):
        print("post request")
        print(request.POST)

        if request.method == 'POST':
            student_data = {
                'first_name': request.POST.get('first_name'),
                'last_name': request.POST.get('last_name'),
                'email': request.POST.get('email'),
                'dob': request.POST.get('dob'),
                'class_level': request.POST.get('class_level'),
                'subjects': ','.join(request.POST.getlist('subject')),  # Convert list to comma-separated string
                'gender': request.POST.get('gender'),
                'father_first_name': request.POST.get('father_first_name'),
                'father_last_name': request.POST.get('father_last_name'),
                'father_occupation': request.POST.get('father_occupation'),
                'mother_first_name': request.POST.get('mother_first_name'),
                'mother_last_name': request.POST.get('mother_last_name'),
                'mother_occupation': request.POST.get('mother_occupation'),
            }

            student = Student(**student_data)
            student.save()

            # Redirect or render success page
        return render(request, 'success.html')




class DashboardView(View):
    def get(self, request):
        students = Student.objects.all()
        for student in students:
            # Split subjects into a list
            student.subjects = student.subjects.split(',')
        return render(request, 'dashboard.html', {'students': students})
    
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
class ContantView(View):
    def get(self, request):
        return render(request, 'contact.html')