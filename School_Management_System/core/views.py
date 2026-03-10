from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Staff, Student
from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

def opening(request):
    return render(request,  'main.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'admin_login.html')
@login_required
def admin_dashboard(request):
    staff_members = Staff.objects.all()
    students = Student.objects.all()
    return render(request, 'admin_dashboard.html', {'staff_members': staff_members, 'students': students})

@login_required
def create_student(request):
    student_count = Student.objects.count() + 1
    student_id = f"student{student_count:04}"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        student_name = request.POST['student_name']
        student_fees = request.POST['student_fees']
        joining_date = request.POST['joining_date']
        profile_pictures = request.FILES.get('pic')

        user = User.objects.create_user(username=username, password=password)
        student = Student.objects.create(
            user=user,
            student_name=student_name,
            student_fees=student_fees,
            joining_date=joining_date,
            profile_picture=profile_pictures
        )
        return redirect('admin_dashboard')
    else:
        return render(request, 'create_student.html',{'uid':student_id})

def create_staff(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        staff_name = request.POST.get('staff_name')
        staff_salary = request.POST.get('staff_salary')
        staff_work = request.POST.get('staff_work')
        profile_picture = request.FILES.get('pic')

        user = User.objects.create_user(username=username, password=password)
        staff = Staff.objects.create(
            user=user,
            staff_name=staff_name,
            staff_salary=staff_salary,
            staff_work=staff_work,
            profile_picture=profile_picture
        )
        return redirect('admin_dashboard')
    else:
        return render(request, 'create_staff.html')

@login_required
def create_student(request):
    student_count = Student.objects.count() + 1
    student_id = f"student{student_count:04}"
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        student_name = request.POST['student_name']
        student_fees = request.POST['student_fees']
        joining_date = request.POST['joining_date']
        profile_pictures = request.FILES.get('pic')

        user = User.objects.create_user(username=username, password=password)
        student = Student.objects.create(
            user=user,
            student_name=student_name,
            student_fees=student_fees,
            joining_date=joining_date,
            profile_picture=profile_pictures
        )
        return redirect('admin_dashboard')
    else:
        return render(request, 'create_student.html', {'uid': student_id})

def staff_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.staff:
            login(request, user)
            return redirect('staff_dashboard')
        else:
            return render(request, 'staff_login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'staff_login.html')

def student_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.student:
            login(request, user)
            return redirect('student_dashboard')
        else:
            return render(request, 'student_login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'student_login.html')

@login_required
def staff_dashboard(request):
    return render(request, 'staff_dashboard.html')

@login_required
def student_dashboard(request):
    return render(request, 'student_dashboard.html')

def user_logout(request):
    logout(request)
    return redirect('home')

@login_required
def all_staffs(request):
    staffs = Staff.objects.all()
    return render(request, 'all_staffs.html', {'staffs': staffs})
@login_required
def update_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    if request.method == 'POST':
        staff.staff_name = request.POST.get('staff_name')
        staff.staff_salary = request.POST.get('staff_salary')
        staff.staff_work = request.POST.get('staff_work')
        staff.save()
        return redirect('all_staffs')
    else:
        return render(request, 'update_staff.html', {'staff': staff})
@login_required
def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, id=staff_id)
    if request.method == 'POST':
        staff.delete()
        staff.user.delete()
        return redirect('all_staffs')
    else:
        return render(request, 'confirm_delete_staff.html', {'staff': staff})
@login_required
def all_students(request):
    students = Student.objects.all()
    return render(request, 'all_students.html', {'students': students})
@login_required
def update_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.student_name = request.POST.get('student_name')
        student.student_fees = request.POST.get('student_fees')
        student.joining_date = request.POST.get('joining_date')
        student.save()
        return redirect('all_students')
    else:
        return render(request, 'update_student.html', {'student': student})
@login_required
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        student.user.delete()
        return redirect('all_students')
    return render(request, 'confirm_delete_student.html', {'student': student})