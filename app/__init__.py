
from flask import Flask, session
import app.bitcoin
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from app import configuration

database=app.db.Database()
bitcoin_object=app.bitcoin.Bitcoin()
def update_rate():
    #app.bitcoin.__init__
    #print (bitcoin_object.btc_eur)
    bitcoin_object.update()

scheduler =BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=update_rate,
    trigger=IntervalTrigger(seconds=60),
    id='update btc rate',
    name='Name',
    replace_existing=True
)
atexit.register(lambda : scheduler.shutdown())

app =Flask(__name__)
app.config['WTF_CSRF_ENABLED']=configuration.Configuration.wtf_csrf
app.config['SECRET_KEY']=configuration.Configuration.secret_key

from app import routes

