import json
from datetime import datetime, timedelta
import random
import pandas as pd

#Generates test temperature and humidity data to be sent to the frontend
def send_data():

    temp_data = []
    hum_data = []
    time_data = []

    # Generate test data
    for i in range(48):
        temp = random.uniform(15, 30)
        hum = random.uniform(50, 80)
        time = (datetime.now() - timedelta(minutes=i*15)).strftime('%I:%M %p').strip()
        temp_data.append(round(temp, 1))
        hum_data.append(round(hum, 1))
        time_data.append(time)

    data = {
        'temperature': temp_data,
        'humidity': hum_data,
        'time': time_data,
    }

    # json_data = json.dumps(data)

    return data

def read_data_from_excel():
    filename = '/home/rhyno/Desktop/django-backend/smarthome/temperature_and_humidity.csv'
    df = pd.read_csv(filename)
    temperature_list = df['temperature'].tolist()
    humidity_list = df['humidity'].tolist()
    time_list = df['timestamp'].tolist()

    data_dict = {
        'temperature': temperature_list,
        'humidity': humidity_list,
        'time': time_list,
    }

    return data_dict