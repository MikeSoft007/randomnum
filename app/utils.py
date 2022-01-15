# Import statement
from app import mongo
from datetime import datetime, date, timedelta
import uuid

# mongo collection
mongo_data = mongo.db.randapi

#funtion to get current date and time of data geeration
def nigerian_time():
    now = datetime.utcnow() + timedelta(hours=1)
    today = date.today()
    d2 = today.strftime("%Y-%m-%d")
    tm = now.strftime("%H:%M:%S%p")
    return d2 + ' ' + 'at' + ' ' + tm
