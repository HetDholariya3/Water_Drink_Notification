import time
from plyer import notification
import logging
from datetime import datetime
import winsound 

logging.basicConfig(filename="water_reminder_log.txt", level=logging.INFO, format="%(asctime)s - Reminder Triggered")

user_input = input("Enter the reminder time (YYYY-MM-DD HH:MM): ").strip()

try:
    target_time = datetime.strptime(user_input, "%Y-%m-%d %H:%M")
except ValueError:
    print("Invalid format. Please enter time in 'YYYY-MM-DD HH:MM'")
    exit()

print(f"Reminder set for {target_time}. Waiting...")

while True:
    now = datetime.now()
    if now >= target_time:
        winsound.Beep(1000, 1000)

        # Show notification
        notification.notify(
            title="Water Reminder",
            message="Time to drink water!",
            timeout=10
        )

        
        logging.info("Water reminder triggered at specific time.")
        break

    time.sleep(10) 
