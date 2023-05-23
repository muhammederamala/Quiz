

from django.db import models
from django.utils import timezone

class quiz_model(models.Model):
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    right_answer_index = models.IntegerField()
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default='inactive')

    def update_status(self):
        now = timezone.now()
        if now < self.start_date:
            self.status = 'inactive'
        elif now >= self.start_date and now <= self.end_date:
            self.status = 'active'
        else:
            self.status = 'finished'
        self.save()

    def __str__(self):
        return self.question
