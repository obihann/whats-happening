import sys
import glob
import serial


class SerialPorts(object):
    @staticmethod
    def listPorts():
        if sys.platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            ports = glob.glob('/dev/tty[A-Za-z]*')
        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        avaliable_ports = []
        x = 1

        ports = [x for x in ports if "Bluetooth" not in x]

        if len(ports) > 1:
            print("Available serial ports:")

            for port in ports:
                try:
                    s = serial.Serial(port)
                    s.close()
                    print('%d: %s' % (x, port))
                    avaliable_ports.append(port)
                    x += 1
                except (OSError, serial.SerialException):
                    pass

            selected_port = input("Please choose a serial port: ")
            return avaliable_ports[int(selected_port) - 1]
        else:
            try:
                s = serial.Serial(ports[0])
                s.close()
            except (OSError, serial.SerialException):
                pass

            return ports[0]
