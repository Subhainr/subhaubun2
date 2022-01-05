from django.db import models
from django.utils import timezone

class TaskML(models.Model):
    email= models.EmailField(max_length = 254)
    pclass = models.IntegerField()
    sex = models.IntegerField()
    age = models.IntegerField()
    sibsp = models.IntegerField()
    parch = models.IntegerField()
    fare = models.FloatField()
    embarked = models.IntegerField()
    title = models.IntegerField()
    time_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return  "%s %d %d %d %d %d %d %d %d" %(self.email,self.pclass,self.sex,self.age,self.sibsp,self.parch,self.fare,self.embarked,self.title)
