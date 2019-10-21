import multiprocessing
import gevent.monkey
gevent.monkey.patch_all()

bind = '0.0.0.0:1322'

workers = 8

worker_class = 'gunicorn.workers.ggevent.GeventWorker'

x_forwarded_for_header = 'X-FORWARDED-FOR'