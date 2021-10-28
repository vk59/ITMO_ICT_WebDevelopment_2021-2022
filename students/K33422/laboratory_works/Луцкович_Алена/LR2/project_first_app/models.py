from django.db import models

class Auto(models.Model):
    license_plate = models.CharField(max_length=15)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    color = models.CharField(max_length=30, null=True)


class Owner(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birthday = models.DateField(null=True)


class Ownership(models.Model):
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE, null=True)
    car = models.ForeignKey(Auto, on_delete=models.CASCADE, null=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True)


class DrivingLicense(models.Model):
    TYPES = (
        ('M', 'Motorcycle'),
        ('C', 'Car'),
        ('B', 'Bus'),
        ('A', 'All')
    )
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    license_number = models.CharField(max_length=10)
    category = models.CharField(max_length=10, choices=TYPES)
    issue_date = models.DateField()

