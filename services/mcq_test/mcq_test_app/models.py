from django.db import models
# from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name

    def get_questions(self):
        return self.question_set.all()

    def get_quizzes(self):
        return self.quiz_set.all()


class Question(models.Model):
    content = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return f"Question Number: {self.id}, Content: {self.content}"

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    content = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_set')

    def __str__(self):
        return f"Answer Number: {self.id}, Content: {self.content}"


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

    # score = models.FloatField()

    def __str__(self):
        return f"Topic: {self.topic}, Student: {self.student}"

