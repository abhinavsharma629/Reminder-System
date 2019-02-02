from django.db import models

# Create your models here.


class TrucksData(models.Model):
    truck_number = models.CharField(primary_key=True, max_length=14)
    insurance_number = models.PositiveIntegerField()
    insurance_expiry = models.DateField(default=None)
    fitness_certificate_id = models.CharField(
        max_length=30, null=True, blank=True)
    fitness_certificate_expiry = models.DateField(default=None)
    image = models.ImageField(upload_to='pictures', blank=True)

    def __str__(self):  # To change the object names of the Truck table.
        return "Allianz-"+self.truck_number


class Notifications(models.Model):
    truck_number = models.CharField(max_length=14)
    insurance_id = models.PositiveIntegerField(default=1)
    fitness_id = models.CharField(max_length=30, default=-1)
    data = models.CharField(max_length=1000, default="sds")
    boolean = models.BooleanField(default=True)
