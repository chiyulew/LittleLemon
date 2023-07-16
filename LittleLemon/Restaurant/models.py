from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField()
    bookingDate = models.DateTimeField()
    
    
class Menu(models.Model):
    id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    inventory = models.SmallIntegerField(default=0)
    
    def get_item(self):
        return f'{self.title}:{str(self.price)}'