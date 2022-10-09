from django.db import models


class Quiz(models.Model):
    topic = models.IntegerField()
    student = models.IntegerField()
    score = models.FloatField()

    def __str__(self):
        return f"Topic: {self.topic}, Student: {self.student}, Score: {self.score}"
