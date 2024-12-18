from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)  
    username = models.CharField(max_length=20, unique=True)  
    name = models.CharField(max_length=30) 
    qualification = models.CharField(max_length=20) 
    email = models.EmailField(max_length=50)  
    contact = models.CharField(max_length=15)  
    address = models.CharField(max_length=35) 
    user_type = models.CharField(max_length=20)  
    created_at = models.DateField(auto_now_add=True) 
    updated_at = models.DateField(auto_now=True)  

    class Meta:
        db_table = 'users'  
