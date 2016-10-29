from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject)

    def __str__(self):
        return self.name


class Option(models.Model):
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    image = models.ImageField(upload_to='problems', null=True, blank=True)

    def __str__(self):
        return self.text


# To VTA: Please add comments to this model, slightly unclear as to what the attributes are for -NJ
class Question(models.Model):
    text = models.TextField()
    details = models.TextField()
    review = models.TextField()
    options = models.ManyToManyField(Option)
    image = models.ImageField(upload_to='problem', null=True, blank=True)

    def __str__(self):
        return self.text


class Quiz(models.Model):
    name = models.CharField(max_length=200)
    is_compulsory = models.BooleanField(default=False)
    topics = models.ManyToManyField(Topic)
    questions = models.ManyToManyField(Question)
    length = models.IntegerField()
    image = models.ImageField(upload_to='quizzes', null=True, blank=True)

    def __str__(self):
        return self.name


class Answer(models.Model):
    quiz = models.ForeignKey(Quiz)
    question = models.ForeignKey(Question)
    option = models.ForeignKey(Option)

    def __str__(self):
        return self.option.__str__()
