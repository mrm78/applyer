from apscheduler.schedulers.background import BackgroundScheduler
from .currency_api import get

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(get, 'interval', minutes=30)
    scheduler.start()