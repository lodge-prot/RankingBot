# coding: UTF-8
import sys
import signal
import datetime

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
        s = '''
Usage : main.py [qiita|hatebu|tvranking]
        '''
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
        pass
    else :
        print("Unkown Ranking...")

if __name__ == '__main__':
    signal.signal(signal.SIGINT, sigterm_handler)
    import sys
    main(sys.argv[0:])
