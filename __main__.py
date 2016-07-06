import argparse
import signal
import sys
import time

from SerialPorts.SerialPorts import SerialPorts
from WhatsHappening.WhatsHappening import WhatsHappening


def signal_handler(signal, frame):
    sys.exit(0)


if __name__ == '__main__':
    signal.signal(signal.SIGTERM, signal_handler)
    signal.signal(signal.SIGINT, signal_handler)

    parser = argparse.ArgumentParser(description='Update LCD screen with useless and horrible information.')
    parser.add_argument('-p', '--port', type=str, default=False, help='Serial port for communication to sensor')

    args = parser.parse_args()
    port = args.port if args.port else SerialPorts.listPorts()

    wh = WhatsHappening(port)

    while True:
        wh.update()
        time.sleep(5)
