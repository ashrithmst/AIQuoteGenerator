from django.db import models

class Quote(models.Model):
    text = models.TextField()              # The quote text
    author = models.CharField(max_length=100, default="Unknown")  # Who said it
    category = models.CharField(max_length=50, default="General") # Optional category

    def __str__(self):
        return f"{self.text[:50]} - {self.author}"
