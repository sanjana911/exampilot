from django.db import models

# Create your models here.

#assessment(id, title, batch, exam_date,exam_time, duration, language,is_active)


class Assesment(models.Model):

    title = models.CharField(max_length=200)

    batch = models.CharField(max_length=200)

    exam_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField(null=True)

    duration = models.FloatField()
    LANGUAGE_CHOICES=(

        ("python","python"),
        ("java","java"),
        ("javascript","javascript"),
        ("mysql","mysql"),
        ("c","c"),
        ("c++","c++"),
        ("other","other"),

    )

    language = models.CharField(max_length=200,choices=LANGUAGE_CHOICES,default="python")

    is_active = models.BooleanField(default=True)

    def __str__(self):
        
        return self.title

