
from time import sleep

class thruster:

    def __init__(self, address, location, orientation, state=0, led_status=0) -> None:
        self.address = address
        self.location = location
        self.orientation = orientation
        self.state = state
        self.led_status = led_status

    def impulse(self, solinoid):
        """Fires the solinoid as quick as possible
        
        Args: 
            solinoid - which solinoid you want to fire. Depends on Orientation of Solinoids.
            Horizontal (Left, Right) or Vertiacal (Top, Bottom).
                0 = Left or Bottom
                1 = Top or Right
        
        """
        bus.write_byte_data(self.address, solinoid, 2)
        sleep(0.5)
    
    def open(self, solinoid):
        """Leaves solinoid open indefinedtly untill otherwise closed"""
        bus.write_byte_data(self.address, solinoid, 1)
        sleep(0.5)
    
    def close(self, solinoid):
        """Leaves solinoid closed indefinedtly untill otherwise opened"""
        bus.write_byte_data(self.address, solinoid, 0)
        sleep(0.5)


thruster1 = thruster("0x08", "center", "horizontal")
thruster2 = thruster("0x09", "bottom left", "vertical")

while True:

    for i in range(50):
        thruster1.impulse(1)
        print("Fire")
        thruster1.open(1)
        sleep(3)
        thruster1.close(1)
