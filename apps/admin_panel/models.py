from django.db import models
from apps.index.models import Admin, User


class Course(models.Model):
    title = models.CharField(max_length=100)
    admin = models.ForeignKey(to=Admin, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Topic(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Question(models.Model):
    content = models.CharField(max_length=256)
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Answer(models.Model):
    content = models.CharField(max_length=256)
    value = models.BooleanField()
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class Result(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    topic = models.ForeignKey(to=Topic, on_delete=models.CASCADE)
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    correct_answer = models.BooleanField()
    spent_time = models.DurationField()
    pass_date = models.DateTimeField(auto_now_add=True)
    num_attempt = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.user) + ' ' + str(self.question) + ' ' + str(self.correct_answer)


class Specialization(models.Model):
    title = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.title


class StaticGraph(models.Model):
    #image = models.ImageField(verbose_name='image', upload_to='static/', null=True, blank=True)
     pass