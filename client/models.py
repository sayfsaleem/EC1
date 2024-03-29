from django.db import models
from froala_editor.fields import FroalaField
from django.urls import reverse
from django.utils.text import slugify

class Tag(models.Model):
    tag_name = models.CharField(max_length=90)

    def __str__(self):
        return self.tag_name

class Service(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)
    title = models.CharField(max_length=180, null=False, blank=False)
    core_line = models.CharField(max_length=400, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    image = models.ImageField(upload_to='services/')
    tags = models.ManyToManyField(Tag)  # Change ForeignKey to ManyToManyField
    description = FroalaField()  # Fixed typo in field name

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        slug = slugify(self.name)
        return reverse('Service', kwargs={'name': slug})


class Industries(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)
    title = models.CharField(max_length=180, null=False, blank=False)
    core_line = models.CharField(max_length=400, null=False, blank=False)
    square_image = models.ImageField(upload_to='services/')
    image = models.ImageField(upload_to='services/')
    tags = models.ManyToManyField(Tag)  # Change ForeignKey to ManyToManyField
    description = FroalaField()  # Fixed typo in field name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        slug = slugify(self.name)
        return reverse('Industry', kwargs={'name': slug})

class CaseStudies(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)
    slug = models.SlugField(max_length=300, null=False, blank=False)
    title = models.CharField(max_length=180, null=False, blank=False)
    core_line = models.CharField(max_length=400, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    image = models.ImageField(upload_to='services/')
    square_image = models.ImageField(upload_to='services/')
    tags = models.ManyToManyField(Tag)  # Change ForeignKey to ManyToManyField
    description = FroalaField()  # Fixed typo in field name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Case', kwargs={'name': self.slug})

class Contact(models.Model):
    name = models.CharField(max_length=90,null=False, blank=False)
    email = models.EmailField(max_length=90,null=False, blank=False)
    subject = models.TextField(max_length=200,null=False, blank=False)
    text = models.TextField(max_length=200,null=False, blank=False)

from datetime import datetime
class Job(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)
    slug = models.SlugField(max_length=90, null=False, blank=False)
    short_detail = models.CharField(max_length=200, null=False, blank=False)
    date = models.DateField(null=False, blank=False,default=datetime.now)
    active = models.BooleanField(null=False, blank=False,default=False)
    location = models.CharField(max_length=200, null=False, blank=False,default="Location")
    tags = models.ManyToManyField(Tag)
    details = FroalaField()

    class Meta:
        indexes = [
            models.Index(fields=['name']),
        ]
    def get_absolute_url(self):
        return reverse('Apply', kwargs={'name': self.slug})

class Applied_User(models.Model):
    name = models.CharField(max_length=90, null=False, blank=False)
    number = models.CharField(max_length=20, null=False, blank=False)
    email = models.CharField(max_length=90, null=False, blank=False, db_index=True)
    applied_date = models.DateField(auto_now_add=True)
    cover_letter = models.FileField(null=True, blank=True, upload_to='cover_letters/')
    resume = models.FileField(upload_to='resumes/', null=False, blank=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)  # ForeignKey linking to Job

    def __str__(self):
        return self.name  # Example representation, customize as needed
