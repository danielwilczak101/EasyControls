from smbus import SMBus
from time import sleep

bus = SMBus(1)


class thruster:

    def __init__(self, address, location=None, orientation=None, state=0, led_status=0):
        self.address = address
        self.location = location
        self.orientation = orientation
        self.state = state
        self.led_status = led_status

    def impulse(self, solinoid):
        """Fires the solinoid as quick as possible

        Args: 
            solinoid - which solinoid you want to fire. Depends on orientation of solinoids.
            Horizontal (Left, Right) or Vertiacal (Top, Bottom).
                0 = Left or Bottom
                1 = Top or Right

        """
        bus.write_byte_data(self.address, solinoid, 2)
        sleep(0.1)

    def open(self, solinoid):
        """Leaves solinoid open indefinedtly untill otherwise closed"""
        bus.write_byte_data(self.address, solinoid, 1)
        sleep(0.1)

    def close(self, solinoid):
        """Leaves solinoid closed indefinedtly untill otherwise opened"""
        bus.write_byte_data(self.address, solinoid, 0)
        sleep(0.1)


one = thruster(0x10)
two = thruster(0x11)
three = thruster(0x12)
four = thruster(0x13)
five = thruster(0x14)
six = thruster(0x15)


one.close(0)
two.close(0)
three.close(0)
four.close(0)
five.close(0)
six.close(0)

one.close(1)
two.close(1)
three.close(1)
four.close(1)
five.close(1)
six.close(1)
