from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
from django_countries.fields import CountryField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # This resizes the pictures uploaded
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Billinginfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    country = CountryField()
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=10, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     self.user = args['user']
    #     return super(Billinginfo, self).save(*args, **kwargs)


    # Billinginfo.objects.create(user = user3, address = fake.address(), email = fake.email(), country = fake.country(), city = fake.city(), postcode = int(fake.postcode()), phone = fake.phone_number() , first_name = fake.first_name(), last_name =  fake.last_name(), company_name = fake.company())

    def __str__(self):
        return f'{self.user.username} Billing'


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    subject = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    # models.oneToManyField()

    def __str__(self):
        return f'{self.user.username} appointment details'
