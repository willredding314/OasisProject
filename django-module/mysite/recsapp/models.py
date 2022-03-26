from django.db import models


class MovieData(models.Model):
    hard_filters = models.JSONField()
    vector_data = models.JSONField()
    cast_data = models.JSONField()

class BinarySelection(models.Model):
    question_text = models.CharField(max_length=200)
    response = models.BooleanField()

    def __str__(self):
        return self.question_text + " - " + str(self.response)

class TextSelection(models.Model):
    question = models.CharField(max_length=200)
    response = models.CharField(max_length=200)

    def __str__(self):
        return self.question + " - " + str(self.response)


