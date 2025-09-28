from django.db import models

class Correct(models.Model):
    word=models.CharField()
    def __str__(self):
        return self.word

class Incorrect(models.Model):
    word=models.CharField()
    correct=models.ForeignKey(Correct, on_delete=models.CASCADE)
    def __str__(self):
        return self.word
# Create your models here.
