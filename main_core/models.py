from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from pytils.translit import slugify

# mark
class Mark(models.Model):
    name = models.CharField("Mark name", max_length=100)

    def __str__(self):
        return self.name

# model
class MarkModel(models.Model):
    name = models.CharField("Model", max_length=100)

    class Meta:
        verbose_name = "Model"
        verbose_name_plural = "Models"

    def __str__(self):
        return self.name

# user registered car
class UserCar(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name="Author")
    mark = models.CharField("Mark", max_length=100)
    model = models.CharField("Model", max_length=100)
    year = models.IntegerField("Year")
    photo = models.ImageField("Car image", upload_to="user/cars/")
    created_at = models.DateTimeField("Created at", default=datetime.now)
    slug = models.SlugField(unique=True, blank=True, editable=False)

    def __str__(self):
        return f"{self.pk} - {self.mark}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.mark)
        super().save(*args, **kwargs)

# user history
class History(models.Model):
    user = models.ForeignKey(User, models.CASCADE, verbose_name="Author")
    car = models.ForeignKey(UserCar, models.CASCADE, verbose_name="Car")
    note = models.TextField("Note", null=True, blank=True)
    image = models.ImageField("Image", upload_to="user/histories/", null=True, blank=True)
    created_at = models.DateTimeField("Created at", default=datetime.now)

    def __str__(self):
        return f"{self.pk} - {self.user.username}"
