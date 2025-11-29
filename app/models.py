from django.db import models

class Otm(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Students(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    photo=models.ImageField(upload_to='photos/%Y/%m/%d')
    email = models.EmailField(unique=False, blank=True, null=True)
    phone = models.CharField(max_length=20)
    birthday = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group = models.ForeignKey('Groups',on_delete=models.CASCADE,default=1)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.surname} {self.name}"

class Groups(models.Model):
    title = models.CharField(max_length=200)
    direction = models.CharField("Yo'nalish", max_length=200)
    otm = models.ForeignKey(Otm, on_delete=models.CASCADE,default=1)
    created_ed = models.DateTimeField(auto_now_add=True)
    updated_ed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} — {self.direction}"
