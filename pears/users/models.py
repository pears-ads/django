from django.db import models
import uuid

class user(models.Model):
    
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_user_data = models.ForeignKey("user_data", on_delete=models.CASCADE)
    email = models.EmailField( max_length=254)
    mobile = models.PositiveIntegerField()
    password = models.CharField( max_length=200)
    Type = models.CharField( max_length=50)
    Extra = models.CharField( max_length=100)

class user_data(models.Model):
    id_user = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField( max_length=50)
    dob = models.DateField()
    gender = models.CharField( max_length=10)
    Lat = models.CharField( max_length=50)
    Long = models.CharField( max_length=50)
    device = models.CharField( max_length=1000)