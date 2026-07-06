from django.db import models

class Project(models.Model):
    TYPE_CHOICES = [
        ('carte', 'Carte'),
        ('timeline', 'Chronologie'),
        ('dataviz', 'Visualisation de données'),
    ]

    titre = models.CharField(max_length=200)
    description = models.TextField()
    type_project = models.CharField(max_length=20, choices=TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.titre
    