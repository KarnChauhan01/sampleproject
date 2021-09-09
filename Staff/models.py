import django
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save

class User(AbstractUser):
    is_owner = models.BooleanField(default=False,null=True)
    is_member = models.BooleanField(default=False,null=True)

    

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    phone_number = models.IntegerField()

    class Meta:

        permissions = (
            ("can_start_customer","can start customer"),
            ("can_update_customer","can update customer"),
            ("can_remove_customer","can remove customer"),
        )
@receiver(post_save,sender=User)
def update_customer_signal(sender,instance,created,**kwrgs):
    if created:
        Customer.objects.create(user=instance)
        instance.customer.save()