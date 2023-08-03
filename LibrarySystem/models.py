from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from datetime import datetime, timedelta


class UserExtend(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.IntegerField()

    def __str__(self):
        return self.user.username


class AddBook(models.Model):
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    book_id = CharField(max_length=10)
    title = CharField(max_length=50)
    subject = CharField(max_length=20)
    category = models.CharField(max_length=10)

    def __str__(self):
        return str(self.title)+"["+str(self.book_id)+']'


def expiration():
    return datetime.today() + timedelta(days=15)


class IssueBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_id = CharField(max_length=20)
    book_1 = models.CharField(max_length=20)
    issue_date = models.DateField(auto_now=True)
    expiration_date = models.DateField(default=expiration)

    def __str__(self):
        return self.student_id


class ReturnBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id_2 = models.CharField(max_length=20)


class AddStudent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=30)
    student_id = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name+'['+str(self.student_id)+']'
