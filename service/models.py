from django.db import models

# Create your models here.
work_choices = {
    "Pending","Pending",
    "In progress","In progress",
    "Completed","Completed"
}

class CustomerModel(models.Model):
    name = models.CharField(max_length=100)
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()
    vechicle_number = models.CharField(max_length=30)
    running_kilometer = models.IntegerField()
    work_status = models.CharField(choices=work_choices)
    date_created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)

class WorkModel(models.Model):
    customer = models.ForeignKey(CustomerModel,on_delete=True)
    description = models.TextField()
    amount = models.FloatField()
    date_created = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
