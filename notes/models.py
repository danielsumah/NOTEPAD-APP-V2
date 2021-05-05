from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Note(models.Model):
    LABEL_CHOICES = (
        ('P', 'primary'),
        ('SE', 'secondary'),
        ('S', 'success'),
        ('D', 'danger'),
        ('W', 'warning'),
        ('I', 'info'),
        ('L', 'light'),
        ('D', 'dark'),

    )

    title = models.CharField(max_length=100)
    due_date =  models.DateTimeField()
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)
    finished = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    def get_finish_url(self):
        return reverse('finish-note-item',kwargs={'id':self.id})

    def get_delete_url(self):
        return reverse('delete-note-item',kwargs={'id':self.id})

    def get_recover_url(self):
        return reverse('recover-note-item',kwargs={'id':self.id})

