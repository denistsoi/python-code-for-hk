import slack


def slack_message(channel, text, as_user):
    sc = slack.WebClient(
        token='xoxb-439490759216-834935618999-rvBQoLt5V1PiVOS7MvZiNonp')
    sc.chat_postMessage(channel=channel, text=text, as_user=as_user)
