from celery.schedules import crontab

imports = ('app.tasks', 'app.main.tasks')
broker_url = 'amqp://'
accept_content = ['json']
task_serializer = 'json'
result_serializer = 'json'
timezone = 'Canada/Mountain'
task_time_limit = 3000
worker_concurrency = 1
beat_schedule = {}

"""
'update_cache': {
    'task': 'app.main.tasks.update_recent_cache',
    'schedule': crontab(minute=0, hour='*/1')
}
"""
