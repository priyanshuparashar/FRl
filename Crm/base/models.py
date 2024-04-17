from django.db import models

# Create your models here.


from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    is_agent = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username
    # Add other fields as needed


class PropertyType(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Property(models.Model):
    property_name=models.CharField(max_length=50,null=False, default="")
    property_type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    dimensions=models.CharField(max_length=100,null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    
    def save(self,*args, **kwargs):
        if self.property_name == "":
            self.property_name = str(self.property_type) + "property"
        super().save(*args, **kwargs)
        
    def __str__(self):
        
        return self.property_name
            
    # Add other fields as needed


class Transaction(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    buyer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=20)  # Buy, Rent, Lease
    transaction_date = models.DateField(auto_now_add=True)
    # Add other fields as needed
