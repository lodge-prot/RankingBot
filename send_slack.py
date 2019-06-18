import datetime
import json
import slackweb
import requests
import time
import sys

def print_datetime(prefix):
    """
    Display current time
    """
    now = datetime.datetime.now()
    print(prefix, ":" , now.strftime("%Y/%m/%d %H:%M:%S"))

def DisplayDate(func):
    """
    Decorator
    """
    def wrapper(*args, **kwargs):
        print_datetime("Start")
        func(*args, **kwargs)
        print_datetime("End  ")
    return wrapper

@DisplayDate
def send_slack(L, lc):
    """
    Notify Slack workspace "Lodge"
    """
    try:
        slack = slackweb.Slack(url=lc.slack_web_token)
        for i in range(len(L)):
            requests.post(lc.slack_web_token, data = json.dumps({
                'text': L[i],  #通知内容
                "unfurl_links": True,
                'link_names': 1,  #名前をリンク化
            }))
            if (i == 5):
                break
            time.sleep(int(lc.sleep_time))
    except requests.exceptions.InvalidSchema as exi:
        error_message = str(exi)
        print(error_message)
        sys.exit()
    except Exception as ex:
        error_message = str(ex)
        print(error_message)
        sys.exit()
