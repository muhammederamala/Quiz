from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone
from .models import quiz_model

def update_quiz_status():
    now = timezone.now()
    quizzes = quiz_model.objects.filter(start_date__lte=now, end_date__gte=now)
    quizzes.update(status='active')
    quiz_model.objects.filter(end_date__lt=now).update(status='finished')

scheduler = BackgroundScheduler()
scheduler.add_job(update_quiz_status, 'interval', seconds=10)
scheduler.start()
