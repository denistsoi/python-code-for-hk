import time
import toml

from notification import message

local_time = time.localtime(time.time())

hour = getattr(local_time, "tm_hour")
minute = getattr(local_time, "tm_min")


# configuration times
config = toml.load("config.toml")

lunch_time = config.get("lunch")
sleep_time = config.get("sleep")
class_time = config.get("class")

while True:
    if hour == lunch_time:
        print("lunch")
        message.slack_message("#testing", "lunch", False)
    elif hour == sleep_time:
        print("miao")
        message.slack_message("#testing", "zzz", False)
    elif hour == class_time:
        print("class")
        message.slack_message("#testing", "python practioner", False)

    print("purr - sleep", hour)
    time.sleep(60)
