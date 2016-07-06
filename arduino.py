import serial


class Arduino(object):
    _screenon = b'\xFE\x42'
    _screenoff = b'\xFE\x46'
    _clear = b'\xFE\x58'
    _cursor = b'\xFE\x47'

    def __init__(self, port='/dev/tty.usbmodem1A12321'):
        self._serial = serial.Serial(port, 9600)
        self.clear()

    def clear(self):
        self._serial.write(self._clear)

    def write(self, msg):
        self._serial.write(bytearray(msg.encode('utf-8')))

    def lineOne(self):
        self._serial.write(self._cursor)
        self._serial.write(b'0')
        self._serial.write(b'0')

    def lineTwo(self):
        self._serial.write(self._cursor)
        self._serial.write(b'1')
        self._serial.write(b'1')
