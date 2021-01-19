from django.db import models

# Create your models here.
class djangoClasses(models.Model):
    #setting the attributes for this class
    title = models.CharField(max_length=60, default="", blank=False, null=False)
    courseNumber = models.IntegerField(default="", blank=False, null=False)
    instructorName = models.CharField(max_length=60, default="", blank=False, null=False)
    duration = models.FloatField(max_length=60, default="", blank=False, null=False)

    objects = models.Manager()

    #setting how an object of this class is displayed
    def __str__(self):
        return self.title