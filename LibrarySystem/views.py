from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import IssueBook, UserExtend, AddBook, ReturnBook, AddStudent


def index(request):
    return render(request, 'index.html')


def staff(request):
    return render(request, 'staff.html')


def staff_login(request):
    if request.session.has_key('is_logged'):
        return redirect('dashboard')
    return render(request, 'staff_login.html')


def staff_sign_up(request):
    return render(request, 'staff_sign_up.html')


def dashboard(request):
    if request.session.has_key('is_logged'):
        book = AddBook.objects.all()
        return render(request,'dashboard.html', {'Book': book})
    return redirect('staff_login')


def add_book(request):
    book = AddBook.objects.all()
    return render(request, 'addbook.html', {'Book': book})


def add_book_submission(request):
    if request.session.has_key('is_logged'):
        if request.method == "POST":
            user_id = request.session["user_id"]
            user1 = User.objects.get(id=user_id)
            book_id = request.POST["book_id"]
            title = request.POST["title"]
            subject = request.POST["subject"]
            category = request.POST["category"]
            add = AddBook(user=user1, bookid=book_id, bookname=title, subject=subject, category=category)
            add.save()
            book = AddBook.objects.all()
            return render(request, 'dashboard.html', {'Book': book})
    return redirect('/')
