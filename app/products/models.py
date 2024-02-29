from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    min_group_size = models.IntegerField(default=5)
    max_group_size = models.IntegerField(default=20)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='groups')
    students = models.ManyToManyField(User, related_name='user_groups')

    def __str__(self):
        return self.name


class UserProductAccess(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    access_granted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
