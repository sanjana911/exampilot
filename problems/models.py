from django.db import models
from exam.models import Assesment

# Create your models here.


class Question(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField()

    score = models.PositiveIntegerField()

    sample_input = models.TextField(null=True)

    sample_output=models.TextField(null=True)

    question_number = models.PositiveIntegerField()

    assesment = models.ForeignKey(Assesment,on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title