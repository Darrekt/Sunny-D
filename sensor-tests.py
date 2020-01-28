import smbus
import math

# Initialisation
bus = smbus.SMBus(1)
bus.write_byte_data(0x39, 0x0, 0x3)

# Polling loop
while True:
    ch0_lo = bus.read_byte_data(0x39, 0xC) & 0xFF
    ch0_hi = bus.read_byte_data(0x39, 0xD) & 0xFF

    ch1_lo = bus.read_byte_data(0x39, 0xE) & 0xFF
    ch1_hi = bus.read_byte_data(0x39, 0xF) & 0xFF

    ch0 = ch0_lo | (ch0_hi << 8)
    ch1 = ch1_lo | (ch1_hi << 8)
    
    coeff = float(ch1) / float(ch0)   
    if (0 < coeff and coeff <= 0.5)
        lux = 0.0304 * ch0 - 0.062 * ch0 * ((ch1/ch0))
