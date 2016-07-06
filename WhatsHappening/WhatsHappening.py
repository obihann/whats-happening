import time
import psutil
import pyowm
#import socket

from gmail import Mail
from arduino import Arduino


class WhatsHappening(object):
    _screenPos = 0
    _mail = Mail()
    _owm = pyowm.OWM('4c046ad50263519b269d79a1e9453a53')

    def __init__(self, port):
        self._arduino = Arduino(port)

    def update(self):
        #ip = socket.gethostbyname(socket.gethostname())

        if self._screenPos == 0:
            observation = self._owm.weather_at_place('halifax,ns')
            w = observation.get_weather()
            temp = w.get_temperature(unit='celsius')['temp']
            status = w.get_status()
            hum = w.get_humidity()

            line_one = '%s %dC %d%%' % (status, temp, hum)
            line_two = '%s' % time.strftime("%a %b %d")
            self._screenPos += 1
        else:
            line_one = 'Email:%d' % self._mail.unread_messages()
            line_two = 'RAM:%d%% CPU:%d%%' % (psutil.virtual_memory().percent, psutil.cpu_percent())
            self._screenPos = 0

        self._arduino.clear()
        self._arduino.write('%s\r\n%s' % (line_one, line_two))
