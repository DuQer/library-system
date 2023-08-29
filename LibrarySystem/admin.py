from django.contrib import admin
from .models import AddBook, IssueBook, ReturnBook, AddStudent
from django.contrib.sessions.models import Session
from .models import UserExtend


admin.site.register(Session)
admin.site.register(UserExtend)


class AddBookAdmin(admin.ModelAdmin):
    list_display = ("user", "book_id", "title", "subject", "category")


admin.site.register(AddBook, AddBookAdmin)


class IssueBookAdmin(admin.ModelAdmin):
    list_display = ("user", "book_1", "student_id")


admin.site.register(IssueBook, IssueBookAdmin)


class ReturnBookAdmin(admin.ModelAdmin):
    list_display = ("user", "book_id_2")


admin.site.register(ReturnBook, ReturnBookAdmin)


class AddStudentAdmin(admin.ModelAdmin):
    list_display = ("user", "student_name", "student_id")


admin.site.register(AddStudent, AddStudentAdmin)
