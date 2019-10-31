from celery import Celery
from celery.schedules import crontab


def configure_celery(app):
    celery = Celery(
        'online—inspection-new',
        broker='redis://10.50.255.104:6379/1',
        backend='redis://10.50.255.104:6379/1',
    )
    celery.conf.timezone = 'Asia/Shanghai'
    celery.conf.beat_schedule = {
        'online-inspection': {
            'task': 'src.mainProgram.run.start',
            'schedule': crontab(minute=30)
        },
    }
    celery.conf.ONCE = {
        'backend': 'celery_once.backends.Redis',
        'settings': {
            'url': 'redis://10.50.255.104:6379/1',
            'default_timeout': 5 * 60
        }
    }

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery
