from django.db import models


class Topic(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=12)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["phone"], name="phone_unique_constraint"),
        ]

    def __str__(self) -> str:
        return self.name

    def get_quizzes(self):
        return self.quiz_set.all()


class Quiz(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='quiz_set')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_set')
    score = models.FloatField()

    def __str__(self):
        return f"Topic: {self.topic}, Student: {self.student}"
