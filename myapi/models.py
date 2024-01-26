from django.db import models

from django.db import models

class UserRegistration(models.Model):
    ADMIN = 1
    DRIVER = 2
    USER = 3

    ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (DRIVER, 'Driver'),
        (USER, 'User')
    )

    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=200)
    date_joined = models.DateTimeField(auto_now_add=True ,null=True)
    is_active = models.BooleanField(default=True)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=USER)
    DriverId=models.CharField(max_length=20,null=True)

    def __str__(self):
        return f"{self.fullname} ({self.get_role_display()})"

    


class GetTaxiForm(models.Model):
    fromaddress = models.CharField(max_length=255)
    toaddress = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=200,default=False)
    ACTION_CHOICES = [
        ('active', 'Active'),
        ('pending', 'Pending'),
        ('unActive', 'Unactive'),
        ('Complete', 'Complete'),
       
    ]
    action = models.CharField(max_length=50, choices=ACTION_CHOICES,null=True,default='pending')
    bookingId= models.CharField(max_length=200,default=False)

    def __str__(self):
        return f"{self.username} ({self.name})"



class Driver(models.Model):
    DriverName = models.CharField(max_length=200)
    DriverAddress = models.CharField(max_length=200)
    VehicleModel = models.CharField(max_length=200)
    VehicleNumber = models.CharField(max_length=20)
    SeatCapacity = models.PositiveIntegerField()
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    AmountPerKm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    SellAmount = models.DecimalField(max_digits=10, decimal_places=2)
    DriverId = models.AutoField(primary_key=True)
    bookingId=models.CharField(max_length=100,null=True)

    def __str__(self):
        return f"{self.DriverName} ({self.bookingId})"
