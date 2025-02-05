

from django.db import models
from datetime import date
from multiselectfield import MultiSelectField

class Post(models.Model):
    # Weather choices
    WEATHER_CHOICES = (
        ('Sunny', 'Sunny'),
        ('Windy', 'Windy'),
        ('Rainy', 'Rainy'),
        ('Snowy', 'Snowy'),
        ('Foggy', 'Foggy'),
        ('Cloudy', 'Cloudy'),
        ('Stormy', 'Stormy'),
    )

    # Mood choices
    MOOD_CHOICES = (
        ('HAPPY', 'Happy'),
        ('SAD', 'Sad'),
        ('EXCITED', 'Excited'),
        ('FURIOUS', 'Furious'),
        ('DEPRESSED', 'Depressed'),
        ('EXHAUSTED', 'Exhausted'),
        ('FRIGHTENED', 'Frightened'),
        ('RELAXED', 'Relaxed'),
        ('SURPRISED', 'Surprised'),
        ('ANGRY', 'Angry'),
        ('NERVOUS', 'Nervous'),
        ('LONELY', 'Lonely'),
        ('JEALOUS', 'Jealous'),
        ('SHY', 'Shy'),
        ('UPSET', 'Upset'),
        ('DISGUSTED', 'Disgusted'),
    )

    # Fields
    date = models.DateField(default=date.today)
    weather = models.CharField(max_length=20, choices=WEATHER_CHOICES, default='Sunny')
    mood = MultiSelectField(choices=MOOD_CHOICES)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()

    # Meta options
    class Meta:
        ordering = ['-date']

    # Methods
    def save_post(self):
        self.save()

    def __str__(self):
        return self.title
