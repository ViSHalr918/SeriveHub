from django.db import models

from django.contrib.auth.models import User

# Create your models here.
work_choice = (
    "pending","pending",
    "in_progress","in_progress",
    "completed","completed"
)

class CustomerModel(models.Model):

    name = models.CharField(max_length=100)

    phone = models.CharField(max_length=15)

    email = models.EmailField()

    vechicle_number = models.CharField(max_length=30)

    running_kilometer = models.IntegerField()

    work_status = models.CharField(choices=work_choice,default="pending",max_length=100)

    created_date = models.DateField(auto_now_add=True)

    update_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

    service_advisor = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class WorkModel(models.Model):

    customer_object = models.ForeignKey(CustomerModel,on_delete=models.CASCADE)

    description = models.CharField(max_length=400)

    amount = models.FloatField()

    date_created = models.DateField(auto_now=True)

    is_active = models.BooleanField(default=False)

    created_date = models.DateField(auto_now_add=True)

    update_date = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)

