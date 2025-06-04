import time
from plyer import notification

time_hour = float(input("Set the hours after you want to drink  water "))
while True:
    time.sleep(3600 * time_hour)
    notification.notify(
        title="Water", 
        message="you should drink water",
        timeout=2)