from django.db import models

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

    def __str__(self):
        return self.title
