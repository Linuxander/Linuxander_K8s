from django.db import models
import datetime

class Employer(models.Model):
    id = models.AutoField(primary_key=True)
    publish = models.BooleanField(default=False)
    title 	= models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    city 	= models.CharField(max_length=200)

    MASSACHUSETTS = 'MA'
    STATE_CHOICES = [
        (MASSACHUSETTS, 'Massachusetts')
    ]
    state = models.CharField(
        max_length=2,
        choices=STATE_CHOICES,
        default=MASSACHUSETTS,
    )

    start = models.DateField()
    end = models.DateField()
    present  = models.BooleanField(default=False)
    public	= models.BooleanField(default=False)

    class Meta:
        verbose_name = 'employer'
        verbose_name_plural = 'employers'

    def __str__(self):
        return str(self.company)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    publish = models.BooleanField(default=False)
    employers_uuid = models.ForeignKey(Employer, on_delete=models.CASCADE)
    blurb = models.CharField(max_length=255)
    public = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'

    def __str__(self):
        return str( self.employers_uuid.company + " - " + self.blurb )

class Technology(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    #To-Do: employers_multilist
    public = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'technology'
        verbose_name_plural = 'technologies'

    def __str__(self):
        return str(self.name)
