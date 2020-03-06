import time

from notification import message

local_time = time.localtime(time.time())

hour = getattr(local_time, "tm_hour")
minute = getattr(local_time, "tm_min")

while True:
    if hour == 12:
        print("lunch")
        message.slack_message("#testing", "lunch", False)
    elif hour == 15:
        print("miao")
        message.slack_message("#testing", "zzz", False)
    elif hour == 17:
        print("class")
        message.slack_message("#testing", "python practioner", False)

    print("purr - sleep", hour)
    time.sleep(60)
