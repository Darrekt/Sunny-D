import smbus

# Initialisation
bus = smbus.SMBus(1)
bus.write_byte_data(0x39, 0x0, 0x3)

# Polling loop
while True:
    CH0_Lo = bus.read_byte_data(0x39, 0xC)
    CH0_Hi = bus.read_byte_data(0x39, 0xD)

    CH1_Lo = bus.read_byte_data(0x39, 0xE)
    CH1_Hi = bus.read_byte_data(0x39, 0xF)
