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
        sleep(0.05)
    
    def open(self, solinoid):
        """Leaves solinoid open indefinedtly untill otherwise closed"""
        bus.write_byte_data(self.address, solinoid, 1)
        sleep(0.1)
    
    def close(self, solinoid):
        """Leaves solinoid closed indefinedtly untill otherwise opened"""
        bus.write_byte_data(self.address, solinoid, 0)
        sleep(0.1)


thruster = thruster(0x10)
#thruster1 = thruster(0x08, "center", "horizontal") 
#thruster2 = thruster(0x09, "bottom left", "vertical")

while True:

    for i in range(15):
        thruster.impulse(1)
        print("Fire")
    thruster.open(0)
    print("Thruster Open")
    sleep(1)
    thruster.close(0)
    print("Thruster Closed")

        
        

