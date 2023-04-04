import pywhatkit
import schedule
import time
import random


receiver_number = "+123456789"  # whatever phone nuber
messages = ["Message 1", "Message 2", "Message 3"] #list of nice messages for someone

def send_message():
    message = random.choice(messages)

    time.sleep(10)

    pywhatkit.sendwhatmsg(receiver_number, message, 8, 00)


schedule.every().day.at("08:00").do(send_message)


while True:
    schedule.run_pending()
    time.sleep(1)
