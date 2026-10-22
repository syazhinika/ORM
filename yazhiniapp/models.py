from django.db import models
from django.contrib import admin 
class blinkit(models.Model):
    Product_name=models.CharField(max_length=20)
    Address=models.TextField()
    Email_Id=models.EmailField()
    Mobile_number=models.IntegerField()
    Availability=models.TextField()
    Rating=models.IntegerField()
    Feedback=models.TextField()
class blinkitAdmin(admin.ModelAdmin):
    list_display=["Product_name","Address","Email_Id","Mobile_number","Availability","Rating","Feedback"]

