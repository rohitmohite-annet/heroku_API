import datetime
import time


# a job scheduled to run every 10 seconds
while(True):
    print("------------------------ Added at : "+time.ctime()+"------------------------")
    time.sleep(30)  # 10 seconds.
    print(datetime.now())

