import random
import pandas as pd
import numpy as np
import time
from datetime import datetime, timedelta


temperature_interval = 60

def add_temp_and_humid_to_excel(filename):
    # Generate a random temperature value in Celsius to one decimal place precision
    temperature = round(random.uniform(0, 40), 1)
    
    # Generate a random humidity value
    humidity = random.randint(0, 100)
    
    # Get the current time
    time = (datetime.now() - timedelta(minutes=1)).strftime('%I:%M %p').strip()

    # Load the Excel file into a pandas DataFrame
    df = pd.read_excel(filename)
    
    # Add the temperature and humidity values to the DataFrame
    new_row = {'Temperature (Celsius)': temperature, 'Humidity': humidity, 'Time': time}
    df = df.append(new_row, ignore_index=True)
    
    # Write the updated DataFrame back to the Excel file
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, index=False)
    writer.save()


while True:
    # Call the function to add the temperature and humidity values to the Excel file
    add_temp_and_humid_to_excel('temperature_and_humidity.xlsx')    
    # Wait for the specified interval before calling the function again
    time.sleep(temperature_interval)
