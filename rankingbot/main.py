# coding: UTF-8
import sys
import signal
import datetime
import subprocess
from urllib.parse import urlparse

def ping(url_list):
    """
    Confirm the spray target site and communication
    If it does not connect, the program ends...
    """
    for url in url_list:
        p_url = urlparse(url)
        domain = p_url.netloc
        ping = subprocess.Popen(["ping", "-c", "1", domain],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
               )
        out, error = ping.communicate()

        if error:
            print('{}'.format(error.rstrip()).replace('b\'ping', 'Network Error'))
            sys.exit()
        else:
            #print("OK" if dbg else "")
            pass

def print_datetime(prefix):
    """
    Display current time
    """
    now = datetime.datetime.now()
    print(prefix, ":" , now.strftime("%Y/%m/%d %H:%M:%S"))

def sigterm_handler(signal_number, stack_frame):
    """
    Signal processing (such as keyboard interrupts)
    """
    print_datetime("End")
    sys.exit(0)

def main(argv):
    if (len(argv) != 2):
        s =  "Usage : main.py [qiita|hatebu|tvranking]"
        print(s)
        sys.exit()

    kind_ranking = argv[1]

    if kind_ranking == "qiita":
        from modules import qiita
        qiita.main(argv)
    elif kind_ranking == "tvranking":
        from modules import tvranking
        tvranking.main(argv)
    elif kind_ranking == "hatebu":
        from modules import hatebu
        hatebu.main(argv)
    else :
        print("Unkown Ranking...")

if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigterm_handler)
    import sys
    main(sys.argv[0:])
